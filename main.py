import requests
import json

url = 'https://www.cbr-xml-daily.ru/daily_json.js'
response_1 = requests.get(url)
print(response_1)