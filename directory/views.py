from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import User, Employee, GroupProfile, Type


def index(request):
    employees = Employee.objects.order_by('start_date')
    groups = GroupProfile.objects.order_by('description')
    types = Type.objects.order_by('name')
    template = loader.get_template('directory/index.html')
    context = RequestContext(request, {
        'employees': employees,
        'groups': groups,
        'types': types,
    })
    return HttpResponse(template.render(context))

def employee_detail(request, employee_id):
	employee = Employee.objects.get(pk=employee_id)
	template = loader.get_template('directory/employee.html')
	context = RequestContext(request, {
        'employee': employee,
    })

	return HttpResponse(template.render(context))

def group_detail(request, group_id):
	group = GroupProfile.objects.get(pk=group_id)
	template = loader.get_template('directory/group.html')
	context = RequestContext(request, {
        'group': group,
    })
	
	return HttpResponse(template.render(context))

def type_list(request, type_id):
	groups = GroupProfile.objects.filter(type=type_id)
	template = loader.get_template('directory/type.html')
	context = RequestContext(request, {
        'groups': groups,
    })
	
	return HttpResponse(template.render(context))















