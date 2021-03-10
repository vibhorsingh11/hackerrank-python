"""
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer e at position i.
print: Print the list.
remove e: Delete the first occurrence of integer e.
append e: Insert integer e at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above. 
Iterate through each command in order and perform the corresponding operation on your list.
"""

if __name__ == '__main__':
    N = int(input("Enter the length\n"))

    my_list = []

    for _ in range(0, N):
        line = input().strip()

        # print the list and continue
        if line == "print":
            print(my_list)
            continue

        # This will split the command in function and the argument.
        # For e.g. insert x will have - parts[0] = insert and part[1] = x
        parts = line.split()

        getattr(my_list, parts[0])(*(map(int, parts[1:])))
