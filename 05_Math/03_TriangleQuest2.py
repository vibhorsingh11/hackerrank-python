
# You are given a positive integer N. Print a numerical triangle of height N-1 like the one below:
#
# 1
# 22
# 333
# 4444
# 55555
# ......
# Can you do it using only arithmetic operations, a single for loop and print statement?
#
# Use no more than two lines.

for i in range(1, int(input())+1):
    print((10**i//9)**2)
