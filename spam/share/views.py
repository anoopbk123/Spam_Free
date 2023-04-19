from django.db import connection
from django.shortcuts import render
from share.models import Share
from user_reg.models import UserReg
from chat.models import Chat
from comment.models import Comment
from like_photo.models import LikePhoto
from login.models import Login
from django.http import HttpResponseRedirect
import datetime
from django.core.files.storage import FileSystemStorage

# Create your views here.
def share_photo(request):
    uid = request.session["uid"]
    objj = UserReg.objects.filter(user_id=uid)  # name
    gm = Chat.objects.filter(friend_id=uid)
    context = {
        'name': objj,
        'chat':gm
    }
    if request.method == "POST":
        obj=Share()
        obj.user_id=uid
        obj.date=datetime.date.today()
        obj.time=datetime.datetime.now().strftime("%I:%M:%S")

        myfile = request.FILES["photo"]
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        obj.media=myfile.name

        obj.save()

        ob=LikePhoto()
        ob.share_id=obj.share_id
        ob.user_id=uid
        ob.like_count="0"
        ob.save()
    return render(request,'share/share_photo.html',context)

def news_feed(request):
    uid = request.session["uid"]
    objj = UserReg.objects.filter(user_id=uid)  # name
    # cc=Counter(LikePhoto.objects.all().values_list('share_id',flat=True))
    # print(cc)
    gm = Chat.objects.filter(friend_id=uid)

    objlist=connection.cursor()
    objlist.execute("SELECT * FROM friends,share,user_reg,like_photo WHERE friends.user_id=%s AND friends.request_status='accepted' AND share.user_id=friends.f_user_id AND share.user_id=user_reg.user_id AND like_photo.share_id=share.share_id",[uid])

    # objcount=connection.cursor()
    # objcount.execute("SELECT share_id,COUNT(*) FROM like_photo GROUP BY share_id")

    context = {
        'name': objj,
        'images':objlist.fetchall(),
        'chat': gm

    }

    return render(request,'share/news_feed.html',context)

def view_post(request):
    uid = request.session["uid"]
    objj = UserReg.objects.filter(user_id=uid)  # name

    objlist = connection.cursor()
    objlist.execute(
        "SELECT share.*,like_photo.* FROM share INNER JOIN like_photo ON share.share_id=like_photo.share_id WHERE share.user_id=%s",[uid])

    sh=Share.objects.filter(user_id=uid)
    gm = Chat.objects.filter(friend_id=uid)
    context = {
        'name': objj,
        'share':sh,
        'images': objlist.fetchall(),
        'chat':gm
    }


    return  render(request,'share/view_post.html',context)

def view_comments(request,idd):
    uid = request.session["uid"]
    objj = UserReg.objects.filter(user_id=uid)  # name
    #
    # obj = UserReg.objects.get(user_id=idd)
    # obj.status = "blocked"
    # obj.save()
    #
    # ob = Login.objects.get(user_id=idd)
    # ob.type = "user pending"
    # ob.save()

    obj =Comment.objects.filter(share_id=idd)

    gm = Chat.objects.filter(friend_id=uid)
    commenttt = {
        'com': obj,
        'name': objj,
        'chat':gm


    }
    return render(request, 'share/view_comments.html',commenttt)



def share_del(request,idd):
    obj=Share.objects.get(share_id=idd).delete()
    return HttpResponseRedirect('/share/view_post/')
# def block_friend(request,ab):
#     uid = request.session["uid"]
#     objj = UserReg.objects.filter(user_id=uid)  # name
#
#     obj = UserReg.objects.get(user_id=ab)
#     obj.status = "blocked"
#     obj.save()
#
#     ob = Login.objects.get(user_id=ab)
#     ob.type = "user pending"
#     ob.save()
#
#     # objj = ReportedComments.objects.all()
#     # obj = ReportedComments.objects.
#     block = {
#         'blo': objj,
#         'name': obj
#     }
#     return render(request,'share/view_comments.html',block)


