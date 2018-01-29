from django.shortcuts import render
from django.views.generic.base import View
from django.db.models import Q

from .models import Course, Category, Tag


class CoursesListView(View):
    def get(self, request):
        courses_list = Course.objects.all()
        categorys = Category.objects.all()
        tags = Tag.objects.all()
        category_name = request.GET.get('category', '')
        if category_name:
            courses_list = courses_list.filter(category__name=category_name)
        tag_name = request.GET.get('tag', '')
        if tag_name:
            courses_list = courses_list.filter(tag__name=tag_name)
        search_name = request.GET.get('name', '')
        if search_name:
            courses_list = courses_list.filter(
                Q(name__icontains=search_name) | Q(category__name__icontains=search_name) | Q(tag__name__icontains=search_name)
            )

        ret = {
            'courses_list': courses_list,
            'categorys': categorys,
            'tags': tags,
            'category_name': category_name,
            'tag_name': tag_name,
            'search_name': search_name
        }
        return render(request, 'courses/courses_list.html', ret)


class CourseDetailView(View):
    def get(self, request):
        return render(request, 'courses/course_detail.html')