age = input("Wie alt bist du ?")

if float(age) >= 18:
    print("Du bist volljährig")
else:
    print("Du bist nicht volljährig")

    while True:
        score_string = input("wie viele punkte hast du ? ")
        score_int = int(score_string)

        if score_int == 10:
            print("Sehr gut")
        elif score_int > 7:
            print("gut")
        elif score_int >5:
            print("Befridigend aber nicht fur deine eltern")
        elif score_int ==5:
            print("Genügend,lern besser")
        else:
            print("Nicht genügend,trottel")
                #
              while True:
                score_string = input("Wie lange programmierst du am Tag? ")
                score_int = int(score_string)

                if score_int == 4:
                    print("Sehr gut")
                elif score_int > 3:
                    print("gut")
                elif score_int >2:
                    print("Befridigend aber nicht fur deine eltern")
                elif score_int ==1:
                    print("Genügend,lern besser")