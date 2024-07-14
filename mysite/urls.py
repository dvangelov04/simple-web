from django.contrib import admin
from django.urls import path, include
from registration import views




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path(' /', include("first.urls")),
    path('account/', include("registration.urls"))
]
