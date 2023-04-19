from django.db import models
from user_reg.models import UserReg

# class Comment(models.Model):
#     comment_id = models.AutoField(primary_key=True)
#     friend_id = models.IntegerField()
#     # user_id = models.IntegerField()
#     user = models.ForeignKey(UserReg,to_field='user_id',on_delete=models.CASCADE)
#     comment = models.CharField(max_length=100)
#     date = models.CharField(max_length=20)
#     time = models.CharField(max_length=20)
#     share_id = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'comment'

class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    # friend_id = models.IntegerField()
    friend = models.ForeignKey(UserReg, to_field='user_id', on_delete=models.CASCADE, related_name='cba')
    # user_id = models.IntegerField()
    user=models.ForeignKey(UserReg,to_field='user_id',on_delete=models.CASCADE,related_name='abc')
    comment = models.CharField(max_length=300)
    date = models.CharField(max_length=20)
    time = models.CharField(max_length=20)
    share_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'comment'








