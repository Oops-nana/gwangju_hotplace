from django.db import models

class Member(models.Model):
    user_id = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    agree = models.BooleanField()

    class Meta:
        db_table = 'user'
        app_label = 'member'
        managed = False