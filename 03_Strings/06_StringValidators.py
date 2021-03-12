# Python has built-in string validation methods for basic data. It can check if a string is composed of alphabetical characters,
# alphanumeric characters, digits, etc.

if __name__ == '__main__':
    s = input("Enter the string\n")
    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))
