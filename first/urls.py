from django.urls import path
from . import views 


urlpatterns = [
    path('home', views.home, name="home"),
    path('stocks', views.stocks, name='stocks'),
    
    path('stocks/edit/<stock_id>', views.edit, name='edit')
]
