from django.shortcuts import render

from .models import BagProducts
from .models import SaledProducts
from productsList.models import ProductsList
from productsList.models import FilesProduct
# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from yookassa import Configuration, Payment, Refund
import uuid
from threading import Thread
from time import sleep
import json
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import random
import string
import email.message


@api_view(['POST'])
def AddProductOnTheBag(request):
    login = request.data['login']
    id = request.data['id']
    size = request.data['size']

    if(not BagProducts.objects.filter(loginUser=login, idProduct=id, size=size)):
        BagProducts(loginUser=login, idProduct=id, size=size).save()

    return Response({'answer': 'Created'})


@api_view(['POST'])
def AddProductOnSales(request):
    login = request.data['login']
    id = request.data['id']
    size = request.data['size']

    BagProducts(loginUser=login, idProduct=id, size=size).save()
    return Response({'answer': 'Created'})

@api_view(['GET'])
def GetProductOnBag(request, login):
    products = BagProducts.objects.filter(loginUser=login)
    mas = []
    for item in products:
        id = item.idProduct
        size = item.size
        productItem = ProductsList.objects.filter(id=id)[0]
        mas.append(
            {
                'id': id,
                'name': productItem.name,
                'price': productItem.price,
                'size': size,
                'image': str(productItem.image)
            }
        )
    return Response({'products': mas})


@api_view(['POST'])
def DeleteProductOnBag(request):
    login = request.data['login']
    id = request.data['id']
    size = request.data['size']

    BagProducts.objects.filter(loginUser=login, idProduct=id, size=size).delete()
    return Response({'answer': 'deleted'})


@api_view(['GET'])
def GetSizesOfLogin(request, login, id):
    sizesBag = BagProducts.objects.filter(loginUser=login, idProduct=id)
    sizesSaled = SaledProducts.objects.filter(loginUser=login, idProduct=id)
    masBag = []
    for item in sizesBag:
        masBag.append(item.size)
    masSaled=[]
    for item in sizesSaled:
        masSaled.append(item.size)
    return Response({'sizesBag': masBag, 'sizesSaled': masSaled})


def CheckPrice(login):
    price = 0
    bagProducts = BagProducts.objects.filter(loginUser=login)
    for item in bagProducts:
        price += float(ProductsList.objects.filter(id=item.idProduct)[0].price)
    return price


@api_view(['GET'])
def CheckBagPrice(request, login):
    return Response({'price': round(CheckPrice(login), 2)})


@api_view(['POST'])
def SalesProducts(request):
    Configuration.account_id = '938224'
    Configuration.secret_key = 'test_iFJJKCixcM5jsByBMPfmGD40riIrssg0llnogV-yzXQ'

    login = request.data['login']
    price = CheckPrice(login)

    payment = Payment.create({
        "amount": {
            "value": round(price, 2),
            "currency": "RUB"
        },
        "confirmation": {
            "type": "redirect",
            "return_url": "http://localhost:3000/"
        },
        "capture": True,
        "description": "Заказ №1"
    }, uuid.uuid4())

    return Response({'payment': payment})


@api_view(['POST'])
def CheckPayment(request):
    login = request.data['login']
    id = request.data['id']
    Thread(target=CheckFunc, args=(id, login)).start()
    return Response({'payment': 'fre'})


def CheckFunc(id, login):
    Configuration.account_id = '938224'
    Configuration.secret_key = 'test_iFJJKCixcM5jsByBMPfmGD40riIrssg0llnogV-yzXQ'
    while True:
        sleep(5)
        payment = json.loads((Payment.find_one(id)).json())
        if(payment['status']=='succeeded'):
            bagUser = BagProducts.objects.filter(loginUser=login)
            for item in bagUser:
                SaledProducts(loginUser=login, idProduct=item.idProduct, size=item.size).save()
                item.delete()
            break
        if(payment['status']=='canceled'):
            break



def SendSaledMail(mail, message):
    sender = "dwoichenko@mail.ru"
    password = "JchUzAv7tnb7aTgthVVk"
    email_content = """
<html lang="en">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <title>Document</title>
    <style type="text/css">
        .headerContainer {
            display: flex;
            justify-content: space-between;
            align-items: center;
            width: 100%;
            border: 1px black solid;
        }

        

        h1 {
            color: red;
        }
    </style>

</head>
<body>
    <div class="headerContainer">
        <h1>hiiy</h1>
    </div>
</body>
</html>"""
    server = smtplib.SMTP("smtp.mail.ru", 587)
    server.starttls()

    msg = email.message.Message()
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(email_content)

    msg['Subject'] = Header('Код авторизации', 'utf-8')
    try:
        server.login(sender, password)
        server.sendmail(sender, mail, msg.as_string())
        return Response({'data': 'jk'}, status=status.HTTP_201_CREATED)
    except Exception as ex:
        print(ex)
    finally:
        server.quit()


@api_view(['GET'])
def GetSaledProductsForLogin(request, login):
    sales = SaledProducts.objects.filter(loginUser=login)
    mas = []
    for item in sales:
        id = item.idProduct
        size = item.size
        product = ProductsList.objects.filter(id=id)[0]
        file = FilesProduct.objects.filter(idProduct=id, size=size)[0]
        mas.append(
            {
                'name': product.name,
                'course': product.course,
                'image': str(product.image),
                'size': file.size,
                'file': str(file.file)
            }
        )
    return Response({'products': mas})
