grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_sorted = sorted(students)
print(students_sorted)
new_dict = {students_sorted[0]: float(sum(grades[0])/(len(grades[0]))), students_sorted[1]: float(sum(grades[1])/(len(grades[1]))), students_sorted[2]: float(sum(grades[2])/(len(grades[2]))), students_sorted[3]: float(sum(grades[3])/(len(grades[3]))), students_sorted[4]: float(sum(grades[4])/(len(grades[4])))}
print(new_dict)