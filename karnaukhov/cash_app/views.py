from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .services import request_course


@api_view(['GET'])
def get_course(request):
    base_currency = request.GET['from']
    target = request.GET['to']
    amount = float(request.GET['value'])

    if amount < 0:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    result = request_course(base_currency=base_currency, target=target, amount=float(amount))

    return Response(result)