import random
print("Affe gegen drachen")

# Spielfeld erstellen
width = 20  # Breite erhöht
height = 10  # Höhe erhöht
field = [['.' for _ in range(width)] for _ in range(height)]

# Held positionieren
hero = "🐒"
hero_x = 0
hero_y = 0

# Zufällige Hindernisse hinzufügen
for _ in range(20):  # Anzahl der Hindernisse erhöht
    x = random.randint(0, width-1)
    y = random.randint(0, height-1)
    if (x, y) != (hero_x, hero_y):
        field[y][x] = '🐲'
        #Gold
for _ in range(20):
    x = random.randint(0, width-1)
    y = random.randint(0, height-1)
    if (x, y) != (hero_x, hero_y):
        field[y][x] = '🔫'

while True:
    # Grafik
    for y in range(height):
        for x in range(width):
            if x == hero_x and y == hero_y:
                print(hero, end=" ")
            else:
                print(field[y][x], end=" ")
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
    
    if field[new_y][new_x] == '🐲':
        print("Du bist unbewaffnet in einen drachen rein gelaufen")
        break
    if field[new_y][new_x] == '🔫':
        print("Du hast eine pistole aufgehoben")
        hero = "🦍"
    else:
        hero_x, hero_y = new_x, new_y
print("Game Over")