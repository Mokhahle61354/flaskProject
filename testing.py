from string import Template
from typing import overload
import re as regex


class YandexEndPoint:

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
    def _get_body(self):
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
            print(is_not_used) 
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
    def url_request(self):
        url = self._header_tamplate.safe_substitute(
            body=self._get_body()
        )
        return url



class YandexGeoObj(YandexEndPoint):
    def __init__(self, apikey: str, geocode="") -> None:
        super().__init__(apikey)
        self.geocode = geocode
        pass

    def get_coordinates(self):
        pass
    def get_name(self):
        pass
    def get_discription(self):
        pass

    def get_boundries(self):
        pass




apikey="951d37f3-1b9f-424f-8768-2ae5f3852535"

yandex_endpoint = YandexEndPoint(apikey=apikey)

yandex_endpoint.geocode = "Moscow Ring Road"

print(yandex_endpoint.url_request)

