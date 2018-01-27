A=set(input().split());
n=int(input());
x=True;
for i in range(n):
    temp=x;
    B=set(input().split());
    x= ((B==A.intersection(B)) and (len(A.difference(B))>0))
    y=temp and x;
    
    
    
print (y)  