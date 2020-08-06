import utils

class Player:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.xp = 0
        self.gold = 0
        self.inventory = dict()

    def castLine(self, fishes):
        caughtFish = utils.getRandomFish(fishes)

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