import requests   #run "pip install request" in cmd terminal, then import

city_name="Africa"    #enter city name of your choice
API_Key="c582e36619807e89dc7ef9cf3d9670ab"    #fetched free api from "Openweather"
url=f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_Key}&unit=metric"

response=requests.get(url)
if response.status_code==200:    #just check that whether api is successfully called or notby print("yes, we hit")
    data=response.json()
    print("WEATHER IS: ",data["weather"][0]["description"])       #response will be generatedd in dictionary format
    print("CURRENT TEMPERATURE IS:",data["main"]["temp"])
    print("CURRENT TEMPERATURE FEELS LIKE:",data["main"]["feels_like"])
    print("CURRENT humidity IS",data["main"]["humidity"])
