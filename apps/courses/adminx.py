# -*- coding: UTF-8 -*-
# __author__ : RobbieHan
# __data__  : 2018/1/29

import xadmin
from .models import Category, Tag, Course


class CategoryAdmin(object):
    list_display = ['id', 'name']
    search_fields = ['name']


class TagAdmin(object):
    list_display = ["id", "name"]
    search_fields = ['name']


class CourseAdmin(object):
    list_display = ["id", "name", 'degree', 'category', 'tag', 'is_hot', 'add_time']
    search_fields = ['name']
    list_filter = ["name", "category", "tag"]
    style_fields = {"detail": "ueditor"}
    list_editable = ["category", 'is_hot']

xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Tag, TagAdmin)
xadmin.site.register(Course, CourseAdmin)
