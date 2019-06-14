from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.views import generic
from .models import Article, BigCategory, Category, Tag


class IndexView(generic.ListView):
	"""
		首页视图，继承自listview,用于展示从数据库中获取的文章列表
	"""
	# 获取数据库中的文章列表
	model = Article
	# template_name属性用于指定使用哪个模板进行渲染
	template_name = 'index.html'
	# context_object_name属性用于给上下文变量取名(在模版中使用该名字)
	context_object_name = 'articles'


