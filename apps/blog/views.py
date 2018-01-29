from django.shortcuts import render
from django.views.generic.base import View
from django.shortcuts import get_object_or_404

from blog.models import Articles, ArticleLabel


def get_public_data():
    article_label = ArticleLabel.objects.all()
    hot_articles = Articles.objects.order_by('-click_num')[:8]
    ret = {
        'article_label': article_label,
        'hot_articles': hot_articles
    }
    return ret


class ArticlesListView(View):
    def get(self, request):
        ret = get_public_data()
        if 'title' in request.GET and request.GET.get('title'):
            title = request.GET.get('title')
            articles_list = Articles.objects.filter(title__icontains=title)
        else:
            articles_list = Articles.objects.all()
        ret['articles_list'] = articles_list
        return render(request, 'blog/article_list.html', ret)


class ArticleDetailView(View):
    """
    文章详情页：通过动态url实现前端页面向后端传递文章id来获取文章详情
    """
    def get(self, request, id):
        ret = get_public_data()
        article_detail = get_object_or_404(Articles, id=id)
        click_num = article_detail.click_num
        click_num += 1
        article_detail.click_num = click_num
        article_detail.save()
        ret['article_detail'] = article_detail
        return render(request, 'blog/article_detail.html', ret)


class LabelSearchView(View):
    """
    标签搜索：通过选中标签获得具有该标签属性的文章列表
    """
    def get(self, request, label):
        ret = get_public_data()
        label = get_object_or_404(ArticleLabel, name=label)
        articles_list = label.tag.all()
        ret['articles_list'] = articles_list
        return render(request, 'blog/article_list.html', ret)


