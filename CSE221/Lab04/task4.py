import heapq

def Dijkstra(graph,source,N):
    rate=[0]*N
    for v in graph:
        rate[int(v)-1]=-10000
    rate[int(source)-1]=10000
    Q=[]
    for v in graph:
        Q.append((rate[int(v)-1],v))
    heapq._heapify_max(Q)
    while Q:
        u=heapq._heappop_max(Q)
        u=u[1]
        x=graph[u]
        for i in range(0,len(x),2): 
            alt=min(rate[int(u)-1],int(x[i+1]))
            v=x[i]
            if alt>rate[int(v)-1]:
                rate[int(v)-1]=alt
                heapq.heappush(Q,(rate[int(v)-1],v))
                heapq._heapify_max(Q)
    r=''
    for i in range(len(rate)):
        if rate[i]==-10000:
            rate[i]=-1
        if rate[i]==10000:
            rate[i]=0
        if i==len(rate)-1:
            r+=str(rate[i])
        else:
            r+=str(rate[i])+' '
    return r

f=open("input4.txt","r")
s=f.readline()
d=int(s)
output=[]
for i in range(d):
    s=f.readline()
    N=int(s[0])
    M=int(s[2])
    if M==0:
        source=f.readline()
        output.append('0')
        continue
    graph={}
    for j in range(M):
        t=f.readline()
        l=t
        val=list(l.split())
        if val[0] in graph:
            graph[val[0]].append(val[1])
            graph[val[0]].append(val[2])
        else:
            graph[val[0]]=val[1:]
        if val[1] not in graph:
            graph[val[1]]=[]
    source=f.readline()
    output.append(Dijkstra(graph,source,N))    

f.close()

with open("output4.txt","w") as g:
    for i in output:
        g.write(i+"\n")
