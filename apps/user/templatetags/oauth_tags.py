from django import template
from ..models import Ouser


register = template.Library()

@register.simple_tag
def get_user_data(uid):
	"""返回用户信息"""
	user = Ouser.objects.filter(id=uid)
	if user:
		return user[0]
	else:
		return ''