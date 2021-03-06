from django.db import models

from DjangoUeditor.models import UEditorField


class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name="课程类别")

    class Meta:
        verbose_name = u"分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=20, verbose_name="课程标签")

    class Meta:
        verbose_name = u"标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name="课程名字")
    desc = models.CharField(max_length=300, verbose_name="课程描述")
    detail = UEditorField(verbose_name="课程详情", imagePath="courses/image/",
                          filePath="courses/file/", default='')
    degree = models.CharField(verbose_name="难度", choices=(("cj", u"初级"), ("zj", u"中级"), ("gj", u"高级")), max_length=2)
    learn_times = models.IntegerField(default=0, verbose_name="学习长度（分钟数）")
    students = models.IntegerField(default=0, verbose_name="学习人数")
    fav_nums = models.IntegerField(default=0, verbose_name="收藏人数")
    image = models.ImageField(upload_to="courses/%y/%m", null=True, blank=True, verbose_name="封面图", help_text="尺寸：357x233")
    click_nums = models.IntegerField(default=0, verbose_name=u"点击人数")
    category = models.ForeignKey('Category', null=True, blank=True, verbose_name="课程类别")
    tag = models.ManyToManyField('Tag', null=True, blank=True, verbose_name="课程标签")
    youneed_know = models.CharField(default="", max_length=300, verbose_name="课程须知")
    is_hot = models.BooleanField(default=True, verbose_name="热门课程", help_text="用于在首页展示的课程")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    class Meta:
        verbose_name = "课程"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
