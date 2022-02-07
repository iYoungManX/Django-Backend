from datetime import datetime

from django.db import models

from apps.users.models import BaseModel
from apps.orgnizations.models import Teacher,CourseOrg
# Create your models here.



class Course(BaseModel):
    course_org=models.ForeignKey(CourseOrg,null=True,blank=True,on_delete=models.CASCADE,verbose_name='course_org')
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE,verbose_name='teacher')
    name=models.CharField(verbose_name='Class_Name',max_length=50)
    desc=models.CharField(verbose_name='Class_Description',max_length=300)
    learn_time=models.IntegerField(default=0,verbose_name='learn_time(min)')
    degree=models.CharField(verbose_name='degree',
                            choices=(('cj','low'),
                                     ('zj','medium'),
                                     ('gj','high')),max_length=10)
    students = models.IntegerField(default=0, verbose_name='student_number')
    fav_nums=models.IntegerField(default=0,verbose_name='favorite_number')
    click_nums=models.IntegerField(default=0,verbose_name='click_number')
    category=models.CharField(default='Backend',max_length=20,
                              verbose_name='class_category')
    tag=models.CharField(default='',verbose_name='class_tag',max_length=10)
    youneed_know=models.CharField(default='',max_length=300,
                                  verbose_name='need_know')
    techer_tell=models.CharField(default='',max_length=300,
                                 verbose_name='teacher_tell_you')
    detail=models.TextField(verbose_name='class_detail')
    image=models.ImageField(upload_to='course/%Y/%m',verbose_name='tag_image',
                            max_length=100)
    is_classics=models.BooleanField(default=True,verbose_name='classicornot')
    class Meta:
        verbose_name='Course'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.name

class Lesson(BaseModel):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,verbose_name='Chapter_name')
    learn_times=models.IntegerField(default=0,verbose_name="Learn_time(min)")


    class Meta:
        verbose_name='Lesson'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.name

class Video(BaseModel):
    lesson=models.ForeignKey(Lesson,verbose_name='Chapter',
                             on_delete=models.CASCADE)
    name=models.CharField(max_length=100,verbose_name='Video_name')
    learn_times = models.IntegerField(default=0, verbose_name="Learn_time(min)")
    url=models.CharField(max_length=200,verbose_name='url_address')
    class Meta:
        verbose_name='Video'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.name


class CourseResources(BaseModel):
    course=models.ForeignKey(Course,on_delete=models.CASCADE,
                             verbose_name='course')
    name=models.CharField(max_length=100,verbose_name='name')
    file=models.FileField(upload_to='course/resource/%Y/%m',
                          verbose_name="download_address",max_length=200)

    class Meta:
        verbose_name='class_resources'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name
