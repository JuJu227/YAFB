from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import User


def index(request):
    users = User.objects.order_by('username')
    template = loader.get_template('directory/index.html')
    context = RequestContext(request, {
        'users': users,
    })
    return HttpResponse(template.render(context))