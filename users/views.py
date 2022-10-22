
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import random
import string
from django.contrib.auth.models import User

def createCode():
    letters = string.ascii_uppercase
    rand_string = ''.join(random.choice(letters) for i in range(5))
    return rand_string

# Create your views here.
@api_view(['POST'])
def sendMailRegistration(request):
    if request.method == 'POST':
        sender = "dwoichenko@mail.ru"
        password = "JchUzAv7tnb7aTgthVVk"
        code = createCode()
        server = smtplib.SMTP("smtp.mail.ru", 587)
        server.starttls()

        msg = MIMEText(f'{code}', 'plain', 'utf-8')
        msg['Subject'] = Header('Код авторизации', 'utf-8')
        try:
            server.login(sender, password)
            server.sendmail(sender, request.data['mail'], msg.as_string())
            return Response({'data': code}, status=status.HTTP_201_CREATED)
        except Exception as ex:
            print(ex)
            return Response({'data': 'canseled'})
        finally:
            server.quit()

@api_view(['POST'])
def RegisterUser(request):
    if request.method == 'POST':
        user = User.objects.create_user(username=request.data['login'],
                                        email=request.data['mail'],
                                        first_name=request.data['name'],
                                        password=request.data['password'])
        user.save()
        return Response({'data': "Created"}, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def CheckLogin(request, login):
        try:
            user = User.objects.get(username=login)
        except User.DoesNotExist:
            return Response({'check': "allowed"}, status=status.HTTP_201_CREATED)
        if request.method == 'GET':
            return Response({'check': "fail"}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def signUpUser(request, login, password):
    try:
        user = User.objects.get(username=login)
    except User.DoesNotExist:
        return Response({'check': 'notExist'})
    if request.method == 'GET':
        return Response({'check': user.check_password(password), 'name': user.first_name, 'mail': user.email, 'admin': user.is_staff})


@api_view(['POST'])
def RegisterAdmin(request):
    if request.method == 'POST':


        user = User.objects.create_user(username=request.data['login'],
                                        email=request.data['mail'],
                                        name='admin',
                                        password=request.data['password'],
                                        is_staff=True
        )
        user.save()
        return Response({'data': "Created"}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def Prover(request):
    img = request.data['photo']

    return Response({'data': img}, status=status.HTTP_201_CREATED)