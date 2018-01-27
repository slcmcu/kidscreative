from django.db import models

from DjangoUeditor.models import UEditorField


class ArticleLabel(models.Model):
    name = models.CharField(max_length=20, verbose_name="标签名称")
    colorNum = models.IntegerField(default=0, verbose_name="显示颜色", help_text="1-10代表标签不同颜色，0为默认")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name


class Articles(models.Model):
    title = models.CharField(max_length=120, verbose_name='标题')
    label = models.ManyToManyField('ArticleLabel', related_name='tag', verbose_name='标签')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')
    modify_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    click_num = models.IntegerField(default=0, verbose_name='访问次数')
    content = UEditorField(imagePath="blog/images/", width=1000, height=600,
                           filePath="blog/files/", default='', verbose_name="内容")
    front_image = models.ImageField(upload_to="blog/images/", null=True, blank=True, verbose_name="封面图", help_text='图片尺寸：295 x 230')
    top_image = models.ImageField(upload_to="blog/images/", null=True, blank=True, verbose_name="顶部图", help_text='图片尺寸：750 x 415')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '文章管理'
        verbose_name_plural = verbose_name
