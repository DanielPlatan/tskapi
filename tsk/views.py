from tsk.parser import parse

from django.http import HttpResponse
def index(request):
    parse()
    return HttpResponse("Parsing is OK, done")