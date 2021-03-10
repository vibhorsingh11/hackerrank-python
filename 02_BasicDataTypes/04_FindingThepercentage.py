# The provided code stub will read in a dictionary containing key/value pairs of name: [marks] for a list of students.
# Print the average of the marks array for the student name provided, showing 2 places after the decimal.

if __name__ == '__main__':
    n = int(input("Enter length"))
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    # Fetching the queried student
    score = student_marks[query_name]
    # Calculating  the average
    resAverage = sum(score)/3
    # print average upto 2 decimal
    print("{:.2f}".format(resAverage))
