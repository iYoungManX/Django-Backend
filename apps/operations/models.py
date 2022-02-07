from django.db import models
from django.contrib.auth import get_user_model
from apps.users.models import BaseModel
from apps.courses.models import Course
# Create your models here.

UserProfile=get_user_model()
class UserAsk(BaseModel):
    name=models.CharField(max_length=20,verbose_name='name')
    mobile=models.CharField(max_length=11,verbose_name='mobile')
    course_name=models.CharField(max_length=50,verbose_name='class_name')

    class Meta:
        verbose_name="User_Questions"
        verbose_name_plural=verbose_name
    def __str__(self):
        return '{name}_{course}({mobile})'.format(name=self.name,course=self.course_name,
                                                  mobile=self.mobile)

class CourseComments(BaseModel):
    user=models.ForeignKey(UserProfile,verbose_name='user',on_delete=models.CASCADE)
    course=models.ForeignKey(Course,verbose_name='course',on_delete=models.CASCADE)
    comments=models.CharField(max_length=200,verbose_name='comments')

    class Meta:
        verbose_name="course_comments"
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.comments

class UserFavorite(BaseModel):
    user = models.ForeignKey(UserProfile, verbose_name='user',on_delete=models.CASCADE)
    fav_id=models.IntegerField(verbose_name='id')
    fac_type=models.IntegerField(choices=((1,'class'),
                                          (2,'orgnization'),
                                          (3,'teacher')),
                                 default=1,verbose_name='fav_type'
                                 )

    class Meta:
        verbose_name = "user_favorite"
        verbose_name_plural = verbose_name
    def __str__(self):
        return '{user}_{id}'.format(user=self.user.name,id=self.fav_id)

class UserMessage(BaseModel):
    user=models.ForeignKey(UserProfile,verbose_name='user',on_delete=models.CASCADE)
    message=models.CharField(max_length=200,verbose_name='user_message')
    has_read=models.BooleanField(default=False,verbose_name='read_ornot')


    class Meta:
        verbose_name='user_message'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.message




class UserCourses(BaseModel):
    user=models.ForeignKey(UserProfile,verbose_name='user',on_delete=models.CASCADE)
    course=models.ForeignKey(Course,verbose_name='Course',on_delete=models.CASCADE)


    class Meta:
        verbose_name="user_class"
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.course.name





