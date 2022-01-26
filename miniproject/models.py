from django.db import models

# Create your models here.

class Member(models.Model):
    user_name = models.CharField(verbose_name = '이름', max_length=300)
    user_id = models.CharField(verbose_name = '아이디', max_length=250, primary_key=True)
    user_pw = models.CharField(verbose_name = '비밀번호', max_length=300)
    user_email = models.EmailField(verbose_name = '이메일', max_length = 128, unique = True, default ='')
    LOCATION = (
        ('O', '승낙(O)'),
        ('X', '거절(X)'),
    )
    user_location = models.CharField(verbose_name = '위치', max_length = 1, choices = LOCATION)
    
    class Meta:
        db_table = 'user'
