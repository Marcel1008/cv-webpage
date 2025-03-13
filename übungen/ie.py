
while True:
    score_string = input("wie viele punkte hast du ? ")
    score_int = int(score_string)

    if score_int == 10:
        print("Sehr gut")
    elif score_int > 7:
        print("gut")
    elif score_int >5:
        print("Befridigend")
    elif score_int ==5:
        print("Genügend")
    else:
        print("Nicht genügend")