from random import randint

class Player:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.xp = 0
        self.gold = 0
        self.inventory = dict()

    def castLine(self, fishes):
        caughtFish = getRandomFish(fishes)

        if caughtFish not in self.inventory:
            self.inventory[caughtFish] = 0
        self.inventory[caughtFish] += 1

        print("You caught a {}!".format(caughtFish))

    def printInventory(self):
        print("Inventory:")
        for fish, count in self.inventory.items():
            print("{:>3} | {}".format(count, fish))

    def levelUp(self):
        if self.xp > 500:
            self.level += 1
            self.xp -= 500
            print("{} leveled to level {}!".format(self.name, self.level))

def getRandomFish(fishes):
    totalSum = sum(fishes.values())
    rng = randint(0, totalSum-1)

    curSum = 0
    for fish, chance in fishes.items():
        if rng < curSum + chance:
            return caughtFish
        else:
            curSum += chance

fishes = {"Arapaima": 50,
          "Bass": 20,
          "Lobster": 20,
          "Ray": 10,
          "Golden Chest": 5
         }

player = Player("Kane")
while True:
    print("Type 'fish' to cast your line!")
    print(">>>", end=" ")

    cmd = input()
    if cmd == "fish":
        player.castLine(fishes)
    elif cmd == "inv":
        player.printInventory()