import csv
import json

inFile = open("AllSets.json", "r")
outFile = open("white.txt", "w") 
outFileU = open("blue.txt", "w")
outFileB = open("black.txt", "w")
outFileR = open("red.txt", "w")
outFileG = open("green.txt", "w")
outFileM = open("multi.txt", "w")
outFileC = open("colorless.txt", "w")

x = json.loads(file)

list = []

for mSet in x:
    for card in x.cards:
        if card.color.length == 1 and card.color[0] == "W":
            color = "White"
        elif card.color.length == 1 and card.color[0] == "U":
            color = "Blue"
        elif card.color.length == 1 and card.color[0] == "B":
            color = "Black"
        elif card.color.length == 1 and card.color[0] == "R":
            color = "Red"
        elif card.color.length == 1 and card.color[0] == "G":
            color = "Green"
        elif card.color.length == 0:
            color = ""
        elif card.color.length > 1:
            color = "Multi"

        if card.rarity == "common":
            rarity = "C"
        elif card.rarity == "uncommon":
            rarity = "D"
        elif card.rarity == "rare":
            rarity = "E"
        elif card.rarity == "mythic":
            rarity = "M"

        list.append([card.name, color, card.rarity, mSet.name, mSet.releaseDate])

list.sort(key = operator.itemgetter(4), reverse=True)
list.sort(key = operator.itemgetter(1, 3, 2, 0)

for card in list:
    outFile.write(card[0] + ", " + card[1] + ", " + card[2] + ", " + card[3])