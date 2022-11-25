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
printed=[]

def DFS_VISIT(graph,node):
    visited[int(node)-1]=1
    printed.append(node)
    for node in graph[node]:
        if visited[int(node)-1]==0:
            DFS_VISIT(graph,node)

def DFS(graph,endPoint):
    for node in graph:
        if visited[int(node)-1]==0:
            DFS_VISIT(graph,node)
    for i in printed:
        print(i,end=" ")
        if i==endPoint:
            break

DFS(graph,'12')