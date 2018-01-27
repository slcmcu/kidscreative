# -*- coding: UTF-8 -*-
# __author__ : RobbieHan
# __data__  : 2018/1/24

from django.utils.deprecation import MiddlewareMixin

from .models import FirmInfo, Menu


class GetBasicConfigMiddleware(MiddlewareMixin):
    """
    用于获取页面显示的基础信息：公司信息、导航菜单等
    """
    def get_basic_confing(self, request):
        if not hasattr(request, '_basic_config'):
            firm_info = FirmInfo.objects.last()
            menu = Menu.objects.values()
            request._basic_config = {'firm_info': firm_info, 'menu': menu}
        return request._basic_config

    def process_request(self, request):
        request.basic_confing = self.get_basic_confing(request)
        pass
