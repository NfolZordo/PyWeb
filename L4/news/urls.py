from django.urls import path, include
from news import views
from news.views import Register

urlpatterns = [

    path('', include('django.contrib.auth.urls')),

    path('register/', Register.as_view(), name='register'),
]
