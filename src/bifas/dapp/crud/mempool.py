from bifas.utils.data_structure.binary import Binary
from ..CONSTANTS import LIST_OF_OPERATORS
from dapp.models import Mempool
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import render
import time
import math

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
    deadline:int=None,
    digital_signature:Binary=None,
) -> bool:
    """
    Boolean function to create record for Mempool.

    Validation :
    * operator must be in the set of LIST_OF_OPERATORS.
    * amount must be positive float.
    * bounty must be non-negative float.
    * deadline must be either 0 or positive integer >= int(current Unix Timestamp)

    Parameters
    ----------
    token_id : bifas.utils.data_structure.binary.Binary, default None
    operator : str, default None
    amount : float, default None
    address : bifas.utils.data_structure.binary.Binary, default None
    bounty : float, default None
    deadline : int, default None
    digital_signature : bifas.utils.data_structure.binary.Binary, default None

    Returns
    -------
    bool
    """
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
        # amountt non positive number.
        return False
    elif (amount < bounty):
        return False
    else:
        kwargs["bounty"] = bounty

    if ((deadline == None) and (type(deadline)==int)):
        return False
    elif (deadline < 0):
        # deadline negative number.
        return False
    elif (deadline != 0) and (deadline <= math.floor(time.time())):
        # Neither empty nor after current unix time
        return False
    else:
        kwargs["deadline"] = deadline

    if ((digital_signature == None) and (type(digital_signature)==Binary)):
        return False
    else:
        kwargs["digital_signature"] = digital_signature.get_x(data_format="base64")

    Mempool(**kwargs).save()
    return True

def read_mempool() -> list:
    return list(Mempool.objects.values())