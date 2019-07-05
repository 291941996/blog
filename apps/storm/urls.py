from django.conf.urls import url
from .views import (IndexView, AboutView, MessageView, DonateView, ExchangeView, ProjectView,
					QuestionView, LinkView, DetailView)

urlpatterns = [
	# 首页
	url(r'^$', IndexView.as_view(template_name='index.html'), name='index'),  # 主页，自然排序
	url(r'^category/about/$', AboutView, name='about'),  # 给我留言
	url(r'^category/message/$', MessageView, name='message'),  # 关于自己
	url(r'^category/donate/$', DonateView, name='donate'),  # 赞助作者
	url(r'^category/exchange/$', ExchangeView, name='exchange'),  # 技术交流
	url(r'^category/project/$', ProjectView, name='project'),  # 项目合作
	url(r'^category/question/$', QuestionView, name='question'),  # 提问交流
	url(r'^link/$', LinkView, name='link'),  # 申请友情链接
	# 大分类页面
	url(r'^category/(?P<bigslug>.*?)/(?P<slug>.*?)', IndexView.as_view(template_name='content.html'), name='category'),
	# 标签页面
	url(r'^tag/(?P<tag>.*?)/$', IndexView.as_view(template_name='content.html'), name='tag'),
	# 归档页面
	url(r'^date/(?P<year>\d+)/(?P<month>\d+)/$', IndexView.as_view(template_name='archive.html'), name='date'),
	# 文章详情页面
	url(r'^article/(?P<slug>.*?)/$', DetailView.as_view(), name='article'),
]
