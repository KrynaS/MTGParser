import json

class Karta:

	def __init__(self, name, kolor, rarity, set):
		self.name = name
		self.kolor = kolor
		self.rarity = rarity

f = open('sets.json',)
data = json.load(f)
f.close()

for i in data
