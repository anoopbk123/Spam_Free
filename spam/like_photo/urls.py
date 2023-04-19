from django.urls import  re_path
from like_photo import views

urlpatterns = [
     re_path('like_photo/(?P<idd>\w+)', views.like, name='like')


]
