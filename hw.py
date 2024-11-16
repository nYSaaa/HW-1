Fruits = ["Apple" , "Banana" , "Pineapple" , "Grapes"]

for fruit in Fruits:
    print(fruit)

Fruits.append("Mango")
Fruits.append("Oranges")

Fruits.sort()

for fruit in Fruits:
    print(fruit)

print(len(Fruits))
Fruits.remove("Banana")
print(Fruits)