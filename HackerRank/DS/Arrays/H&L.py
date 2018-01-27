n=int(input())
a=list(map(int,input().split()))
flag=0
for i in range(n):
	for j in range(i,n):
		if a[i]<a[j]:
			flag=1
			break
	if flag==0:
		print(a[i],end=" ")
	flag=0