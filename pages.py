from .static.apikey import get_api_key
from .YandexFunctions.functions import YandexEndPoint
from flask import Blueprint
yandex_endpoint = YandexEndPoint(apikey=get_api_key())
mowscow_endpoint = YandexEndPoint(apikey=get_api_key())
mowscow_endpoint.geocode = "Moscow Ring Road"

print(yandex_endpoint.url_request)
compare_city = Blueprint("compare", __name__)

@compare_city.route("/")
def moscow_data():
    return mowscow_endpoint.url_request()

@compare_city.route("/info/<string:address>")
def city_discription(address=None):
    print(address)
    yandex_endpoint.geocode = address
    return f"{yandex_endpoint.url_request}"

