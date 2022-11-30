from django.contrib import admin
from django.urls import path, include
from news import views
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('main_news/', views.index, name='home'),
    path('creation/', views.creation, name="creation"),
    path('personal/', views.personal, name="personal"),
    path('news/', include('news.urls')),
]
