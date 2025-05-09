namen = ['Alice', 'Bob', 'Cathy', 'Dan', 'Ed', 'Frank', 'Gary', 'Helen', 'Irene', 'Jack', 'Kelly', 'Larry']
for x in namen:
    print(x)

print("und jetzt mit nummern")

for nummer,x in enumerate(namen,1):
    print(nummer,x)
        