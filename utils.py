from random import randint

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