from django.shortcuts import render
from django.views.generic.base import View

from sysconf.models import FirmInfo
from blog.models import Articles


class IndexPageView(View):
    def get(self, request):
        latest_articles = Articles.objects.order_by('-add_time')[0:6]
        ret = {"latest_articles": latest_articles}
        return render(request, 'main/home.html', ret)


class ContactView(View):
    def get(self, request):
        firm_info = FirmInfo.objects.last()
        ret = {'firm_info': firm_info}
        return render(request, 'main/contact.html', ret)


