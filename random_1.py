import random

def roll():
    min = 1
    max = 6
    roll = random.randint(min, max) # generiert eine Zufallszahl zwischen 1 und 6
    return roll
"""
Value = roll()
# Methode 1: Konvertierung mit str()
print("The number is: " + str(Value) + " times")

# Methode 2: String-Formatierung mit format()
print("The number is: {} times".format(Value)))

# Methode 3: F-Strings
print(f"The number is: {Value} times")

# Methode 4: Prozent-Formatierung
print("The number is: %d times" % Value)
"""
while True:
    players = input("Enter the number of players (2 - 4): ")
    if players.isdigit(): #überprüft, ob die Eingabe eine Zahl ist
        players = int(players) #konvertiert die Eingabe in eine Ganzzahl
        if 2<= players <= 4:
            print("there are {} players".format(players))
            break #beendet die Schleife, wenn die Eingabe gültig ist.
        else:
            print("Player number must be between 2 and 4!")
    else:
        print("Invalid! Try again")        

max_score = 50 #maximale Punktzahl, die ein Spieler erreichen muss, um zu gewinnen.
player_scores = [0 for _ in range(players)] #eine Liste mit 0 für jeden Spieler, um die Punktzahl zu speichern.

#       HAUPTSCHLEIFE
while max(player_scores) < max_score: #wiederholt die Schleife, solange keiner der Spieler die maximale Punktzahl erreicht hat.
    for player_idx in range(players): #iteriert über jeden Spieler
        print("\nPlayer number", player_idx + 1, "turn has just started!") #zeigt an, welcher Spieler an der Reihe ist.
        print("Your total score is:", player_scores[player_idx], "\n") #zeigt die aktuelle Gesamtpunktzahl des Spielers an.
        current_score = 0 #setzt den Rundenscore des Spielers auf 0. 

#       #   Innere Schleife für den Wurf
        while True: #Endlosschleife für den Wurf des Spielers
            should_roll = input("Would you like to roll (y)? ") #möchte der Spieler würfeln
            if should_roll.lower() != "y": #überprüft, ob die Antwort nicht 'y' ist
                break # beendet die Wurfschleife, wenn der Spieler nicht würfeln möchte

            value = roll() # führt den Würfelwurf aus
            if value == 1: #überprüft, ob der Spieler eine 1 geworfen hat
                print("Wurf ist 1! Deine Runde ist vorbei!")
                current_score = 0 # setzt den Rundenscore auf 0
                break #beendet die Wurfschleife
            else: # wird ausgeführt, wenn der Spieler keine 1 geworfen hat
                current_score += value # addiert den Wurfwert zum Rundenscore
                print("You rolled a:", value) # Zeigt den wurfwert an.

            print("Your score is:", current_score) # zeigt den aktuellen Rundenscore an

#       Hinzufügen des Rundenscores zur Gesamtpunktzahl
        player_scores[player_idx] += current_score # addiert den Rundenscore zur Gesamtpunktzahl des Spielers
        print("Deine Gesamtpunktzehl ist:", player_scores[player_idx]) # zeigt die aktualisierte Gesamtpunktzahl des Spielers an.
        break
        
max_score = max(player_scores) # findet die höchste Punktzahl.
winning_idx = player_scores.index(max_score) # findet den Index des Spielers mit der höchsten Punktzahl.
print("Player number", winning_idx + 1,
      "is the winner with a score of:", max_score) # zeigt den Gewinner und seine Punktzahl an