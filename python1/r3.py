# 2D Roguelike game
import random
print(" the 9/11 Game")
# Spielfeld erstellen
width = 10
height = 5
field = [['.' for _ in range(width)] for _ in range(height)]

# Held positionieren
hero = "✈️"
hero_x = 0
hero_y = 0

# Zufällige Hindernisse hinzufügen
for _ in range(10):
    x = random.randint(0, width-1)
    y = random.randint(0, height-1)
    if (x, y) != (hero_x, hero_y):
        field[y][x] = '🏡'

while True:
    # Grafik
    for y in range(height):
        for x in range(width):
            if x == hero_x and y == hero_y:
                print(hero, end="")
            else:
                print(field[y][x], end="")
        print()  # Neue Zeile
    
    print("Bitte Kommando eingeben: (w=hoch, s=runter, a=links, d=rechts, q=beenden)")
    command = input(">>> ")
    
    new_x, new_y = hero_x, hero_y
    
    if command == "w":
        new_y = max(0, hero_y - 1)
    elif command == "s":
        new_y = min(height - 1, hero_y + 1)
    elif command == "a":
        new_x = max(0, hero_x - 1)
    elif command == "d":
        new_x = min(width - 1, hero_x + 1)
    elif command == "q":
        print("Spiel beendet.")
        break
    else:
        print("Ungültiges Kommando")
        continue
    
    if field[new_y][new_x] != '#':
        hero_x, hero_y = new_x, new_y
    else:
        print("Du kannst nicht durch Hindernisse gehen!")

        