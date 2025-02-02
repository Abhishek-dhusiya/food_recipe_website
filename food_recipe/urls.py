"""
URL configuration for food_recipe project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
import django
from django.contrib import admin
from django.urls import path,include
from modules import views
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/',include('tinymce.urls')),
    path('',views.MyHtml,name='home'),
    path('signup/',views.Signup,name='signup'),
    path('login/',views.logins,name='login'),
    path('approve/',views.approve_user),
    path('logout/',views.LogoutPage,name='logout'),
    path('recipe/',views.food,name='recipe'),
    path('rec',views.addfeed,name='feedbacks'),
    path('details/', views.recipes_details, name='recipe_details'),
    path('chef/',views.chef_details,name="chefdetails"),
    path('cal/',views.cal,name='cal'),
    path('ch/',views.chef_info,name='chef_info'),
    path('apis/',views.apis,name="apis"),
    path('dashboard/', views.dashboard, name='dashboard')  
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)