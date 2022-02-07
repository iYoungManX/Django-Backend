from django.shortcuts import render
from django.views.generic.base import View
from django.http import JsonResponse
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from apps.orgnizations.models import CourseOrg,City
from Online_Class.settings import MEDIA_URL
from apps.orgnizations.forms import AskAddForm

class AddAskView(View):
    def post(self,request,*args, **kwargs):
        userask_from=AskAddForm(request.POST)
        if userask_from.is_valid():
            userask_from.save(commit=True)
            return JsonResponse({
                'status':'success'
            })
        else:
            return JsonResponse({
                'status': 'fail',
                'msg':'add wrong'
            })


class OrgView(View):
    def get(self,request,*args, **kwargs):
        ## get data from database
        all_orgs=CourseOrg.objects.all()

        all_cities=City.objects.all()
        hot_orgs=all_orgs.order_by('-click_nums')[:3]
        ############### 筛选(机构类别) #############
        category=request.GET.get('ct','')
        if category:
            all_orgs=all_orgs.filter(category=category)
        orgs_num = all_orgs.count()
        ########################################

        ############### 筛选(城市) #############
        city_id = request.GET.get('city', '')
        if city_id:
            if city_id.isdigit():
                all_orgs = all_orgs.filter(city_id=int(city_id))
        orgs_num = all_orgs.count()
        ########################################

        ############### 排序 ###################
        sort=request.GET.get('sort','')
        if sort=='students':
            all_orgs=all_orgs.order_by('-student')
        elif sort=='courses':
            all_orgs=all_orgs.order_by('-course_nums')
        ########################################

        ############### 分页  ##################
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        # Provide Paginator with the request object for complete querystring generation

        p = Paginator(all_orgs, per_page=5,request=request)

        orgs = p.page(page)
        ########################################



        return render(request,'org-list.html',
                      {'all_orgs':orgs,'orgs_num':orgs_num,
                       'all_cities':all_cities,'category':category,
                       'city_id':city_id,
                       'sort':sort,
                       'hot_orgs':hot_orgs
                                               })


class OrgHomeView(View):
    def get(self,request,org_id,*args, **kwargs):
        course_org=CourseOrg.objects.get(id=int(org_id))
        course_org.click_nums+=1
        course_org.save()

        all_courses=course_org.course_set.all()[:3]
        all_teachers = course_org.teacher_set.all()[:1]
        return render(request,'org-detail-homepage.html',
                      {'all_courses':all_courses,
                       'all_teachers':all_teachers,
                       'course_org':course_org})
