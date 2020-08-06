from random import randint

fishes = {"Arapaima": 50,
          "Bass": 20,
          "Lobster": 20,
          "Ray": 10,
          "Golden Chest": 5
         }

while True:
    print("Type 'fish' to cast your line!")
    print(">>>", end=" ")

    cmd = input()
    if cmd == "fish":
        totalSum = sum(fishes.values())
        rng = randint(0, totalSum-1)

        curSum = 0
        for fish, chance in fishes.items():
            if rng < curSum + chance:
                caughtFish = fish
                break
            else:
                curSum += chance

        print("You caught a {}!".format(caughtFish))