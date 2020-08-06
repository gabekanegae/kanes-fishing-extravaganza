from Player import Player

fishes = {"Arapaima":
                  {"chance": 50,
                  "xpWorth": 100,
                  "goldWorth": 100},
          "Bass":
                  {"chance": 20,
                  "xpWorth": 100,
                  "goldWorth": 100},
          "Lobster":
                  {"chance": 20,
                  "xpWorth": 100,
                  "goldWorth": 100},
          "Ray":
                  {"chance": 10,
                  "xpWorth": 100,
                  "goldWorth": 100},
          "Golden Chest":
                  {"chance": 5,
                  "xpWorth": 100,
                  "goldWorth": 100}
         }

def main():
    player = Player("Kane")
    while True:
        print("Type 'fish' to cast your line!")
        print(">>>", end=" ")

        cmd = input()
        if cmd == "fish":
            player.castLine(fishes)
        elif cmd == "inv":
            player.printInventory()

if __name__ == "__main__":
    main()