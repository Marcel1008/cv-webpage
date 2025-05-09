#roguelike game

sigma = "abcdefghijklmnoDpqr§ghfvksP"
hero = "@"
hero_x = 0

while True:
  #grafik
    for xpos, title in enumerate(sigma):
        if xpos == hero_x:
            print(hero, end="")
        else:
            print(title, end="")
    print() #neue zeile
    
    print("bitte commando eingeben: (a oder d)")
    commando = input(">>>")
    if commando == "a":
        hero_x -= 1
    elif commando == "d":
        hero_x += 1
    else:
        print("ungültiges commando")