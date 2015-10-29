from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader

from .models import User, Employee, GroupProfile, Type, Office, Message


def nav(request):
    types = Type.objects.order_by('name')
    offices = Office.objects.order_by('name')
    template = loader.get_template('base.html')
    navinfo = {
        'types': types,
        'offices': offices,
        'user_name': request.COOKIES.get("user_name"),
        'user_id': request.COOKIES.get("user_id"),
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

    if employee:
        redirect = HttpResponseRedirect("/directory");
        redirect.set_cookie("login_user", True)
        redirect.set_cookie("user_id", employee[0].id)
        redirect.set_cookie("user_name", employee[0].full_name)

        return redirect

    return HttpResponseRedirect("/login")


def signout(request):
    redirect = HttpResponseRedirect("/login")
    redirect.delete_cookie("login_user")
    redirect.delete_cookie("user_id")
    redirect.delete_cookie("user_name")

    return redirect


def index(request):
    if not __login__(request):
        return HttpResponseRedirect("/login")

    employees = Employee.objects.order_by('full_name')
    groups = GroupProfile.objects.order_by('group')
    template = loader.get_template('directory/index.html')
    navinfo = nav(request)

    context = RequestContext(request, {
        'employees': employees,
        'groups': groups,
        'header': "Directory",
        'navinfo': navinfo,
    })

    return HttpResponse(template.render(context))


def employee_detail(request, employee_id):
    if not __login__(request):
        return HttpResponseRedirect("/login")

    employee = Employee.objects.get(pk=employee_id)
    groups = GroupProfile.objects.filter(employee=employee_id)
    reports = Employee.objects.filter(manager=employee_id)
    template = loader.get_template('directory/employee.html')
    navinfo = nav(request)
    context = RequestContext(request, {
        'employee': employee,
        'groups': groups,
        'reports': reports,
        'navinfo': navinfo,
    })

    return HttpResponse(template.render(context))


def group_detail(request, group_id):
    if not __login__(request):
        return HttpResponseRedirect("/login")

    group = GroupProfile.objects.get(pk=group_id)
    employees = Employee.objects.filter(groups=group_id)
    header = "Group: %s" % group
    template = loader.get_template('directory/group.html')
    navinfo = nav(request)
    context = RequestContext(request, {
        'group': group,
        'employees': employees,
        'header': header,
        'navinfo': navinfo,
    })

    return HttpResponse(template.render(context))


def office_detail(request, office_id):
    if not __login__(request):
        return HttpResponseRedirect("/login")

    office = Office.objects.get(pk=office_id)
    employees = Employee.objects.filter(office=office_id)
    header = "Office: %s" % office
    template = loader.get_template('directory/group.html')
    navinfo = nav(request)
    context = RequestContext(request, {
        'office': office,
        'employees': employees,
        'header': header,
        'navinfo': navinfo,
    })

    return HttpResponse(template.render(context))


def type_list(request, type_id):
    if not __login__(request):
        return HttpResponseRedirect("/login")

    groups = GroupProfile.objects.filter(type=type_id)
    type = Type.objects.get(pk=type_id)
    header = "Groups of type: %s" % type
    template = loader.get_template('directory/type.html')
    navinfo = nav(request)
    context = RequestContext(request, {
        'groups': groups,
        'header': header,
        'navinfo': navinfo,
    })

    return HttpResponse(template.render(context))


def news_feed(request):
    if not __login__(request):
        return HttpResponseRedirect("/login")

    messages = Message.objects.order_by('-time_stamp')
    newsfeed = []
    navinfo = nav(request)

    for message in messages:
        employee = Employee.objects.get(pk=message.writer_id)

        if employee:
            feed = dict(writer_id=employee.id, writer_full_name=employee.full_name,
                        time_stamp=message.time_stamp, text=message.text)
            newsfeed.append(feed)

    template = loader.get_template('directory/news_item.html')
    context = RequestContext(request, {
        'newsfeed': newsfeed,
        'navinfo': navinfo,
    })

    return HttpResponse(template.render(context))


def post_item(request):
    if not __login__(request):
        return HttpResponseRedirect("/login")

    employee_id = request.COOKIES.get("user_id")
    employee = Employee.objects.get(pk=employee_id)

    message = Message(writer=employee, text=request.POST.get("content", ""))
    message.save(request)
    print "New message %s" % message.text

    return HttpResponseRedirect("..")


def news_feed_by_employee(request, employee_id):
    if not __login__(request):
        return HttpResponseRedirect("/login")

    employee = Employee.objects.get(pk=employee_id)
    messages = Message.objects.filter(writer=employee_id).order_by('-time_stamp')

    template = loader.get_template('directory/message.html')
    context = RequestContext(request, {
        'employee': employee,
        'newsfeed': messages,
    })

    return HttpResponse(template.render(context))


def post_news_feed(request, employee_id):
    if not __login__(request):
        return HttpResponseRedirect("/login")

    employee_id = request.COOKIES.get("user_id")
    employee = Employee.objects.get(pk=employee_id)

    if employee:
        message = Message(writer=employee, text=request.POST.get("content", ""))
        message.save()
        print "New message %s" % message.text

    return HttpResponseRedirect("..")


def __login__(request):
    login_user = request.COOKIES.get("login_user")

    if not login_user:
        return False

    return True

