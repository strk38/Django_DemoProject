from django.urls import path
from . import views as blg

urlpatterns = [
    path('',blg.blogs, name='blogs'),
    path('t/', blg.teachers_info, name='teacher'),
    path('f/', blg.showFormsData, name='form'),
    path('r/', blg.registration),
]
