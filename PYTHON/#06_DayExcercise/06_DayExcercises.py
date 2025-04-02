#06_DayExcercise1

list = tuple()


brother = ("Alan", "Sebas")
sister = ("Mariana", "karla")
hermanos_y_hermanas = brother + sister
print(hermanos_y_hermanas)


hermanos = hermanos_y_hermanas


count = len(hermanos)
print('numero de hermanos de hermanos', len(hermanos))


family_memembers = hermanos + ('Omar','Jessica')
print(family_memembers)


sibling = family_memembers[:len(hermanos_y_hermanas)]
parents = family_memembers[-2:]
print(sibling, parents)


fruit = ("Mango", "Banana", "apple")
veggies = ("tomato", "Onion", "broccoli")
animal_product = ("Bacon", "Egg", "Butter")


food_stuff_tp = fruit + veggies + animal_product
print(food_stuff_tp)


food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)


mid = int(len(food_stuff_tp)/2)
food_stuff_tp = food_stuff_tp[:mid]
print(food_stuff_tp)

del food_stuff_tp


nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)
