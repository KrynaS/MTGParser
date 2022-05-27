import csv
import json
from operator import itemgetter, attrgetter, methodcaller

class Karta:

	def __init__(self, name, kolor, rarity, set, data):
		self.name = name
		self.kolor = kolor
		self.rarity = rarity
		self.set = set
		self.data = data
	
	def raritySort(self):
		if self.rarity == "common":
			return 0
		if self.rarity == "uncommon":
			return 1
		if self.rarity == "rare":
			return 2
		if self.rarity == "mythic":
			return 3
	def colorSort(self):
		if self.kolor == "":
			return 10
		if len(self.kolor) > 1:
			return 11
		if self.kolor[0] == "W":
			return 5
		if self.kolor[0] == "U":
			return 6
		if self.kolor[0] == "B":
			return 7
		if self.kolor[0] == "R":
			return 8
		if self.kolor[0] == "G":
			return 9

inFile = open("data.json", "r", encoding="utf-8")
outFile = open("white.txt", "w", encoding="utf-8")

data = json.load(inFile)
lista = []

for i in data:
	for j in data[i]['cards']:
		if not j['colors']:
			karta = Karta(j["name"], "", j["rarity"], data[i]["name"], data[i]["releaseDate"])
		else:
			karta = Karta(j["name"], j["colors"], j["rarity"], data[i]["name"], data[i]["releaseDate"])
		if not data[i]['isOnlineOnly']:
			lista.append(karta)

f = open('myfile','w', encoding="utf-8")

def printkolory(kolory):
	str = ""
	for y in range(len(kolory)):
		if y+1 != len(kolory):
			str = str + kolory[y] + "/"
		else:
			str = str + kolory[y]
	return str

lista.sort(key=attrgetter('name'))
lista.sort(key=methodcaller('raritySort'))
lista.sort(key=attrgetter('set'))
lista.sort(key=attrgetter('data'), reverse=True)
lista.sort(key=methodcaller('colorSort'))
	
for x in range(len(lista)):
	f.write(lista[x].name  + "." + printkolory(lista[x].kolor)  + "." +  lista[x].rarity  + "." + lista[x].set + "\n")