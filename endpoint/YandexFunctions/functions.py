from .model import GeoObject
from string import Template
from typing import overload
import re as regex
import urllib.request, json 

class YandexEndPoint:

    """
    This class will make request to Yandex Geocoder API.
    *With*
    Request Format:
        https://geocode-maps.yandex.ru/1.x
         ? geocode=<string>
         & apikey=<string>
         & [sco=<string>]
         & [kind=<string>]
         & [rspn=<boolean>]
         & [ll=<number>, <number>]
         & [spn=<number>, <number>]
         & [bbox=<number>,<number>~<number>,<number>]
         & [format=<string>]
         & [skip=<integer>]
         & [lang=<string>]
         & [callback=<string>]
    """
    
    def __init__(self, apikey:str) -> None:
        self._geocode = None
        self._kind = None
        self._rspn = None
        self._header_tamplate = Template(
        f"""
        https://geocode-maps.yandex.ru/1.x/
        ?apikey={apikey}
        &format=json
        $body
        &lang=en-US
        """.replace("\n", "").replace(" ", "")
        )
        self._body_tamplate = Template(
            """
            &geocode=$geocode
            &kind=$kind
            &rspn=$rspn
            """
        )
        pass

    # @staticmethod
    def _get_body(self)-> str:
        """
        this function cleans unused body parameters:
        Example: 
        for provided tamplate string:
            &kind=None <- Not used
            &rspn=$rspn <- Value not provided
            &lang=en-US <- Value provided and used
        
        the function will drop every parameters except 'lang'
        """
        url_body = ""
        body_template = str(self._body_tamplate.safe_substitute(
            geocode = self._geocode,
            kind = self._kind,
            rspn = self._rspn
        ))
        print(body_template)
        for line in body_template.split("\n"):
            is_not_used = regex.findall(r"=None$", line) 
            if is_not_used != []:
                # delete
                continue
                pass
            else:
                url_body += line.strip()
            pass

        return url_body

    @property
    def geocode(self):
        return self._geocode

    @geocode.setter
    def geocode(self, value):
        self._geocode = value.replace(" ", "+")

    @property
    def url_request(self)->str:
        url = self._header_tamplate.safe_substitute(
            body=self._get_body()
        )
        return url

    def get_dict_data(self)->dict:
        print(self.url_request)
        with urllib.request.urlopen(self.url_request) as url:
            json_data = json.loads(url.read().decode())
            return json_data

    def get_geo_object(self)->GeoObject:

        geo_obj_collection: dict = self.get_dict_data()["response"]["GeoObjectCollection"]
        geo_meta_data: dict = geo_obj_collection["metaDataProperty"]
        #first geo object will be used from featureMember
        geo_object: list = geo_obj_collection["featureMember"][0]["GeoObject"]
        lower_corner = geo_object["boundedBy"]["Envelope"]["lowerCorner"]
        upper_corner = geo_object["boundedBy"]["Envelope"]["upperCorner"]          
        geo_obj = GeoObject(
            data_property=geo_meta_data,
            name=geo_object["name"],
            description= geo_object["description"] if geo_object["description"] is not None else "",
            point= tuple(float(pos) for pos in geo_object["Point"]["pos"].split()),
            lower_corner= tuple(float(pos) for pos in lower_corner.split()),
            upper_corner= tuple(float(pos) for pos in upper_corner.split())
        )
        
        return geo_obj



        