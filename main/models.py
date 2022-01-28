from django.db import models
from numpy import True_
from member.models import Member
from sqlalchemy import null
# Create your models here.


class CommonPlace(models.Model):
    place_id = models.BigIntegerField(primary_key=True)
    place_name = models.TextField(null=True)
    phone = models.TextField(null=True)
    lat = models.TextField(null=True)
    lng = models.TextField(null=True)
    road_address = models.TextField(null=True)
    info = models.BigIntegerField(null=True)
    img = models.TextField(null=True)

    class Meta:
        db_table = 'place_common'
        app_label = 'main'
        managed = False

    def place_count_by_count():
        count = CommonPlace.objects.all().count()
        return count


class museumDetail(models.Model):
    # commonplace = models.ForeignKey(CommonPlace, on_delete=models.SET_NULL, null = True, db_column='place_id')
    place_id = models.OneToOneField(
        CommonPlace, primary_key=True, db_column='place_id', on_delete=models.CASCADE)
    website = models.TextField(null=True)
    week_begin = models.TextField(null=True)
    week_end = models.TextField(null=True)
    holiday_begin = models.TextField(null=True)
    holiday_end = models.TextField(null=True)
    close_info = models.TextField(null=True)
    img = models.TextField(null=True)

    class Meta:
        db_table = 'museum_detail'
        managed = False


class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=100, null=True)
    date = models.DateField(auto_now=False, auto_now_add=False, default=null)
    id = models.ForeignKey(
        Member, on_delete=models.CASCADE, db_column=id)
    place_id = models.ForeignKey(
        CommonPlace, null=True, on_delete=models.SET_NULL)
    rate = models.IntegerField(null=True)

    class Meta:
        db_table = 'comment'
        managed = False
