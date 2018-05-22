from django.urls import path

from . import views

#app_name = 'kafe'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.addProduct, name='add'),
    path('addSuccess/', views.success, name = 'success'),
    path('delete/<int:id>/', views.productDelete, name ='delete'),
]
#'delete/<int:id>/'
