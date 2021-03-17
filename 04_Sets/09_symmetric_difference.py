# The first line contains the number of students who have subscribed to the English newspaper.
# The second line contains the space separated list of student roll numbers who have subscribed to the English newspaper.
# The third line contains the number of students who have subscribed to the French newspaper.
# The fourth line contains the space separated list of student roll numbers who have subscribed to the French newspaper.

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
nSub = set(map(int, input().split()))
b = int(input())
bSub = set(map(int, input().split()))
unionSub = nSub.symmetric_difference(bSub)
print(len(unionSub))
