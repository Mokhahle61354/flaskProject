import json
  
def get_api_key():

    f = open('static/ApiKeys.json',)
    api_keys = json.load(f)
    yandex_key = api_keys["yandex"]
    return yandex_key