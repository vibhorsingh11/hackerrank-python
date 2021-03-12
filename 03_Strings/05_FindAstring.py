# In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the
# given string. String traversal will take place from left to right, not from right to left.

def count_substring(string, sub_string):
    c = start = 0
    while True:
        start = string.find(sub_string, start)+1
        if start > 0:
            c += 1
        else:
            return c


if __name__ == '__main__':
    string = input("Enter string\n").strip()
    sub_string = input("Enter subString\n").strip()

    count = count_substring(string, sub_string)
    print(count)
