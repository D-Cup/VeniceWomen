# -*- coding:utf-8 -*-
import xadmin
from mainApp.models import Tag, Art
from xadmin import views


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = '威尼斯人后台管理系统'
    site_footer = '威尼斯人'
    menu_style = 'accordion'


class TagAdmin:
    # 后台列表显示列
    list_display = ['name', 'modify_time', 'is_top']
    # 后台列表查询条件
    search_fields = ['name']


class ArtAdmin:
    # 后台列表显示列
    list_display = ['title', 'summary', 'content', 'publish_date', 'tag']
    # 后台列表查询条件
    search_fields = ['title', 'summary']
    style_fields = {'content': 'ueditor'}

xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSettings)
xadmin.site.register(Tag, TagAdmin)
xadmin.site.register(Art, ArtAdmin)