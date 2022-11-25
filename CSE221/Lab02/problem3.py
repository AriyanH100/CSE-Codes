with open("input3.txt","r") as f:
    content=f.read()

n=int(content[0])
lst=list(content.split("\n"))
lst1=list(lst[1].split(" "))
B=[]  #Contains the IDs 
for i in lst1:
        B.append(int(i))
lst2=list(lst[2].split(" "))
A=[]  #Contains the marks
for i in lst2:
        A.append(int(i))

x=dict()  #Dictionary to store marks with corresponding IDs

for i in range(len(A)):
    if A[i] in x:
        x[A[i]].append(B[i])
    else:
        x[A[i]]=[B[i]]

#Insertion sort
for i in range(n-1):
    temp=A[i+1]
    k=i
    j=i
    while j>=0:
        if A[j]>temp:
            A[j+1]=A[j]
        else:
            break
        j-=1
    A[j+1]=temp

C=[]  #Array to store non-duplicate marks
for i in A:
    if i not in C:
        C.append(i)

with open("output3.txt","w") as g:
    for i in range(len(C)-1,-1,-1):
        for j in x[C[i]]:
            g.write(str(j)+" ")


