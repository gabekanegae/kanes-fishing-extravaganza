from random import randint
from Player import Player

import json

def getRandomFish(fishes):
    totalSum = 0
    for fish, attributes in fishes.items():
        totalSum += attributes["chance"]

    rng = randint(0, totalSum-1)

    curSum = 0
    for fish, attributes in fishes.items():
        if rng < curSum + attributes["chance"]:
            return fish
        else:
            curSum += attributes["chance"]

def loadJSON(filename):
    with open(filename) as f:
        return json.load(f)

def saveJSON(filename, data):
    with open(filename, "w+") as f:
        json.dump(data, f)

def loadPlayer(filename):
    try:
        playerJSON = loadJSON(filename)
    except:
        return None

    player = Player(playerJSON["name"],
                    playerJSON["level"],
                    playerJSON["xp"],
                    playerJSON["gold"],
                    playerJSON["inventory"])

    return player

def savePlayer(player, filename):
    playerDict = {"name": player.name,
                  "level": player.level,
                  "xp": player.xp,
                  "gold": player.gold,
                  "inventory": player.inventory}

    saveJSON(filename, playerDict)