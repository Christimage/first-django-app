from django.urls import path
from myfirstapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('fashion', views.fashion, name='fashion'),
    path('electronic', views.electronic, name='electronic'),
    path('jewellery', views.jewellery, name='jewellery'),
    path('register', views.register, name='register'),
]

