import json
import urllib.request

ciudad = "uruguay"

url = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + ciudad + '&appid=e388302d7bbfeb525550c747d087ad8f').read()

# JSON A DICCIONARIO
data_dic = json.loads(url)

#print(data_dic)

data = {
        "CODIGO PAIS": str(data_dic['sys']['country']),
        "LONGITUD": str(data_dic['coord']['lon']),
        "LATITUD": str(data_dic['coord']['lat']),
        "TEMPERATURA": str(data_dic['main']['temp']) + 'k',
        "PRESION": str(data_dic['main']['pressure']),
        "HUMEDAD": str(data_dic['main']['humidity']),
        }

print(data)