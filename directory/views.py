from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import User, Employee, GroupProfile, Type, Office


def nav():
    types = Type.objects.order_by('name')
    offices = Office.objects.order_by('name')
    template = loader.get_template('base.html')
    navinfo = {
        'types': types,
        'offices': offices,
    }
    return navinfo

def index(request):
    employees = Employee.objects.order_by('start_date')
    groups = GroupProfile.objects.order_by('description')
    types = Type.objects.order_by('name')
    offices = Office.objects.order_by('name')
    template = loader.get_template('directory/index.html')
    navinfo = nav()
    context = RequestContext(request, {
        'employees': employees,
        'groups': groups,
        'types': types,
        'offices': offices,
        'header': "Directory",
        'navinfo': navinfo,
    })
    return HttpResponse(template.render(context))

def employee_detail(request, employee_id):
	employee = Employee.objects.get(pk=employee_id)
	template = loader.get_template('directory/employee.html')
	navinfo = nav()
	context = RequestContext(request, {
        'employee': employee,
        'navinfo': navinfo,
    })

	return HttpResponse(template.render(context))

def group_detail(request, group_id):
	group = GroupProfile.objects.get(pk=group_id)
	template = loader.get_template('directory/group.html')
	navinfo = nav()
	context = RequestContext(request, {
        'group': group,
        'navinfo': navinfo,
    })
	
	return HttpResponse(template.render(context))

def type_list(request, type_id):
	groups = GroupProfile.objects.filter(type=type_id)
	type = Type.objects.get(pk=type_id)
	header = "Groups of type: %s" % type
	template = loader.get_template('directory/type.html')
	navinfo = nav()
	context = RequestContext(request, {
        'groups': groups,
        'header': header,
        'navinfo': navinfo,
    })
	
	return HttpResponse(template.render(context))















