#1
magicword = input("Wie lautet dein Zauberwort")
print (f"Achtung! Dein Geheimwort lautet:{magicword}")
#2
food = input("was ist dein lieblings essen")
drink = input("was ist dein lieblings getränk")

print(f"deine perfekte mahlzeit ist {food} mit einem kaltem{drink}")
#3
while True:
    hobys = ['Putzen', 'Schlafen', 'Essen']
    newhoby = input("Was möchtest du hinzufügen? ")
    hobys.append(newhoby) 
    if newhoby == "stop":
        break
    print(f"Meine hobyliste hat folgende elemnete:{hobys}")
    

    todos = ['zimmerPutzen', 'Schlafen', 'Essen']

    newtodo = input("Was möchtest du hinzufügen")
    todos.append(newtodo)
    if newtodo == "sigma":
        break
print("Meine todoliste hat folgende elemnete:")

#aufgabe sigma 4
to_do_liste = ["Vokabeln lernen", "Zimmer putzen", "Joggen"]

print("Willkommen zu deiner To-Do-Liste!")
print("Deine to-Do-Liste ist kein sigma aber hat folgende elemente{to_do_liste}:")

print("\Gib neue Aufgaben ein, oder tippe 'fertig', um das Programm zu beenden.")

while True:
    neue_aufgabe = input("Neue Aufgabe hinzufügen: ")
    
    
    if neue_aufgabe.lower() == "fertig":
        print("Programm beendet. Hier ist deine finale To-Do-Liste:")
        break
    to_do_liste.append(neue_aufgabe)
    

    print("\Deine aktuelle To-Do-Liste:")
    for index, aufgabe in enumerate(to_do_liste, start=1):
        print(f"{index}. {aufgabe}")



# 5
temperatur = float(input("Wie ist die aktuelle Außentemperatur in Grad Celsius? "))


if temperatur > 25:
    print("Perfekt für kurze Kleidung oder Sommeroutfits!")
elif 15 <= temperatur <= 25:
    print("Leichte Jacke reicht aus.")
else:
    print("Bitte warm anziehen und eventuell Schal mitnehmen!")

#6 sigma satzt des pitatotas
import math  


def berechne_kreisumfang(radius):
    """
    Berechnet den Umfang eines Kreises basierend auf dem Radius.
    Formel: Umfang = 2 * π * Radius
    """
    umfang = 2 * math.pi * radius  
    return umfang  


radien = [3, 5, 10]  

for radius in radien:
    umfang = berechne_kreisumfang(radius)  
    print(f"Der Umfang des Kreises mit Radius {radius} beträgt {umfang:.2f} (Einheiten).")


