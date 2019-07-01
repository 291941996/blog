from django.conf.urls import url
from .views import IndexView

urlpatterns = [
	url(r'^$', IndexView.as_view(template_name='index.html'), name='index'),
	url(r'^category/(?P<bigslug>.*?)/(?P<slug>.*?)', IndexView.as_view(template_name='content.html'), name='category'),
]
