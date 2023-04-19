from django.urls import  re_path
from share import views

urlpatterns = [
     re_path('share_photo/',views.share_photo),
     re_path('news_feed/',views.news_feed),
     re_path('view_post',views.view_post),
     re_path('view_comments/(?P<idd>\w+)', views.view_comments, name='commm'),
     re_path(r'^share_del/(?P<idd>\w+)', views.share_del, name='share_del'),
    # url('block_friend/(?P<ab>\w+)',views.block_friend, name='blockk')




]
