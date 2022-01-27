from django.db import models

# Create your models here.

<<<<<<< HEAD

# class User(models.Model):
#     username = models.CharField(verbose_name='이름', max_length=255)
#     id = models.CharField(verbose_name='아이디', max_length=255, primary_key=True)
#     password = models.CharField(verbose_name='비밀번호', max_length=255)
#     email = models.EmailField(
#         verbose_name='이메일', max_length=128, unique=True, default='')
#     GENDER = (
#         ('M', '남성(Man)'),
#         ('W', '여성(Woman)'),
#     )
#     usergender = models.CharField(
#         verbose_name='성별', max_length=1, choices=GENDER)
#     LOCATION = (
#         ('O', '승낙(O)'),
#         ('X', '거절(X)'),
#     )
#     location = models.CharField(
#         verbose_name='위치', max_length=1, choices=LOCATION)
#     country = models.CharField(verbose_name='지역', max_length=100)

#     class Meta:
#         db_table = 'user'
=======
class User(models.Model):
    username = models.CharField(verbose_name = '이름', max_length=255)
    id = models.CharField(verbose_name = '아이디', max_length=255, primary_key=True)
    password = models.CharField(verbose_name = '비밀번호', max_length=255)
    email = models.EmailField(verbose_name = '이메일', max_length = 128, unique = True, default ='')
    GENDER = (
        ('M', '남성(Man)'),
        ('W', '여성(Woman)'),
    )
    usergender = models.CharField(verbose_name = '성별', max_length= 1 , choices=GENDER)
    LOCATION = (
        ('O', '승낙(O)'),
        ('X', '거절(X)'),
    )
    location = models.CharField(verbose_name = '위치', max_length = 1, choices = LOCATION)
    country = models.CharField(verbose_name = '지역', max_length = 100)
    
    class Meta:
        db_table = 'user'
>>>>>>> 11423cffaf13ad01bc3a5e064a9e340e5f34c8b1
