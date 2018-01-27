# -*- coding: UTF-8 -*-
# __author__ : RobbieHan
# __data__  : 2018/1/24

import xadmin

from .models import ArticleLabel, Articles


class ArticleLabelAdmin(object):
    list_display = ['id', 'name', 'colorNum']


class ArticlesAdmin(object):
    list_display = ["id", "title", "label", "add_time", "modify_time", "click_num"]
    search_fields = ['title', 'label']
    list_filter = ["title", "label", "add_time", "modify_time", "click_num"]
    style_fields = {"content": "ueditor"}


xadmin.site.register(ArticleLabel, ArticleLabelAdmin)
xadmin.site.register(Articles, ArticlesAdmin)
