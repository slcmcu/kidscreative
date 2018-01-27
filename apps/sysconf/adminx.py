# -*- coding: UTF-8 -*-
# __author__ : RobbieHan
# __data__  : 2018/1/24

import xadmin
from xadmin import views
from .models import FirmInfo, Menu


class GlobalSettings(object):
    site_title = "创想乾坤后台管理系统"
    site_footer = "Copyright © 2016-2017 RobbieHan. Version1.0.0"
    menu_style = "accordion"  # 导航菜单折叠


class FirmInfoAdmin(object):
    list_display = ['comName', 'telephone', 'email', 'address']


class MenuAdmin(object):
    list_display = ['menuName', 'code', 'icon', 'url', 'status', 'quickLink', 'parent', 'sortNumber']
    list_editable = ['status', 'url', 'sortNumber', 'quickLink']

xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(FirmInfo, FirmInfoAdmin)
xadmin.site.register(Menu, MenuAdmin)
