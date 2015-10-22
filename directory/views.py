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

def login(request):
    template = loader.get_template('login.html')
    context = RequestContext(request, {})

    return HttpResponse(template.render(context))

def signup(request):
    employee = Employee()
    employee.email = request.POST.get("email")
    employee.full_name = request.POST.get("username")
    employee.title = request.POST.get("title")
    email = "{email}".format(email=employee.email)

    user = User.objects.filter(email=email.lower())

    if user:
        employee.user = user
        employee.save()
        return HttpResponseRedirect("/directory")

    return HttpResponseRedirect("/login")

def signin(request):
    email = "{username}".format(username=request.POST.get("username"))
    password = "{password}".format(password=request.POST.get("password"))
    employee = Employee.objects.filter(email=email.lower(), password=password)

    print "Sign-in : %s %s --- %s" % (email, password, employee)

    if employee:
        return HttpResponseRedirect("/directory")

    return HttpResponseRedirect("/login")

def index(request):
    employees = Employee.objects.order_by('full_name')
    groups = GroupProfile.objects.order_by('group')
    template = loader.get_template('directory/index.html')
    navinfo = nav()
    context = RequestContext(request, {
        'employees': employees,
        'groups': groups,
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

def office_detail(request, office_id):
	office = Office.objects.get(pk=office_id)
	employees = Employee.objects.filter(office=office_id)
	header = "Office: %s" % office
	template = loader.get_template('directory/group.html')
	navinfo = nav()
	context = RequestContext(request, {
        'office': office,
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

def news_feed(request):
    messages = Message.objects.order_by('-time_stamp')
    navinfo = nav()
    template = loader.get_template('directory/news_item.html')
    context = RequestContext(request, {
        'newsfeed': messages,
        'navinfo': navinfo,
    })

    return HttpResponse(template.render(context))

def post_item(request):
	# TODO: change employee to signed in user
    employee = Employee.objects.get(pk=2)

    message = Message(writer=employee, text=request.POST.get("content", ""))
    message.save()
    print "New message %s" % message.text

    return HttpResponseRedirect("..")


def news_feed_by_empoyee(request, employee_id):
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
