#if __name__ == '__main__':
N = int(input())
l=[];
for i in range(0,N):
    s=input().split(" ");
    command=s[0];
    args=s[1:];
    if (command!="print"):
        command+="(" + "," .join(args)+")";
        eval("l."+command);
        print (l);
    else:
        print (l);
            
        
        #switch(command)
# -*- coding: utf-8 -*-

