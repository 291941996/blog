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


def AboutView(request):
	return render(request, 'about.html', {'category': 'about'})

def MessageView(request):
	return render(request, 'message.html', {'category': 'message'})

def LinkView(request):
	return render(request, 'link.html')


def DonateView(request):
	return render(request, 'donate.html', {'category': 'donate'})


def ExchangeView(request):
	return render(request, 'exchange.html', {'category': 'exchange'})


def ProjectView(request):
	return render(request, 'project.html', {'category': 'project'})


def QuestionView(request):
	return render(request, 'question.html', {'category': 'question'})



