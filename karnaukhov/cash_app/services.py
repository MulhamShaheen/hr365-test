from django.conf import settings
import currencyapicom


def request_course(base_currency: str, target: str, amount: float):
    client = currencyapicom.Client(settings.API_KEY)
    rates = client.latest()['data']

    value_in_usd = amount / rates[base_currency]["value"]
    output_value = value_in_usd * rates[target]["value"]

    response = {
        "result": output_value
    }

    return response
