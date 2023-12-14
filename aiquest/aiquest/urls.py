"""
URL configuration for aiquest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
#from machine_learning import views as ml  #importing views of app machine_learning
#from Blogs import views as blg

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ml/',include('machine_learning.urls')),
    path('blog/',include('Blogs.urls')),
    #path('deep/',include('deep_learning.urls')),
    
    #OLD WAYS/Alternates
    #path('', ml.apps),
    #path('ml/', ml.machine), #using function 'machine' defined in views of machine_leaning app
    #path('dl/',ml.deep_learning),
    #path('about/',ml.about),
    #path('blogs/',blg.blogs),
    
    ]
