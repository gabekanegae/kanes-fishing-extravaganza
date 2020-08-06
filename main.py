import utils
from Player import Player

FISH_FILE = "fishDB.json"
PLAYER_FILE = "player_savefile.json"

def main():
    # Load fish list
    fishes = utils.loadJSON(FISH_FILE)

    # Load player (or create one)
    player = utils.loadPlayer(PLAYER_FILE)
    if not player:
        playerName = input("Ahoy fisherman! I see you're new here! What's your name? ")
        player = Player(playerName)

    # Main loop
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
            utils.savePlayer(player, PLAYER_FILE)
            return

if __name__ == "__main__":
    main()