import random as r

appetizers = {'country greens': 12, 'onion rings': 13, 'butterbrodt': 46}
main_courses = {'super potato': 612, 'soup': 143, 'curry': 436}
desserts = {'shugar': 1, 'donat': 8, 'cake': 4}
dish_types = [appetizers, main_courses, desserts]

keys = []
items = []
for dish_type in dish_types:
    i = 0
    dish_index = r.randint(0, len(dish_type) - 1)
    for key, item in dish_type.items():
        if i == dish_index:
            keys.append(key)
            items.append(item)
        i += 1

print(keys, items, sum(items))