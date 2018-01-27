from collections import Counter
s=dict(Counter(input()))
s1={}
l=list(s.values());
l=(sorted(l,key=int,reverse=True))
l1=[];
l2=list(s.keys());
l2=(sorted(l2,key=str,reverse=False))
print(l2)