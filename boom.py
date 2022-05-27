import json
from pprint import pprint
from django.utils.encoding import smart_str

class Karta:

	def __init__(self, name, kolor, rarity, set):
		self.name = name
		self.kolor = kolor
		self.rarity = rarity
		self.set = set


def json_load_byteified(file_handle):
	return _byteify(
		json.load(file_handle, object_hook=_byteify),
		ignore_dicts=True
	)

def json_loads_byteified(json_text):
	return _byteify(
		json.loads(json_text, object_hook=_byteify),
		ignore_dicts=True
	)

def _byteify(data, ignore_dicts = False):
	# if this is a unicode string, return its string representation
	if isinstance(data, str):
		return data.encode('utf-8')
	# if this is a list of values, return list of byteified values
	if isinstance(data, list):
		return [ _byteify(item, ignore_dicts=True) for item in data ]
	# if this is a dictionary, return dictionary of byteified keys and values
	# but only if we haven't already byteified it
	if isinstance(data, dict) and not ignore_dicts:
		return {
			_byteify(key, ignore_dicts=True): _byteify(value, ignore_dicts=True)
			for key, value in data.items()
		}
	# if it's anything else, return it in its original form
	return data

with open('data.json', encoding="utf8") as data_file:
	data = json_load_byteified(data_file)
lista = []

for i in data:
	for j in i['cards']:
		#pprint(data[keyss[i]]["cards"][j])
		#pprint("\n")
		if not j["colors"]:
			karta = Karta(j["name"], "", j["rarity"], i["name"])
		else:
			karta = Karta(j["name"], j["colors"], j["rarity"], i["name"])
		lista.append(karta)

f = open('myfile','w')

def printkolory(kolory):
	str = ""
	for y in range(len(kolory)):
		if y+1 != len(kolory):
			str = str + kolory[y] + "/"
		else:
			str = str + kolory[y]
	return str
	
	
for x in range(len(lista)):
	f.write(lista[x].name  + "." + printkolory(lista[x].kolor)  + "." +  lista[x].rarity  + "." + lista[x].set + "\n")