import requests as r
import ssl

import certifi
from urllib.request import urlopen
zip_code = input("Enter zip code")
country_code= input("enter your contry code")
API_key='a5746e182c2c39abaee6e006037d0fb6'
url=f"https://api.openweathermap.org/data/2.5/forecast?zip={zip_code},{country_code}&appid={API_key}"
We = r.get(url)
st=We.status_code()
print(st)
print(We)