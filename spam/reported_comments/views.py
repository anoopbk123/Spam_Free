from django.shortcuts import render
from reported_comments.models import ReportedComments
from user_reg.models import UserReg
from login.models import Login
# Create your views here.
def view_cyberbullying_report(request):
    uid = request.session["uid"]
    objj = UserReg.objects.filter(user_id=uid)  # name

    bk=UserReg.objects.filter(status='cyberbullying detected').values_list('user_id',flat=True)
    # print(bk)
    obj = ReportedComments.objects.all().exclude(user_id__in=bk)

    cyber=UserReg.objects.filter(status='cyberbullying detected')
    print(cyber)
    cyberbullying_report = {
        'creport': obj,
        'name':objj,
        'cyber':cyber
    }
    return render(request,'reported_comments/view_cyberbullying_report.html',cyberbullying_report)


def view_block(request,cdf):
    uid = request.session["uid"]
    obj = UserReg.objects.filter(user_id=uid)  # name

    obb = UserReg.objects.get(user_id=cdf)
    obb.status = "cyberbullying detected"
    obb.save()

    ob = Login.objects.get(user_id=cdf)
    ob.type = "user pending"
    ob.save()

    objj=ReportedComments.objects.all()
    # obj = ReportedComments.objects.
    block = {
        'blo': objj,
        'name':obj
    }
    return render(request,'reported_comments/view_block.html', block)


