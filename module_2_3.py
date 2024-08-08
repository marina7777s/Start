
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
a = 0
while a < len(my_list):
    elem = my_list[a]
    a += 1
    if elem > 0:
        print(elem)
    if elem < 0:
        break
    if a == 0:
        continue




