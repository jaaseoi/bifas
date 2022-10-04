from django.http import HttpResponse
from django.http import JsonResponse

def index(request):
    return HttpResponse("index")

import datetime
def ping(request):
    return HttpResponse("Pong {}".format(datetime.datetime.now()))

# -------------------------------- Mempool --------------------------------
from .crud.mempool import index_page as mempool_index
def mempool_index_page(request):
    return mempool_index(request)

from .crud.mempool import create_mempool
from bifas.utils.data_structure.binary import Binary
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def mempool_post(request):
    if request.method =="POST":
        return HttpResponse(
            create_mempool(
                token_id=Binary(str(request.POST.get("token_id", None)), data_format="base64"),
                operator=str(request.POST.get("operator", None)),
                amount=float(request.POST.get("amount", -1)),
                address=Binary(str(request.POST.get("address", None)), data_format="base64"),
                bounty=float(request.POST.get("bounty", -1)),
                deadline=int(request.POST.get("deadline", -1)),
                digital_signature=Binary(str(request.POST.get("digital_signature", None)), data_format="base64"),
            )
        )
    else:
        return HttpResponse(False)

from .crud.mempool import read_mempool
def mempool_get(request):
    return JsonResponse(
        data=read_mempool(),
        safe=False,
    )