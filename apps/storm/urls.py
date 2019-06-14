from django.conf.urls import url
from .views import IndexView

urlpatterns = [
	url(r'^$', IndexView.as_view(template_name='index.html'), name='index'),
]
