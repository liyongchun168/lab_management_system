from django import template
from ..models import Project,User,ProApprove
register = template.Library()

@register.filter
def status(p, u):
    pro = ProApprove.objects.filter(user=u, project=p).first()
    return pro.status

@register.filter
def have_user(p,u):
    pro = ProApprove.objects.filter(user=u,project=p)
    return True if pro else False
