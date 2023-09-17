import json
import requests
from django.conf import settings
import currencyapicom


def request_course(base_currency: str, target: str, amount: float):
    client = currencyapicom.Client(settings.API_KEY)
    result = client.convert(base_currency=base_currency, currencies=[target], value=amount)

    return result
