grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = sorted(list(students))
grades_aver = []
for i in range(len(grades)):
    g = [sum(grades[i]) / len(grades[i])]
    grades_aver.append(g)
stud_grades = dict(zip(students, grades_aver))

print(stud_grades)
