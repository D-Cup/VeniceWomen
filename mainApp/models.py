from DjangoUeditor.models import UEditorField
from django.db import models

# Create your models here.

# class Tag(models.Model):


# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name='标签名')
    modify_time = models.DateTimeField(auto_now=True,
                                       verbose_name='最后修改')

    is_top = models.BooleanField(default=True,
                                 verbose_name='是否置顶')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '标签分类'
        db_table = 't_tag'
        verbose_name_plural = verbose_name


class Art(models.Model):
    title = models.CharField(max_length=100,
                             verbose_name='标题')
    summary = models.TextField(verbose_name='简介')
    content = UEditorField(verbose_name='内容',width=800,height=600,imagePath='atrs_ups/ueditor/',filePath='arts_ups/ueditor/',blank=True,toolbars='full',default='')
    publish_date = models.DateTimeField(auto_now_add=True,
                                        blank=True,  # 是否可以为 空
                                        null=True,
                                        verbose_name='发布时间')

    tag = models.ForeignKey(Tag,
                            on_delete=models.SET_NULL,
                            null=True,
                            verbose_name='标签')

    class Meta:
        db_table = 't_art'
        verbose_name = '文章'
        verbose_name_plural = verbose_name

