# from .static.apikey import get_api_key
# from werkzeug.wrappers import response
from os import read
from .YandexFunctions.functions import YandexEndPoint
from .YandexFunctions.model import ComputeGeoObject, GeoObject
from ..static.apikey import get_api_key
# import moscow_data, yandex_endpoint
from flask import Blueprint
import markdown
# from . import moscow_geo_object, yandex_endpoint

compare_city = Blueprint("compare", __name__)
moscow_endpoint = YandexEndPoint(apikey=get_api_key())
moscow_endpoint.geocode = "Moscow Ring Road"

@compare_city.route("/")
def home_page():
    readme_md = open("README.md", "r").read()
    return markdown.markdown(readme_md)


@compare_city.route("/enclused/<string:address>")
def get_is_enclosed(address)-> bool:
    """
    Returns true if address is bounded in MKAD

    Returns:
        [type]: [description]
    """
    MKAD_endpoint = YandexEndPoint(apikey=get_api_key())
    yandex_endpoint = YandexEndPoint(apikey=get_api_key())
    yandex_endpoint.geocode = address
    MKAD_endpoint.geocode = "Russia, Moscow, MKAD"
    address_geo_object: GeoObject = MKAD_endpoint.get_geo_object()
    compute_obj = ComputeGeoObject(
        reference_city = yandex_endpoint.get_geo_object(),
        selected_city = address_geo_object
    )
    return compute_obj.is_inside_evelope()


@compare_city.route("/info/<string:address>")
def city_description(address)->str:
    yandex_endpoint = YandexEndPoint(apikey=get_api_key())
    # moscow_endpoint = YandexEndPoint(apikey=get_api_key())
    moscow_endpoint.geocode = "Moscow Ring Road"
    tmp_yandex_endpoint = yandex_endpoint
    tmp_yandex_endpoint.geocode = address
    address_geo_object: GeoObject = tmp_yandex_endpoint.get_geo_object()
    print(address_geo_object.description)
    return address_geo_object.description


@compare_city.route("/distance/<string:address>")
def distance_from_moscow(address="CBD Cape Town")->float:
    """
    This method, will calculate distance from "Moscow Ring Road" to provided 'address'

    Args:
        address (str): "name of the selected place"
            - Example: "CBD Cape Town"

    Returns:
        dict : json/dict holding distance infomation about provided address
    """
    yandex_endpoint = YandexEndPoint(apikey=get_api_key())
    tmp_yandex_endpoint = yandex_endpoint
    tmp_yandex_endpoint.geocode = address
    address_geo_object: GeoObject = tmp_yandex_endpoint.get_geo_object()

    distance_obj = ComputeGeoObject(
        reference_city = moscow_endpoint.get_geo_object(),
        selected_city = address_geo_object
    )
    distance_km = distance_obj.get_point_distance()
    envelope_distance = distance_obj.get_envelope_distances()
    distance_km.update(envelope_distance)

    return distance_km

@compare_city.route("/<string:params>/<string:address>")
def get_multiple_params(params:str, address:str) -> dict:
    """
    This method, will return data for provided parameters for given address

    Args:
        params (str): ""parameters to include on results in form of string separated only by 'space'
            - Example: "description +description distance"
            - Hints: everything with '+' as prefix will return info for reference address -> ("Moscow Ring Road")
        address (str): "name of the selected place"
            - Example: "CBD Cape Town"

    Returns:
        dict : json/dict holding infomation about provided parameters
    """
    MKAD_endpoint = YandexEndPoint(apikey=get_api_key())
    moscow_endpoint = YandexEndPoint(apikey=get_api_key())
    ref_city_address = "Moscow Ring Road"
    dict_response = {}
    if 'description' in params:
        dict_response.update({'description':city_description(address=address)})
    if '+description' in params:
        dict_response.update({'+description':city_description(address=ref_city_address)})
    if 'distance' in params:
        dict_response.update({'distance':distance_from_moscow(address=address)})
    if 'enclosed' in params:
        dict_response.update({'enclosed':get_is_enclosed(address=address)})
    else:
        dict_response.update({'description':city_description(address=address)})
        dict_response.update({'distance':distance_from_moscow(address=address)})
        pass

    return dict_response

