import json
import urllib.request

ciudad = "uruguay"

url = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + ciudad + '&appid=e388302d7bbfeb525550c747d087ad8f').read()

# JSON
data_json = json.loads(url)
#print(data_dic)

# DICCIONARIO
data_dic = {
        "CODIGO PAIS": str(data_json['sys']['country']),
        "LONGITUD": str(data_json['coord']['lon']),
        "LATITUD": str(data_json['coord']['lat']),
        "TEMPERATURA": str(data_json['main']['temp']) + 'k',
        "PRESION": str(data_json['main']['pressure']),
        "HUMEDAD": str(data_json['main']['humidity']),
        }

for k,v in data_dic.items():
        print(k,v)