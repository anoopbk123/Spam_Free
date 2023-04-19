from django.shortcuts import render
from like_photo.models import LikePhoto
from share.models import Share
from django.http import HttpResponseRedirect
import datetime
# Create your views here.
def like(request,idd):
    uid=request.session["uid"]
    obj=LikePhoto.objects.get(share_id=idd)
    # obj.user_id=uid
    obj.like_count=int(obj.like_count)+1
    print(obj.like_count)
    # obj.share_id=idd
    obj.save()
    return HttpResponseRedirect('/share/news_feed/')

