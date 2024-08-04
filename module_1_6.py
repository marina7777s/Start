# работа со словарями
my_dict = {'Sara': 1996, 'Klara': 1990, 'Den': 1992}
print(my_dict)
print(my_dict['Sara'])
print(my_dict.get('Ken'))
my_dict.update({'Ken': 1993, 'Molli': 2001})
print(my_dict)
a = my_dict.pop('Sara')
print(my_dict)
print(a)
print(my_dict)
# работа с множествами
my_set = {2, 5, 2, 'book', 123.23, 123.23}
print(my_set)
my_set.add('apple')
my_set.add('plum')
print(my_set)
my_set.remove('plum')
print(my_set)
