import random

def roll():
    min = 1
    max = 10
    roll = random.randint(min, max)

    return roll

Value = roll()
# Methode 1: Konvertierung mit str()
print("The number is: " + str(Value) + " times")

# Methode 2: String-Formatierung mit format()
print("The number is: {} times".format(Value)))

# Methode 3: F-Strings
print(f"The number is: {Value} times")

# Methode 4: Prozent-Formatierung
print("The number is: %d times" % Value)

while True:
    player = input("Enter the number of players (2 - 4): ")
    if player.isdigit():
        player = int(player)
        if 2<= player <= 4:
            print("there are {} players".format(player))
            break
        else:
            print("Player number must be between 2 and 4!")
    else:
        print("Invalid! Try again")        

