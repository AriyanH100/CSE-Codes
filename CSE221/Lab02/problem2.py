with open("input2.txt","r") as f:
    content=f.read()
    lst=list(content.split("\n"))
    lst1=list(lst[1].split(" "))
    lst2=list(lst[0].split(" "))
    A=[]
    for i in lst1:
            A.append(int(i))

n=int(lst2[0])
m=int(lst2[1])

for i in range(n):
    min=i  
    for j in range(i+1,n):
        if A[min]>A[j]:
            min=j
                      
    temp=A[min]
    A[min]=A[i]
    A[i]=temp
  
with open("output2.txt","w") as g:  
    for i in range(m):
        g.write(str(A[i])+" ")
