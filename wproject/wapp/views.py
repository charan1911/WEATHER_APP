from django.shortcuts import render
import json
import urllib.request
import datetime
'''error_message ='not found'
                #print(error_message)
                #return render(request, 'home.html', {'error_message': error_message})
''''''


import json
def weather(request):
    if 'location' in request.GET:
        city = request.GET.get('location')
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid= your api here"
        # demonstrate how to use the 'params' parameter:
        x = requests.get(url)
        #Converts response object to dictionary
        y = x.json()
        context = {
            'c_name' : f"City_name:{y['name']}",
            'Temperature': f"Temperature: {y['main']['temp']} F",
            'Pressure': f"Pressure: {y['main']['pressure']}",
            'Humidity': f"Humidity: {y['main']['humidity']}",
            'Weather_condition': f"Weather_Condition: {y['weather'][0]['description'].upper()}"
        }

        return render(request, 'home.html', context)
    return render(request, 'home.html')
'''

def homefn(request):
    if request.method == 'POST':
        import urllib.request
        import json
        key = 'e24c9d176a5eb4a5a6ac74c02748b044'
        city = request.POST["city"].replace(" ", "+")
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"

        try:
            source = urllib.request.urlopen(url).read()
            data = json.loads(source)

            if data.get("cod") == 200:
                # Valid location
                unix_timestamp = data['dt']
                formatted_date = datetime.datetime.fromtimestamp(unix_timestamp).strftime('%Y-%m-%d %H:%M:%S')
                return render(request, 'home.html', {'data': data['main'], 'city': request.POST['city'], 'date':formatted_date})
                '''
                else:
                    # Invalid location
                    if not request.POST['city']:
                        # User didn't enter a city name
                        error_message = "Please enter a city name."
                    else:
                        # User entered a city name, but it's not valid
                        error_message = f"{request.POST['city']} is not found."
                        # Invalid location
                        error_message = f"{city} is not found !!"
                        print(error_message)
                        return render(request, 'home.html', {'error_message': error_message})
                        '''
        except urllib.error.HTTPError as e:
            # Handle HTTP errors (e.g., 404)
            #error_message = f"HTTP Error: {e.code} - {e.reason}"
            error_message = "YOU HAVE ENTERED INVALID NAME !!"
            print(error_message)
            return render(request, 'home.html', {'error_message': error_message})
        except urllib.error.URLError as e:
            # Handle network errors
            error_message = f"Network Error: {str(e)}"
            print(error_message)
            return render(request, 'home.html', {'error_message': error_message})
    else:
        return render(request, 'home.html')

    '''if request.method=='POST':
        import urllib.request
        import json
        key='e24c9d176a5eb4a5a6ac74c02748b044'
        source=urllib.request.urlopen("http://api.openweathermap.org/data/2.5/weather?q="+request.POST["city"].replace(" ","+")+"&appid="+key).read()
        data=json.loads(source)
        print(data)
        if data.get("cod") == 200:
            # Valid location
            return render(request, 'home.html', {'data': data['main'], 'city': request.POST['city'], 'date': data['dt']})
        else:
            # Invalid location
            error_message = 'error'
            print(error_message)
            return render(request, 'home.html', {'error_message': error_message})
            #return render(request,'home.html',{'data':data['main'],'city':request.POST['city'],'date':data['dt']})

    else:
        return render(request,'home.html')'''
