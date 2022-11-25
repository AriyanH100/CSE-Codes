print("Enter no of process:")
n=int(input())
print("Enter time quantam:")
tq=int(input())
arrival_time=[]
burst_time=[] 
complete_time=[0]*n 
turnaround_time=[0]*n 
waiting_time=[0]*n
burst_remaining=[]
f=[0]*n #f indicates whether processes are in ready queue or not
st=0 
tot=0
q=[]  #ready queue
q.append(0)
f[0]=1

for i in range(n):
    print("Enter Arrival Time of Process",i+1)
    arrival_time.append(int(input()))
    print("Enter Burst Time of Process",i+1)
    burst_time.append(int(input()))

burst_remaining=burst_time.copy()

while(True):   
    if tot==n:
        break    
    c=q[0]  
    q.pop(0)  #pops the first element from the ready queue
    if burst_remaining[c]-tq>0:
        burst_remaining[c]=burst_remaining[c]-tq
        st+=tq
    else:
        st+=burst_remaining[c]
        burst_remaining[c]=0
        tot+=1
        complete_time[c]=st
        turnaround_time[c]=complete_time[c]-arrival_time[c]
        waiting_time[c]=turnaround_time[c]-burst_time[c]   
    for i in range(n):
        if burst_remaining[i]>0 and arrival_time[i]<=st and f[i]==0: 
            q.append(i)  #putting the other processes into ready queue
            f[i]=1
    if burst_remaining[c]>0:
        q.append(c)  #putting the current process at the end of the ready queue if burst_remaining not 0
    if len(q)==0:
        for i in range(n):
            if burst_remaining[i]>0:
                q.append(i)
                f[i]=1
                break
           
for i in range(1,n+1):
    if i==1:
        print("Completion Time of Process",i,":",complete_time[i-1],end=", ")
    elif i==n:
        print("Process",i,":",complete_time[i-1])
    else:
        print("Process",i,":",complete_time[i-1],end=", ")

for i in range(1,n+1):
    if i==1:
        print("Turnaround Time of Process",i,":",turnaround_time[i-1],end=", ")
    elif i==n:
        print("Process",i,":",turnaround_time[i-1])
    else:
        print("Process",i,":",turnaround_time[i-1],end=", ")

for i in range(1,n+1):
    if i==1:
        print("Waiting Time of Process",i,":",waiting_time[i-1],end=", ")
    elif i==n:
        print("Process",i,":",waiting_time[i-1])
    else:
        print("Process",i,":",waiting_time[i-1],end=", ")

print("Average Turnaround Time:",sum(turnaround_time)/n)
print("Average Waiting Time:",sum(waiting_time)/n)