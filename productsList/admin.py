from django.contrib import admin

# Register your models here.
from .models import ProductsList
from .models import FilesProduct
from .models import CommentariesProduct
from .models import CategoriesProduct
from .models import CategoriesAll

admin.site.register(ProductsList)
admin.site.register(FilesProduct)
admin.site.register(CommentariesProduct)
admin.site.register(CategoriesProduct)
admin.site.register(CategoriesAll)