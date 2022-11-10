from django.urls import path, re_path
from . import views

urlpatterns = [
    path("wiki", views.index, name="index"),
    path('wiki/random', views.randomArticle, name="random"),
    path('wiki/creation', views.creation, name="creation"),
    path('wiki/<slug:article>', views.article, name="article")

]
