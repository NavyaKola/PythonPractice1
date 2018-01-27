from collections import namedtuple
N=int(input());
namesOfTheCol=input().split();
sum1=0;
for i in range(N):
    Student=namedtuple('Info',namesOfTheCol);
    f1,f2,f3,f4=input().split();
    s=Student(f1,f2,f3,f4)
    sum1=float(s.MARKS)+sum1;
print ('{:.2f}'.format(sum1/N))
