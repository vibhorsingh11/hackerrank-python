"""
Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
"""
if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([score, name])

    students.sort()
    b = [i for i in students if i[0] != students[0][0]]
    c = [j for j in b if j[0] == b[0][0]]

    c.sort(key=lambda x: x[1])
    for i in range(len(c)):
        print(c[i][1])
