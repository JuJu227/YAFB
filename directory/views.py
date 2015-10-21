from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import User, Employee, GroupProfile


def index(request):
    employees = Employee.objects.order_by('start_date')
    groups = GroupProfile.objects.order_by('description')
    template = loader.get_template('directory/index.html')
    context = RequestContext(request, {
        'employees': employees,
        'groups': groups,
    })
    return HttpResponse(template.render(context))