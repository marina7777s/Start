immutable_var = (5, 7, 9, "ручка", True)
print(immutable_var)
mutable_list = ([3, 5, 8], 2, 1)
mutable_list[0][1] = 6
print(mutable_list)
immutable_var[2] = 3 # эементы в кортеже не меняются