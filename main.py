import utils
from Player import Player

def main():
    player = Player("Kane")

    fishes = utils.loadFishDB("fishDB.json")
    print(fishes["Arapaima"]["xpWorth"])

    while True:
        print("Options: [f]ish | [i]nventory | [p]layer info | [e]xit")
        cmd = input(">>> ").lower()

        if cmd.startswith("f"): # fish
            player.castLine(fishes)
        elif cmd.startswith("i"): # inventory
            player.printInventory()
        elif cmd.startswith("p"): # player info
            print(player)
        elif cmd.startswith("e"): # exit
            print("Thanks for playing!")
            return

if __name__ == "__main__":
    main()