#project/blog/urls.py

from django.urls import path
from . import views


app_name = 'clothing'

urlpatterns = [
        path('', views.IndexView.as_view(), name='index'),
        path('category/<str:category>/', views.CategoryView.as_view(),
                                       name='category'),
        path('tag/<str:tag>/', views.TagView.as_view(),
                                       name='tag'),
        # path('', views.index, name='index'),
        # path('category/<str:category>/', views.category, name='category'),
        # path('tag/<str:tag>/', views.tag, name='tag'),
        path('detail/<int:blog_id>/', views.detail, name='detail'),
]
