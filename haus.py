# 6. BMI Rechner als Funktion
def berechne_bmi(gewicht, groesse_cm):
    groesse_m = groesse_cm / 100  # Größe in Meter
    bmi = gewicht / (groesse_m ** 2)
    print(f"Dein BMI beträgt: {bmi:.2f}")


# 7. Taschengeldplaner

def taschengeld(monatliches_taschengeld, laufzeit_monate):
    gespart = monatliches_taschengeld * laufzeit_monate
    print(f"Nach {laufzeit_monate} Monaten hast du {gespart}€ gespart.")


# 8. Zahlenratespiel
def zahlenratespiel():
    geheimzahl = 7
    versuche = 5

    for versuch in range(1, versuche + 1):
        tipp = int(
            input(f"Versuch {versuch}/{versuche}: Gib deine Zahl ein: "))

        if tipp < geheimzahl:
            print("Zu niedrig!")
        elif tipp > geheimzahl:
            print("Zu hoch!")
        else:
            print("Herzlichen Glückwunsch! Du hast die Zahl erraten.")
            break
    else:
        print("Leider hast du die Zahl nicht erraten. Die richtige Zahl war 7.")


# 9. Notenübersicht mit Schleife und Verzweigung
def notenuebersicht():
    while True:
        name = input("Eingabe Name: ")
        if name.lower() == "ende":
            print("Programm beendet.")
            break
        note = float(input("Eingabe Note: "))

        if note >= 5:
            print(f"{name} hat bestanden!")
        else:
            print(f"{name} ist durchgefallen.")


# 10. E-Mail Generator
def erstelle_email(vorname, nachname):
    email = f"{vorname.lower()}.{nachname.lower()}@schule.com"
    print(f"Deine neue E-Mail-Adresse lautet: {email}")


# 11. Erweiterter Newsletter-Generator

def erstelle_newsletter(empfaenger, absender, adresse, ort):
    nachricht = f"Hallo {empfaenger}!\n\nMit dieser Email möchte ich dich über meine neue Adresse informieren.\n{adresse}\n{ort}\n\nLiebe Grüße\n{absender}"
    print(nachricht)


# 11(Aber sigma variante)
name = input("An wen geht die Nachricht? ")
absender = input("Wer ist der Absender? ")

print(f"Hallo {name}")
print("")
print("Mit dieser E-Mail möchte ich dich über meine neue Adresse informieren.")
print("")
print("Musterstraße 123")
print("12345 Musterhausen")
print("Viele Grüße")
print("")
print(f"{absender}")


