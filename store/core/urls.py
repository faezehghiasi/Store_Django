
from django.contrib import admin
from django.urls import path, include,re_path
from . import views

app_name = 'core'

urlpatterns = [
    path('',views.ListOfProductsView.as_view(),name='products_list'),

]