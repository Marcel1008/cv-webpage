def meine_funktion():

    gewicht=input("Gewicht in kg: ")
    Größe=input("Größe in cm: ")
    dauer = input("Dauer in Minuten: ")
    intensität = input("Intensität Leicht oder mittel oder schwer: ")
    if intensität == "Leicht":
        print("Du hast in", dauer, "Minuten", (3.5 * 3.5 * 60 * float(dauer) * float(gewicht) / 200, "Kalorien verbrannt."))
    elif intensität == "mittel":
        print("Du hast in", dauer, "Minuten", (4.0 * 4.0 * 60 * float(dauer) * float(gewicht) / 200, "Kalorien verbrannt."))
    elif intensität == "schwer":
        print("Du hast in", dauer, "Minuten", (5.0 * 5.0 * 60 * float(dauer) * float(gewicht) / 200, "Kalorien verbrannt."))
    else:
        print("andere auswahl gibt es nd du trottel")
        
meine_funktion()

import math as sigma
def calculate_saving():