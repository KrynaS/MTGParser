import json
from turtle import color, sety
from pprint import pprint
from xlwt import Workbook

def printkolory(kolory):
	str = ""
	for y in range(len(kolory)):
		if y+1 != len(kolory):
			str = str + kolory[y] + "/"
		else:
			str = str + kolory[y]
	return str

def printRarity(rarity):
	str = ''
	first = True
	if 'common' in rarity:
		str += 'C'
		first = False
	if 'uncommon' in rarity:
		str += 'U' if first else '/U'
		first = False
	if 'rare' in rarity:
		str += 'R' if first else '/R'
		first = False
	if 'mythic' in rarity:
		str += 'M' if first else '/M'
		first = False
	return str

class Karta:

	def __init__(self, name, kolor, rarity, ilosc):
		self.name = name
		self.kolor = kolor
		self.rarity = rarity
		self.ilosc = ilosc

	def isLowestRarity(self, rarity):

		if self.isThisRarity(rarity):
			if rarity == 'common':
				return True
			if rarity == 'uncommon' and 'common' not in self.rarity :
				return True
			if any(x in rarity for x in ['rare', 'mythic']) and 'common' not in self.rarity and 'uncommon' not in self.rarity:
				return True
			
		return False

	def isThisRarity(self, rarity):
		return any(x in rarity for x in self.rarity)

class Karty:
	
	def __init__(self, dict):
		self.fullList = dict.values()

	# def __init__(self, dict1, dict2):
	# 	for card in dict2:
	# 		if dict1[card.name] == None:
	# 			dict1[card.name] = card

	def getByExactColorAndRarity(self, color, rarity):
		result = list()

		for karta in self.fullList:
			if color in karta.kolor and len(karta.kolor) == 1 and karta.isLowestRarity(rarity):
				result.append(karta)
		result.sort(key=lambda x: x.name, reverse=False)
		return result

	def getMultiColorsByRarity(self, rarity):
		result = list()

		for karta in self.fullList:
			if len(karta.kolor) > 1 and karta.isLowestRarity(rarity):
				result.append(karta)
		result.sort(key=lambda x: x.name, reverse=False)
		return result

	def getNoColorByRarity(self, rarity):
		result = list()

		for karta in self.fullList:
			if len(karta.kolor) == 0 and karta.isLowestRarity(rarity):
				result.append(karta)
		result.sort(key=lambda x: x.name, reverse=False)
		return result
	

f = open('AllPrintings.json', encoding='utf-8')
data = json.load(f)
dict = dict()
data = data['data']

for set in data.values():
	if set.get('isPartialPreview', None) == True:
		continue
	for card in set['cards']:
		if card['name'] == 'World Breaker':
			stop = 0
		if card.get('isOnlineOnly', None) == True:
			continue
		if dict.get(card['name']) != None:
			if card['rarity'] not in dict[card['name']].rarity:
				# if card['name'] == 'Serra Angel':
				# 	stop = 0
				dict[card['name']].rarity.append(card['rarity'])
		else:
			# if card['legalities'].get('pioneer') != None and card['legalities'].get('pioneer') == 'Legal':
			if card.get('text', None) != None and "Devoid" in card['text']:
				if card.get('manaCost', None) != None:
					if '{W}' in card['manaCost'] and 'W' not in card['colors']:
						card['colors'].append('W')
					if '{U}' in card['manaCost'] and 'U' not in card['colors']:
						card['colors'].append('U')
					if '{B}' in card['manaCost'] and 'B' not in card['colors']:
						card['colors'].append('B')
					if '{R}' in card['manaCost'] and 'R' not in card['colors']:
						card['colors'].append('R')
					if '{G}' in card['manaCost'] and 'G' not in card['colors']:
						card['colors'].append('G')
			karta = Karta(card['name'], card['colors'], [card['rarity']], 0)
			dict[karta.name] = karta

f = open('myfile','w')
	
karty = Karty(dict)

wb = Workbook()
sheet = wb.add_sheet('Karty')

kolory = ['W', 'U', 'B', 'R', 'G', ]
rarity = ['common', 'uncommon', ['rare', 'mythic']]

i = 0
for k in kolory:
	for r in rarity:
		for x in karty.getByExactColorAndRarity(k, r):
			#f.write(lista[x].name  + "." + printkolory(lista[x].kolor)  + "." +  lista[x].rarity  + "\n")
			sheet.write(i, 0, x.name)
			sheet.write(i, 1, x.kolor)
			sheet.write(i, 2, printRarity(x.rarity))
			sheet.write(i, 3, x.ilosc)
			i+=1

for r in rarity:
	for x in karty.getMultiColorsByRarity(r):
		sheet.write(i, 0, x.name)
		sheet.write(i, 1, x.kolor)
		sheet.write(i, 2, printRarity(x.rarity))
		sheet.write(i, 3, x.ilosc)
		i+=1

for r in rarity:
	for x in karty.getNoColorByRarity(r):
		sheet.write(i, 0, x.name)
		sheet.write(i, 1, x.kolor)
		sheet.write(i, 2, printRarity(x.rarity))
		sheet.write(i, 3, x.ilosc)
		i+=1

wb.save('karty.xls')