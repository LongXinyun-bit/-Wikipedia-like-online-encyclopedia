# encyclopedia/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>/", views.entry, name="entry"),
    path("search/", views.search, name="search"),
    path("new_page/", views.new_page, name="new_page"),  # 确保这一行存在
    path("edit/<str:title>/", views.edit, name="edit"),
]
