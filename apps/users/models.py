from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
GENDER_CHOICE=(
    ('M','Male'),
    ('F','Female')
               )

class BaseModel(models.Model):
    add_time = models.DateTimeField(default=datetime.now, verbose_name='add_time')
    class Meta:
        abstract=True

class UserProfile(AbstractUser):
    nick_name=models.CharField(max_length=50,
                               verbose_name='Nice Name',default='')
    birthday=models.DateField(verbose_name='Birthday',
                              null=True,blank=True)
    gender=models.CharField(verbose_name='Gender',choices=GENDER_CHOICE
                            ,max_length=6)
    address=models.CharField(max_length=100,verbose_name='address',
                             default='' )
    mobile=models.CharField(max_length=11,unique=True,
                            verbose_name='Mobile Number')
    image=models.ImageField(upload_to='head_image/%Y/%m',
                            default='default.jpg')

    class Meta:
        verbose_name='User_Profile'
        verbose_name_plural=verbose_name

    def __str__(self):
        if self.nick_name:
            return self.nick_name
        else:
            return self.username
