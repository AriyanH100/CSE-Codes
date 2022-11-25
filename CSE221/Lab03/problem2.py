f=open("input1.txt","r")
s=f.readline()
d=int(s)
graph={}
for line in f:
    l=line
    val=list(l.split())
    graph[val[0]]=val[1:]
f.close()

visited=[0]*d
queue=[]

def BFS(visited,graph,node,endPoint):
    visited[int(node)-1]=1
    queue.append(node)
    while queue:
        m=queue.pop(0)
        print(m,end=" ")
        if m==endPoint:
            break
        for i in graph[m]:
            if visited[int(i)-1]==0:
                visited[int(i)-1]=1
                queue.append(i)

BFS(visited,graph,'1','12')