from django.db import models
from apps.users.models import BaseModel


# Create your models here.

class City(BaseModel):
    name=models.CharField(max_length=20,verbose_name='city')
    desc=models.CharField(max_length=200,verbose_name='description')
    class Meta:
        verbose_name='City'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name


class CourseOrg(BaseModel):
    name=models.CharField(max_length=50,verbose_name='org_name')
    desc=models.TextField(verbose_name='description')
    tag=models.CharField(default='Well-known',max_length=10,verbose_name='tag')
    address=models.CharField(default='',max_length=80,verbose_name='address')
    category=models.CharField(default='pxjg',verbose_name='org_category',
                              max_length=4,choices=(('pxjg',"Orgnization"),
                                                    ('gr',"Personal"),
                                                    ('gx','University')
                                                    ))
    click_nums = models.IntegerField(default=0, verbose_name='click_number')
    fav_nums = models.IntegerField(default=0, verbose_name='favorite_number')
    image = models.ImageField(upload_to='Org/%Y/%m', verbose_name='Logo',
                              max_length=100)
    student=models.IntegerField(default=0,verbose_name='student_number')
    course_nums=models.IntegerField(default=0,verbose_name='course_numbers')
    city=models.ForeignKey(City,on_delete=models.CASCADE,verbose_name='city',default='2')
    is_auth=models.BooleanField(default=False,verbose_name='auth_or_not')
    is_gold=models.BooleanField(default=False,verbose_name='gold_or_not')
    def courses(self):
        courses=self.course_set.filter(is_classics=True)[:3]
        return courses

    class Meta:
        verbose_name='Orgnization'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.name

class Teacher(BaseModel):
    org=models.ForeignKey(CourseOrg,on_delete=models.CASCADE,
                          verbose_name='Orgnizations')
    name=models.CharField(max_length=20,verbose_name='Teacher')
    work_years=models.IntegerField(default=0,verbose_name='work_years')
    work_company=models.CharField(max_length=50,verbose_name='work_company')
    work_position=models.CharField(max_length=50,verbose_name='work_position')
    points=models.CharField(max_length=50,verbose_name='teaching_points')
    age=models.IntegerField(default=18,verbose_name='age')
    click_nums = models.IntegerField(default=0, verbose_name='click_number')
    fav_nums = models.IntegerField(default=0, verbose_name='favorite_number')
    image = models.ImageField(upload_to='Teacher/%Y/%m', verbose_name='image',
                              max_length=100)
    desc=models.CharField(max_length=200,verbose_name='description')
    class Meta:
        verbose_name='Teacher'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.name