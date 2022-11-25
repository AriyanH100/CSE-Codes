f=open("input1.txt","r")
lst1=[]
for line in f:
    l=line
    lst1.append(l.split())
lst=[]
for i in lst1:
    x=len(i)-1
    for j in i:
        lst.append(j)

visited=[0]*100
def DFS(S):
    count=0
    Q=[]
    Q.append(S)
    while Q!=[]:
        n=Q.pop()
        count+=1
        visited[n]=1
        child=[]
        if n==len(lst)-1:  # for last row last index
            child=[]
        elif n>=len(lst)-x-1:  # for last row
            if lst[n+1]=="Y":
                child.append(n+1)
        elif (n-x)%(x+1)==0:  # for last column
            if lst[n+x]=="Y":
                child.append(n+x)
            if lst[n+x+1]=="Y":
                child.append(n+x+1)
        elif n%(x+1)==0:  # for first column
            if lst[n+1]=="Y":
                child.append(n+1)
            if lst[n+x+1]=="Y":
                child.append(n+x+1)
            if lst[n+x+2]=="Y":  
                child.append(n+x+2)
        else:
            if lst[n+1]=="Y":
                child.append(n+1)
            if lst[n+x]=="Y":
                child.append(n+x)
            if lst[n+x+1]=="Y":
                child.append(n+x+1)
            if lst[n+x+2]=="Y": 
                child.append(n+x+2)
        for i in range(len(child)):
            if visited[child[i]]==0:
                Q.append(child[i])
    return(count)

totalcount=[]
for i in range(len(lst)):
    if lst[i]=="Y" and visited[i]==0:
       totalcount.append(DFS(i))

print(max(totalcount))

