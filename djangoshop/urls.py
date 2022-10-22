"""djangoshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from customers import views as vi
from users import views as userViews
from qestionBase import views as questionViews
from probImg import views as probViews
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.conf.urls.static import static
from productsList import views as prodViews
from salesUser import views as salesViews
from courses import views as coursesViews

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('api/register/', userViews.RegisterUser),
    re_path('api/adminRegister/', userViews.RegisterAdmin),
    re_path('api/sendCode/', userViews.sendMailRegistration),
    re_path('api/questionSave/', questionViews.SaveQuestion),
    re_path('api/GetAllQuestions/', questionViews.GetAllQuestions),
    re_path('api/DeleteQuestion/', questionViews.DeleteQuestion),
    path('api/checkUser/<str:login>', userViews.CheckLogin),
    path('api/checkUser/<str:login>/<str:password>', userViews.signUpUser),

    path('api/products/allCategories', prodViews.getAllCategories),
    path('api/products/addCategories', prodViews.AddNewCategories),
    path('api/products/addProduct', prodViews.AddNewProduct),
    path('api/products/addSizes', prodViews.setFilesAndSizes),
    path('api/products/getCategoryId/<str:name>', prodViews.getProductsForCategoryName),
    path('api/products/getProductForId/<str:id>', prodViews.getProductForId),
    path('api/products/getProductCommentaries/<str:id>', prodViews.getProductCommentaries),
    path('api/products/AddComment', prodViews.AddComment),
    path('api/products/getAllProductMainInfo', prodViews.getAllProductMainInfo),
    path('api/products/DeleteProductForId', prodViews.DeleteProductForId),
    path('api/products/UpdateProductMainInfo', prodViews.UpdateProductMainInfo),
    path('api/products/UpdateProductImage', prodViews.UpdateProductImage),
    path('api/products/getAllCategoriesForUpdate', prodViews.getAllCategoriesForUpdate),
    path('api/products/deleteCategory', prodViews.deleteCategory),
    path('api/products/changeCategoryForId', prodViews.changeCategoryForId),
    path('api/products/GetFourLastProducts', prodViews.GetFourLastProducts),
    path('api/products/ChangeCategoryForProductId', prodViews.ChangeCategoryForProductId),
    path('api/products/GetSizesForProductId/<str:id>', prodViews.GetSizesForProductId),
    path('api/products/AddNewFileOnProduct', prodViews.AddNewFileOnProduct),
    path('api/products/DeleteSizeOnProduct', prodViews.DeleteSizeOnProduct),
    path('api/products/UpdateFileOnProduct', prodViews.UpdateFileOnProduct),

    path('api/sales/AddProductOnTheBag', salesViews.AddProductOnTheBag),
    path('api/sales/GetProductOnBag/<str:login>', salesViews.GetProductOnBag),
    path('api/sales/DeleteProductOnBag', salesViews.DeleteProductOnBag),
    path('api/sales/GetSizesOfLogin/<str:login>/<str:id>', salesViews.GetSizesOfLogin),
    path('api/sales/SalesProducts', salesViews.SalesProducts),
    path('api/sales/CheckPayment', salesViews.CheckPayment),
    path('api/sales/CheckBagPrice/<str:login>', salesViews.CheckBagPrice),
    path('api/sales/GetSaledProductsForLogin/<str:login>', salesViews.GetSaledProductsForLogin),

    path('api/courses/AddCourse', coursesViews.AddCourse),
    path('api/courses/DeleteCourse', coursesViews.DeleteCourse),
    path('api/courses/UpdateCourse', coursesViews.UpdateCourse),
    path('api/courses/GetAllCourses', coursesViews.GetAllCourses),

]

# Register viewset
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.MEDIA_URL_FILE, document_root=settings.MEDIA_ROOT_FILE)


