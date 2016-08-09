import json
from urllib.request import urlopen

API_URL = "http://weather.livedoor.com/forecast/webservice/json/v1?city=471010"
json_data = ""
with urlopen(API_URL) as response:
    for line in response:
        line = line.decode("UTF-8")
        json_data += line


weather = json.loads(json_data)
print("weather of (Naha)")
print("{0}very hot: {1}degree".format(weather['forecasts'][0]['telop'],
                           weather['forecasts'][0]['temperature']['max']['celsius']))
print()

from pprint import pprint
pprint(weather)

