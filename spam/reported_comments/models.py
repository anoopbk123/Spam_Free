from django.db import models
from user_reg.models import UserReg
# Create your models here.
# class ReportedComments(models.Model):
#     report_id = models.AutoField(primary_key=True)
#     # user_id = models.IntegerField()
#     user = models.ForeignKey(UserReg,to_field='user_id',on_delete=models.CASCADE)
#
#     comment_id = models.IntegerField()
#     report = models.CharField(max_length=50)
#     date = models.CharField(max_length=20)
#     time= models.CharField(max_length=20)
#     class Meta:
#         managed = False
#         db_table = 'reported_comments'


class ReportedComments(models.Model):
    report_id = models.AutoField(primary_key=True)
    # user_id = models.IntegerField()
    user = models.ForeignKey(UserReg,to_field='user_id',on_delete=models.CASCADE)
    comment_id = models.IntegerField()
    report = models.CharField(max_length=300)
    date = models.CharField(max_length=20)
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'reported_comments'


