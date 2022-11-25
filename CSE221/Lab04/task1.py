import heapq

def Dijkstra(graph,source,N):
    dist=[0]*N
    visited=[0]*N
    for v in graph:
        dist[int(v)-1]=10000
        visited[int(v)-1]=False
    dist[int(source)-1]=0
    Q=[]
    for v in graph:
        Q.append((dist[int(v)-1],v))
    heapq.heapify(Q)
    while Q:
        u=heapq.heappop(Q)
        u=u[1]
        if visited[int(u)-1]:
            continue
        visited[int(u)-1]=True
        x=graph[u]
        for i in range(0,len(x),2): 
            alt=dist[int(u)-1]+int(x[i+1])
            v=x[i]
            if alt<dist[int(v)-1]:
                dist[int(v)-1]=alt
                heapq.heappush(Q,(dist[int(v)-1],v))
    return(dist[N-1])

f=open("input1.txt","r")
s=f.readline()
d=int(s)
output=[]
for i in range(d):
    s=f.readline()
    N=int(s[0])
    M=int(s[2])
    if M==0:
        output.append('0')
        continue
    graph={}
    for j in range(M):
        t=f.readline()
        l=t
        val=list(l.split())
        print(val)
        if val[0] in graph:
            graph[val[0]].append(val[1])
            graph[val[0]].append(val[2])
        else:
            graph[val[0]]=val[1:]
        if val[1] in graph:
            graph[val[1]].append(val[0])
            graph[val[1]].append(val[2])
        else:
            graph[val[1]]=[val[0]]
            graph[val[1]].append(val[2])

    output.append(str(Dijkstra(graph,'1',N)))

f.close()   
    
with open("output1.txt","w") as g:
    for i in output:
        g.write(i+"\n")
