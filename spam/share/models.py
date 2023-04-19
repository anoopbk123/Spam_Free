from django.db import models

# Create your models here.
class Share(models.Model):
    share_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    media = models.CharField(max_length=100)
    date = models.CharField(max_length=20)
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'share'





