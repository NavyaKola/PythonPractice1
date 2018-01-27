s=input().split();
n=s[0];
m=s[1];
sarray=input().split();
setA=set(input().split());
setB=set(input().split());
hap=0;
for i in sarray:
    if (i in setA):
        hap=hap+1;
    elif (i in setB):
        hap=hap-1;
    else:
        hap=hap;
print (hap);