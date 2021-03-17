# You have a non-empty set , and you have to execute  commands given in  lines.

# The commands will be pop, remove and discard.

n = int(input())
s = set(map(int, input().split()))
N = int(input())
for i in range(0, N):
    operation = input().split()
    if operation[0] == "pop":
        s.pop()
    elif operation[0] == "remove":
        s.remove(int(operation[1]))
    elif operation[0] == "discard":
        s.discard(int(operation[1]))
print(sum(s))
