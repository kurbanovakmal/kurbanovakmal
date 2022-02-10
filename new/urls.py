from django.urls import path
from .views import BlogViews,BlogDetailViews


urlpatterns = [
    path('',BlogViews.as_view(),name='home'),
    path('post/<int:pk>/',BlogDetailViews.as_view(),name='post_detail')

]