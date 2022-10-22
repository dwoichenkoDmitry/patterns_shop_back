from django.contrib import admin

# Register your models here.
from .models import BagProducts
from .models import SaledProducts


admin.site.register(BagProducts)
admin.site.register(SaledProducts)
