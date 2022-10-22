from django.db import migrations

def create_data(apps, schema_editor):
    ProductsList = apps.get_model('productsList', 'ProductsList')
    ProductsList(name="кофточка", price="235 руб", discount=False, description="описание", cloth="Ткани", addition="дополнение", course="ссылка").save()


    FilesProduct = apps.get_model('productsList', 'FilesProduct')
    FilesProduct(idProduct="456", size="46").save()

    CommentariesProduct = apps.get_model('productsList', 'CommentariesProduct')
    CommentariesProduct(idProduct="456", name="Марина", date="28 июль 2022", comment="какой то там коммент").save()

    CategoriesProduct = apps.get_model('productsList', 'CategoriesProduct')
    CategoriesProduct(idProduct="456", idCategories="32").save()

    CategoriesAll = apps.get_model('productsList', 'CategoriesAll')
    CategoriesAll(name="Куртки").save()

class Migration(migrations.Migration):

    dependencies = [
        ('productsList', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_data),
    ]