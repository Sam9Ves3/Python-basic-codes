def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)
n = 20
for i in range(0, n):
    print("{0}! = {1}".format(i, fact(i)))