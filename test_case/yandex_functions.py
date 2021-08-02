from typing import Tuple
from endpoint.YandexFunctions.model import GeoObject
from static.apikey import get_api_key
from endpoint.YandexFunctions.functions import YandexEndPoint
import unittest

yandex_endpoint =  YandexEndPoint(apikey=get_api_key())
address = "Moscow Ring Road"
yandex_endpoint.geocode = address
class TestYandexFunctions(unittest.TestCase):

    def _check_body(self):

        url_body = yandex_endpoint._get_body().split("/")

        url_endpoint = url_body[0]
        url_commands = url_body[1]
        url_place_address = url_body[2]

        pass

    def check_geo_object(self):

        geo_obj = yandex_endpoint.get_geo_object()
        self.assertTrue(isinstance(geo_obj, GeoObject))
        self.assertTrue(isinstance(geo_obj.point, Tuple))
        self.assertTrue(isinstance(geo_obj.lower_corner, Tuple))
        self.assertTrue(isinstance(geo_obj.upper_corner, Tuple))
        pass

