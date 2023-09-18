from rest_framework.decorators import api_view
from rest_framework.response import Response

from .services import request_course


@api_view(['GET'])
def get_course(request):
    base_currency = request.GET['from']
    target = request.GET['to']
    amount = request.GET['value']

    result = request_course(base_currency=base_currency, target=target, amount=float(amount))

    return Response(result)