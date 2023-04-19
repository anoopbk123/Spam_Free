from django.db import models
class LikePhoto(models.Model):
    like_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    like_count = models.CharField(max_length=100)
    share_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'like_photo'
