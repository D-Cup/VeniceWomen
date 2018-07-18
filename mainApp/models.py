from DjangoUeditor.models import UEditorField
from django.db import models

# Create your models here.

# class Tag(models.Model):


# Create your models here.
# class Tag(models.Model):
#     name = models.CharField(max_length=50,
#                             verbose_name='标签名')
#     modify_time = models.DateTimeField(auto_now=True,
#                                        verbose_name='最后修改')
#
#     is_top = models.BooleanField(default=True,
#                                  verbose_name='是否置顶')
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = '标签分类'
#         db_table = 't_tag'
#         verbose_name_plural = verbose_name
#
#
# class Art(models.Model):
#     title = models.CharField(max_length=100,
#                              verbose_name='标题')
#     summary = models.TextField(verbose_name='简介')
#     content = UEditorField(verbose_name='内容',width=800,height=600,imagePath='atrs_ups/ueditor/',filePath='arts_ups/ueditor/',blank=True,toolbars='full',default='')
#     publish_date = models.DateTimeField(auto_now_add=True,
#                                         blank=True,  # 是否可以为 空
#                                         null=True,
#                                         verbose_name='发布时间')
#
#     tag = models.ForeignKey(Tag,
#                             on_delete=models.SET_NULL,
#                             null=True,
#                             verbose_name='标签')
#
#     class Meta:
#         db_table = 't_art'
#         verbose_name = '文章'
#         verbose_name_plural = verbose_name

class User(models.Model):
    userName = models.CharField(max_length=20, unique=True)  # 用户账户，设置唯一
    userPasswd = models.CharField(max_length=32)  # 密码
    phone = models.CharField(max_length=12,default="",null=True)  # 联系方式
    email= models.CharField(max_length=50, verbose_name='邮箱', null=True,default='')
    imgPath = models.ImageField(upload_to='static/uploads',max_length=500,default='',null=True)  # 头像图片路径
    state = models.BooleanField(default=True, verbose_name='用户状态')

    def delete(self, using=None, keep_parents=False):
        self.state = False
        self.save()
        return 'Success'

    class Meta:
        db_table = 'weomen_user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name
