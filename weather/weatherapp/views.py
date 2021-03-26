from django.shortcuts import render

# Create your views here.
import urllib.request
import json


def index(request):
    if request.method == "POST":
        city = request.POST['city']
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city +
                                        '&units=metric&appid=0961d45cbc2cd817d7db50cbf5a67e2f').read()
        lis_of_data = json.loads(source)
        data = {
            "country_code": str(lis_of_data['sys']['country']),
            "coordinate": str(lis_of_data['coord']['lon']) + ',' + str(lis_of_data['coord']['lat']),
            "temp": str(lis_of_data['main']['temp']) + '°C',
            "pressure": str(lis_of_data['main']['pressure']),
            "humidity": str(lis_of_data['main']['humidity']),
            "main": str(lis_of_data['weather'][0]['main']),
            "description" : str(lis_of_data['weather'][0]['description']),
            "icon": lis_of_data['weather'][0]['icon']
        }
        print(data)
    else:
        data = {}
    return render(request, "index.html",data)



