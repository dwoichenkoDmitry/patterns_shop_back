from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from salesUser.models import BagProducts
from salesUser.models import SaledProducts
# Create your views here.
from .models import ProductsList
from .models import FilesProduct
from .models import CommentariesProduct
from .models import CategoriesProduct
from .models import CategoriesAll



@api_view(['GET'])
def getAllCategories(request):
    categories = CategoriesAll.objects.all()
    dict = {}
    for index, item in enumerate(categories):
        dict[index] = {'id': item.idCategories, 'name': item.name, 'image': str(item.image)}

    return Response({'data': dict})

@api_view(['POST'])
def AddNewCategories(request):
    name = request.data['name']
    photo = request.data['photo']
    CategoriesAll(name=name, image=photo).save()
    return Response({'answer': 'Created'})

@api_view(['POST'])
def AddNewProduct(request):
    name = request.data['name']
    price = request.data['price']
    discount = request.data['discount'] == "true"
    oldPrice = request.data['oldPrice']
    description = request.data['description']
    cloth = request.data['cloth']
    addition = request.data['addition']
    course = request.data['course']
    image = request.data['image']
    categories = request.data['categories']


    product = ProductsList(name=name, price=price, discount=discount,
                 oldPrice=oldPrice, description=description,
                 cloth=cloth, addition=addition, course=course,
                 image=image)
    product.save()
    id = product.id
    masCategories = categories.split('$')
    print("Массивчик ", "_"*10, masCategories)
    for item in masCategories:

        category = CategoriesAll.objects.filter(name=item)

        categoryId = category[0].idCategories

        CategoriesProduct(idProduct=id, idCategories=categoryId).save()

    return Response({'id': id, 'answer': 'Created'})

@api_view(['POST'])
def setFilesAndSizes(request):
    file = request.data['file']
    size = request.data['size']
    id = request.data['id']

    FilesProduct(idProduct=id, size=size, file=file).save()
    return Response({'answer': 'Created'})


@api_view(['GET'])
def getProductsForCategoryName(request, name):
    caregory = CategoriesAll.objects.filter(name=name)
    id = caregory[0].idCategories

    links = CategoriesProduct.objects.filter(idCategories=id)
    mas = []
    for item in links:
        product = ProductsList.objects.filter(id=item.idProduct)[0]

        mas.append({
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'discount': product.discount,
            'oldPrice': product.oldPrice,
            'image': str(product.image)
        })

    return Response({'products': mas})


@api_view(['GET'])
def getProductForId(request, id):
    product = ProductsList.objects.filter(id=id)[0]
    result = {
        'id': product.id,
        'name': product.name,
        'price': product.price,
        'discount': product.discount,
        'oldPrice': product.oldPrice,
        'description': product.description,
        'cloth': product.cloth,
        'addition': product.addition,
        'course': product.course,
        'image': str(product.image)
    }
    sizes = FilesProduct.objects.filter(idProduct=id)
    masSizes = []
    for item in sizes:
        masSizes.append(item.size)
    return Response({'products': result, 'sizes': masSizes})

@api_view(['GET'])
def getProductCommentaries(request, id):
    comments = CommentariesProduct.objects.filter(idProduct=id)
    result = []
    for item in comments:
        mas = item.date.split('$')
        result.append({
            'name': item.name,
            'date': item.date,
            'comment': item.comment,
            'image': str(item.image)
        })
    return Response({'comments': result})

dictMonth = {
    '0': 'Январь',
    '1': 'Февраль',
    '2': 'Март',
    '3': 'Апрель',
    '4': 'Май',
    '5': 'Июнь',
    '6': 'Июль',
    '7': 'Август',
    '8': 'Сентябрь',
    '9': 'Октябрь',
    '10': 'Ноябрь',
    '11': 'Декабрь',
}

@api_view(['POST'])
def AddComment(request):
    id = request.data['id']
    name = request.data['name']
    comment = request.data['comment']
    image = request.data['image']
    day = request.data['day']
    minute = request.data['minute']
    year = request.data['year']
    hour = request.data['hour']
    if(len(hour)==1):
        hour = f"0{hour}"
    if(len(minute)==1):
        minute= f"0{minute}"
    print("proverka________", request.data['month'])
    month = dictMonth[request.data['month']]
    date = f"{day} {month} {year}${hour}:{minute}"
    CommentariesProduct(idProduct=id, name=name, date=date, comment=comment, image=image).save()
    return Response({'answer': 'Created'})


@api_view(['GET'])
def getAllProductMainInfo(request):
    products = ProductsList.objects.all()
    mas = []
    for item in products:
        mas.append({
            'id': item.id,
            'name': item.name,
            'price': item.price,
            'image': str(item.image)
        })
    return Response({'products': mas})


