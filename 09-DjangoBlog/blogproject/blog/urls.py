from . import views
from django.urls import path

urlpatterns = [
    path('', views.ArticleList.as_view(), name='home'),
    path('<slug:slug>/', views.ArticleView.as_view(), name='article_view'),
    path('about', views.AboutView.as_view(), name='about_view'),
]
