from django.urls import  re_path
from comment import views


urlpatterns = [
     re_path('comment/(?P<cid>\w+)',views.comment,name='com')

]
