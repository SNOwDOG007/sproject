from django.urls import path
from . import views

urlpatterns = [
   path("single_joinus", views.SingleJoinusView, name="single_joinus"),
   path("single_about", views.SingleAboutView, name="single_about"),
   path("single_blog", views.SingleBlogView, name="single_blog"),
   path("single_gallery", views.SingleGalleryView, name="single_gallery"),
]
 