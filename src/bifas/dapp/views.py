from django.http import HttpResponse
from django.http import JsonResponse

def index(request):
    return HttpResponse("index")

import datetime
def ping(request):
    return HttpResponse("Pong {}".format(datetime.datetime.now()))