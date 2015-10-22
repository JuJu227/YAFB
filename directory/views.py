from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader

from .models import User, Employee, GroupProfile, Type, Office, Message


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
	groups = GroupProfile.objects.filter(employee=employee_id)
	template = loader.get_template('directory/employee.html')
	navinfo = nav()
	context = RequestContext(request, {
        'employee': employee,
        'groups': groups,
        'navinfo': navinfo,
    })

	return HttpResponse(template.render(context))

def group_detail(request, group_id):
	group = GroupProfile.objects.get(pk=group_id)
	employees = Employee.objects.filter(groups=group_id)
	header = "Group: %s" % group
	template = loader.get_template('directory/group.html')
	navinfo = nav()
	context = RequestContext(request, {
        'group': group,
        'employees': employees,
        'header': header,
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

def news_feed(request, employee_id):
    employee = Employee.objects.get(pk=employee_id)
    messages = Message.objects.filter(writer=employee_id).order_by('-time_stamp')

    template = loader.get_template('directory/message.html')
    context = RequestContext(request, {
        'employee': employee,
        'newsfeed': messages,
    })

    return HttpResponse(template.render(context))

def post_news_feed(request, employee_id):
    employee = Employee.objects.get(pk=employee_id)

    if employee:
        message = Message(writer=employee, text=request.POST.get("content", ""))
        message.save()
        print "New message %s" % message.text

    return HttpResponseRedirect("..")
