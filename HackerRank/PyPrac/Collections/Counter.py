import collections;
X=int(input());
ListOfShoeSize=list(map(int,input().split()));
d=collections.Counter(ListOfShoeSize);
N=int(input());
income=0;
for i in range(N):
    size,price=map(int,input().split());
    if d[size]:
        income=income+price;
        d[size]-=1
print (income);
        

#numShoes = int(input())
#shoes = collections.Counter(map(int, input().split()))
#numCust = int(input())
#
#income = 0
#
#for i in range(numCust):
#    size, price = map(int, input().split())
#    if shoes[size]: 
#        income += price
#        shoes[size] -= 1
#
#print (income)