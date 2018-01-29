from django.shortcuts import render
from django.views.generic.base import View

from .models import Course, Category, Tag


class CoursesListView(View):
    def get(self, request):
        ret = {}
        courses_list = Course.objects.all()
        ret['courses_list'] = courses_list
        return render(request, 'courses/courses_list.html', ret)




