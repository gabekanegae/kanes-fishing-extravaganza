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

        # Add fish to Player.inventory
        if caughtFish not in self.inventory:
            self.inventory[caughtFish] = 0
        self.inventory[caughtFish] += 1

        # Add xp to Player.xp
        self.xp += fishes[caughtFish]["xpWorth"]
        self.levelUp()

        print("You caught a {}!".format(caughtFish))

    def printInventory(self):
        print("Inventory:")
        for fish, count in self.inventory.items():
            print("{:>3} | {}".format(count, fish))

    def __repr__(self):
        return "{} | Lv. {}, {}/500 XP | {}g".format(self.name, self.level, self.xp, self.gold)

    def levelUp(self):
        if self.xp >= 500:
            self.level += 1
            self.xp -= 500
            print("{} leveled to level {}!".format(self.name, self.level))