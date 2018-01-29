from django.shortcuts import render
from django.views.generic.base import View

from sysconf.models import FirmInfo
from blog.models import Articles
from courses.models import Course

class IndexPageView(View):
    def get(self, request):
        latest_articles = Articles.objects.order_by('-add_time')[0:6]
        hot_courses = Course.objects.all()[0:6]
        ret = {
            "latest_articles": latest_articles,
            "hot_courses": hot_courses
        }
        return render(request, 'main/home.html', ret)


class ContactView(View):
    def get(self, request):
        firm_info = FirmInfo.objects.last()
        ret = {'firm_info': firm_info}
        return render(request, 'main/contact.html', ret)



