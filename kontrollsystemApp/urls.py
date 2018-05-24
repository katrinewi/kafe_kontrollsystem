from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.addProduct, name='add'),
    path('delete/<int:id>/', views.productDelete, name ='delete'),
    path('buy/<int:id>/', views.kjopProdukt, name='buy'),
    path('reset/', views.goToReset, name='reset'),
    path('reset/confirmed/', views.reset, name='confirmed')
]
