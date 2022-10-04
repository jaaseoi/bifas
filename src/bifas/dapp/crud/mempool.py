from bifas.utils.data_structure.binary import Binary
from bifas.utils.data_structure.date_time import datetime_add_microsecond_time_delta
import datetime
from ..CONSTANTS import LIST_OF_OPERATORS
from django.core.serializers import serialize
from dapp.models import Mempool
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import render
from rest_framework import serializers
import typing

def index_page(
    request,
    *args,
    **kwargs,
) -> HttpResponse:
    return render(
        request=request,
        template_name="mempool/index.html",
        context={},
    )

def paginator(page_number, per_page):
    contact_list = Mempool.objects.all()
    paginator = Paginator(
        object_list=contact_list,
        per_page=per_page,
    )
    page_obj = paginator.get_page(
        number=page_number,
    )
    return page_obj

def create_mempool(
    token_id:Binary=None,
    operator:str=None,
    amount:float=None,
    address:Binary=None,
    bounty:float=None,
    time_to_live:int=None,               # in microseconds
) -> bool:
    kwargs = {}
    if ((token_id == None) and (type(token_id)==Binary)):
        return False
    else:
        kwargs["token_id"] = token_id.get_x(data_format="base64")

    if ((operator == None) and (type(operator)==str)):
        return False
    elif(operator not in LIST_OF_OPERATORS):
        # Invalid operator.
        return False
    else:
        kwargs["operator"] = operator

    if ((amount == None) and (type(amount)==float)):
        return False
    elif (amount <= 0):
        # Amount non positive number.
        return False
    else:
        kwargs["amount"] = amount

    if ((address == None) and (type(address)==Binary)):
        return False
    else:
        kwargs["address"] = address.get_x(data_format="base64")
    if ((bounty == None) and (type(bounty)==float)):
        return False
    elif (bounty <= 0):
        # Amount non positive number.
        return False
    else:
        kwargs["bounty"] = bounty

    if ((time_to_live == None) and (type(time_to_live)==int)):
        return False
    elif (time_to_live <= 0):
        # Time To Live non positive number.
        return False
    else:
        kwargs["time_to_live"] = datetime_add_microsecond_time_delta(
            x=datetime.datetime.now(),
            delta=time_to_live,
        )

    Mempool(**kwargs).save()
    return True

def read_mempool() -> list:
    return list(Mempool.objects.values())