@api_view(['POST'])
def DeleteProductForId(request):
    id = request.data['id']
    ProductsList.objects.filter(id=id).delete()
    FilesProduct.objects.filter(idProduct=id).delete()
    CommentariesProduct.objects.filter(idProduct=id).delete()
    CategoriesProduct.objects.filter(idProduct=id).delete()
    BagProducts.objects.filter(idProduct=id).delete()
    SaledProducts.objects.filter(idProduct=id).delete()
    return Response({'products': 'Deleted'})

@api_view(['POST'])
def UpdateProductMainInfo(request):
    id = request.data['id']
    name = request.data['name']
    price = request.data['price']
    discount = request.data['discount']
    oldPrice = request.data['oldPrice']
    description = request.data['description']
    cloth = request.data['cloth']
    addition = request.data['addition']
    course = request.data['course']
    product = ProductsList.objects.filter(id=id)[0]
    if(product.name != name):
        product.name = name
    if (product.price != price):
        product.price = price
    if (product.discount != discount):
        product.discount = discount
    if (product.oldPrice != oldPrice):
        product.oldPrice = oldPrice
    if (product.description != description):
        product.description = description
    if (product.cloth != cloth):
        product.cloth = cloth
    if (product.addition != addition):
        product.addition = addition
    if (product.course != course):
        product.course = course
    product.save()
    return Response({'products': 'Update'})


@api_view(['POST'])
def UpdateProductImage(request):
    image = request.data['image']
    id = request.data['id']
    product = ProductsList.objects.filter(id=id)[0]
    product.image = image
    product.save()
    return Response({'products': 'Update'})


@api_view(['GET'])
def getAllCategoriesForUpdate(request):
    products = CategoriesAll.objects.all()
    mas = []
    for item in products:
        mas.append({
            'id': item.idCategories,
            'name': item.name,
            'image': str(item.image)
        })
    return Response({'categories': mas})

@api_view(['POST'])
def deleteCategory(request):
    id = request.data['id']
    CategoriesAll.objects.filter(idCategories=id).delete()
    return Response({'answer': 'deleted'})

@api_view(['POST'])
def changeCategoryForId(request):
    id = request.data['id']
    name = request.data['name']
    imgUpdate = request.data['imgUpdate']
    category = CategoriesAll.objects.filter(idCategories=id)[0]
    if imgUpdate == 'true':
        image = request.data['image']
        category.image = image
    category.name = name
    category.save()
    return Response({'answer': 'updated'})

@api_view(['GET'])
def GetFourLastProducts(request):
    products = ProductsList.objects.all()
    mas = []
    if len(products) > 3:
        for item in products[len(products)-4:len(products)]:
           mas.append(
               {
                   'id': item.id,
                   'name': item.name,
                   'price': item.price,
                   'image': str(item.image)
               }
           )
    else:
        for item in products:
            mas.append(
                {
                    'id': item.id,
                    'name': item.name,
                    'price': item.price,
                    'image': str(item.image)
                }
            )
    return Response({'answer': mas})



@api_view(['POST'])
def ChangeCategoryForProductId(request):
    id = request.data['id']
    categories = request.data['categories']
    CategoriesProduct.objects.filter(idProduct=id).delete()
    for item in categories:
        CategoriesProduct(idProduct=id, idCategories=item).save()
    return Response({'answer': 'updated'})



@api_view(['GET'])
def GetSizesForProductId(request, id):
    sizes = FilesProduct.objects.filter(idProduct=id)
    mas = []
    for item in sizes:
        mas.append(item.size)
    return Response({'sizes': mas})


@api_view(['POST'])
def AddNewFileOnProduct(request):
    id = request.data['id']
    name = request.data['name']
    file = request.data['file']

    FilesProduct(idProduct=id, size=name, file=file).save()
    return Response({'answer': 'created'})

@api_view(['POST'])
def DeleteSizeOnProduct(request):
    size = request.data['size']
    id = request.data[id]

    FilesProduct.objects.filter(idProduct=id, size=size).delete()
    BagProducts.objects.filter(idProduct=id, size=size).delete()
    SaledProducts.objects.filter(idProduct=id, size=size).delete()
    return Response({'answer': 'deleted'})

@api_view(['POST'])
def UpdateFileOnProduct(request):
    id = request.data['id']
    size = request.data['size']
    file = request.data['file']

    fileCur = FilesProduct.objects.filter(idProduct=id, size=size)[0]
    fileCur.file = file
    fileCur.save()
    return Response({'answer': 'updated'})