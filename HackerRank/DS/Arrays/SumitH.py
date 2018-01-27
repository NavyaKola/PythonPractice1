t = int(input())
 
for t_i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    pos = []
    neg = []
    for num in arr:
        if num < 0:
            neg.append(num)
        else:
            pos.append(num)
    neg = sorted(neg, reverse=True)
    i = len(pos)
    a = sum(pos)
    b = sum(neg)
    tmax = i*a + b
    for j in range(len(neg)):
        i += 1
        a += neg[j]
        b -= neg[j]
        thismax = i*a + b
        if thismax > tmax:  tmax = thismax
    print(tmax)