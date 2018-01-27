from django.shortcuts import render
from django.views.generic.base import View
from django.shortcuts import get_object_or_404

from blog.models import Articles, ArticleLabel


def get_article_label():
    article_label = ArticleLabel.objects.all()
    return article_label


def get_hot_articles():
    """
    获取阅读量最高文章：用户右侧热门文章推荐
    :return:
    """

    hot_articles = Articles.objects.order_by('-click_num')[:8]
    return hot_articles



class ArticlesListView(View):
    def get(self, request):
        article_label = get_article_label()
        hot_articles = get_hot_articles()
        if 'title' in request.GET and request.GET.get('title'):
            title = request.GET.get('title')
            articles_list = Articles.objects.filter(title__icontains=title)
        else:
            articles_list = Articles.objects.all()

        ret = {
            'articles_list': articles_list,
            'article_label': article_label,
            'hot_articles': hot_articles
        }
        return render(request, 'blog/article_list.html', ret)


class ArticleDetailView(View):
    """
    文章详情页：通过动态url实现前端页面向后端传递文章id来获取文章详情
    """
    def get(self, request, id):
        article_detail = get_object_or_404(Articles, id=id)
        article_label = get_article_label()
        hot_articles = get_hot_articles()

        click_num = article_detail.click_num
        click_num += 1
        article_detail.click_num = click_num
        article_detail.save()

        ret = {
            'article_detail': article_detail,
            'article_label': article_label,
            'hot_articles': hot_articles,
        }
        return render(request, 'blog/article_detail.html', ret)


class LabelSearchView(View):
    """
    标签搜索：通过选中标签获得具有该标签属性的文章列表
    """
    def get(self, request, label):
        article_label = get_article_label()
        hot_articles = get_hot_articles()
        label = get_object_or_404(ArticleLabel, name=label)
        articles_list = label.tag.all()

        ret = {
            'articles_list': articles_list,
            'article_label': article_label,
            'hot_articles': hot_articles
        }
        return render(request, 'blog/article_list.html', ret)


