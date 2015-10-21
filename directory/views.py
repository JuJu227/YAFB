from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import User, Employee


def index(request):
    employees = Employee.objects.order_by('start_date')
    template = loader.get_template('directory/index.html')
    context = RequestContext(request, {
        'employees': employees,
    })
    return HttpResponse(template.render(context))