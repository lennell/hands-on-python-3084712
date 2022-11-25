import requests
from pprint import pprint

response = requests.get(
    "http://api.worldbank.org/v2/countries/SE/indicators/SP.POP.TOTL?per_page=5000&format=json")

last_twenty_years = response.json()[1][:20]

for year in last_twenty_years:
    print(year["date"] + " " * year["value"])
