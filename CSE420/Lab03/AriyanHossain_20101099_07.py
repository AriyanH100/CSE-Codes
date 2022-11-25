import re

pattern=[]  #list for patterns
n1=int(input())
for i in range(n1):
    inp1=input()
    p=inp1+'$'
    pattern.append(p)
n2=int(input())
lst=[]  #list for strings
for i in range(n2):
    inp2=input()
    lst.append(inp2)
for i in range(len(lst)):   
    flag=0  #checks if pattern matches any string
    for j in range(len(pattern)):
        if (re.match(pattern[j],lst[i])):
            if flag==1:
                print(",",j+1,end="")
            else:
                flag=1
                print("YES,",j+1,end="")
    if flag==1:
        print()
    if flag==0:
        print("NO, 0")
    
