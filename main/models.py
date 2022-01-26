from cgitb import text
from pyexpat import model
from django.db import models
from sqlalchemy import null
# from django.contrib.gis.db.models.functions import Distance
# Create your models here.
class CommonPlace(models.Model):
    place_id = models.BigIntegerField(primary_key=True)
    place_name = models.TextField(null=True)
    phone = models.TextField(null=True)
    lat = models.TextField(null=True)
    lng = models.TextField(null=True)
    road_address = models.TextField(null=True)
    info = models.BigIntegerField(null=True)
    rate = models.IntegerField(null=True)

    class Meta :
        db_table = 'place_common'
        app_label = 'main'
        managed = False 

class museumDetail(models.Model):
    # commonplace = models.ForeignKey(CommonPlace, on_delete=models.SET_NULL, null = True, db_column='place_id')
    place_id = models.OneToOneField(CommonPlace, primary_key=True,db_column='place_id', on_delete=models.CASCADE)
    website = models.TextField(null=True)
    week_begin = models.TextField(null=True)
    week_end = models.TextField(null=True)
    holiday_begin = models.TextField(null=True)
    holiday_end = models.TextField(null=True)
    close_info = models.TextField(null=True)

    class Meta :
        db_table = 'museum_detail'
        managed = False


