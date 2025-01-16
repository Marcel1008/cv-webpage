todos = ['Apfel', 'Banane', 'Pfirsich']

for _ in range(3):
    newitem = input("Was möchtest du hinzufügen")
    todos.append(newitem)
    print("Meine todoliste hat folgende elemnete:")


    for todo in todos:
        print(f"- {todo}")
        print(todos)