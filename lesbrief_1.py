fruit = {"banaan": "geel"}
fruit2 = {"aardbei": "rood"}
fruit3 = {"kiwi": "groen"}

fruit["perzik"] = "oranje"

#controleer = input("Welke index wil je opzoeken?")

def merge_three_dicts(fruit, fruit2, fruit3):
    fruit3 = fruit.copy()
    fruit3.update(fruit2)
    fruit3.update(fruit3)
    return fruit

fruit4 = merge_three_dicts(fruit, fruit2, fruit3)
print(fruit4)



#if controleer in fruit:
#    print(controleer + " zit erin")
#else:
#   print(controleer + " zit er niet in.")