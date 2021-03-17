# Given 2 sets of integers, M and N, print their symmetric difference in ascending order. The term symmetric difference indicates
# those values that exist in either M or N but do not exist in both.

# Enter your code here. Read input from STDIN. Print output to STDOUT
a, b = (int(input()), input().split())
c, d = (int(input()), input().split())

x = set(b)
y = set(d)

p = y.difference(x)

q = x.difference(y)

r = p.union(q)

print('\n'.join(sorted(r, key=int)))
