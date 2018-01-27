# Enter your code here. Read input from STDIN. Print output to STDOUT
# -*- coding: utf-8 -*-
N=int(input());
stamps=set();
for i in range(N):
    stamp=input()+"\n";
    stamps.add(stamp);
print (len(stamps));

