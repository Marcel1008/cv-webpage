#aufgabe 1
todos = ['Putzen', 'Schlafen', 'Essen']
newtodo = input("Was möchtest du hinzufügen")
todos.append(newtodo)
print(f"Meine todoliste hat folgende elemnete:{todos}")

#aufgabe 1a
film = ['spiderman', 'johnpork', 'teletubbies']
newfilm = input("Was möchtest du hinzufügen")
film.append(newfilm)
print(f"Meine filmliste hat folgende elemnete:{film}")
#aufgabe 1b
freunde = ['mcdonald trump', 'alexander van der hundebellen', 'herberet kickl']
newfreunde = input("Was möchtest du hinzufügen")
film.append(newfreunde)
print(f"Meine filmliste hat folgende elemnete:{freunde}")
#aufgabe 2
todos = ['Putzen', 'Schlafen', 'Essen']
while True:
    #aufgabe 2a
    while True:
        film = ['spiderman', 'johnpork', 'teletubbies']
        newfilm = input("Was möchtest du hinzufügen")
        film.append(newfilm)
        #aufgabe 2b
        while True:
            freunde = ['mcdonald trump', 'alexander van der hundebellen', 'herberet kickl']
            newfreunde = input("Was möchtest du hinzufügen")
            film.append(newfreunde)
            print(f"Meine filmliste hat folgende elemnete:{freunde}")