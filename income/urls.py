
from django.contrib import admin
from django.urls import path
from . import views as v
urlpatterns = [
        path('-income',v.add_income,name='addincome'),
]
