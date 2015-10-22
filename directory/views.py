from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import User, Employee, GroupProfile, Type, Message


def index(request):
    employees = Employee.objects.order_by('start_date')
    groups = GroupProfile.objects.order_by('description')
    types = Type.objects.order_by('name')
    template = loader.get_template('directory/index.html')
    context = RequestContext(request, {
        'employees': employees,
        'groups': groups,
        'types': types,
        'header': "Directory",
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
	type = Type.objects.get(pk=type_id)
	header = "Groups of type: %s" % type
	template = loader.get_template('directory/type.html')
	context = RequestContext(request, {
        'groups': groups,
        'header': header,
    })

	return HttpResponse(template.render(context))

def news_feed(request, employee_id):
    employee = Employee.objects.get(pk=employee_id)
    messages = Message.objects.filter(writer=employee_id).order_by('-time_stamp')

    template = loader.get_template('directory/message.html')
    context = RequestContext(request, {
        'employee': employee,
        'newsfeed': messages,
    })

    return HttpResponse(template.render(context))

