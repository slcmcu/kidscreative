from django.db import models


class FirmInfo(models.Model):
    """
    公司信息
    """
    comName = models.CharField(max_length=50, verbose_name="公司名称")
    telephone = models.CharField(max_length=15, null=True, blank=True, verbose_name="联系电话")
    email = models.EmailField(null=True, blank=True, verbose_name="电子邮件")
    address = models.CharField(max_length=50, null=True, blank=True, verbose_name="通信地址")
    qqNumber = models.IntegerField(null=True, blank=True, verbose_name="咨询QQ")
    comSlogan = models.CharField(null=True, blank=True, max_length=100, verbose_name="公司标语")

    def __str__(self):
        return self.comName

    class Meta:
        verbose_name = "公司信息"
        verbose_name_plural = verbose_name


class Menu(models.Model):
    """
    导航菜单
    """
    menuName = models.CharField(max_length=32, unique=True, verbose_name="菜单名")
    parent = models.ForeignKey("self", null=True, blank=True, verbose_name="父菜单")
    status = models.BooleanField(default=True, verbose_name="状态")
    quickLink = models.BooleanField(default=False, verbose_name="底部快速导航")
    icon = models.CharField(max_length=50, null=True, blank=True, verbose_name="图标")
    code = models.CharField(max_length=50, null=True, blank=True, verbose_name="编码")
    url = models.CharField(max_length=128, unique=True, null=True, blank=True)
    sortNumber = models.IntegerField(default=0, null=True, blank=True, verbose_name="显示顺序", help_text="按照数字排序，0优先级最高")

    class Meta:
        verbose_name = "导航菜单"
        verbose_name_plural = verbose_name
        ordering = ['sortNumber']

    def __str__(self):
        menu_list = [self.menuName]
        p = self.parent
        while p:
            menu_list.insert(0, p.menuName)
            p = p.parent
        return '-'.join(menu_list)

