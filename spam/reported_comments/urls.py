from django.urls import  re_path
from reported_comments import views

urlpatterns = [
     re_path('view_cyberbullying_report/',views.view_cyberbullying_report),
     re_path('view_block/(?P<cdf>\w+)',views.view_block,name='block_user')

    ]


