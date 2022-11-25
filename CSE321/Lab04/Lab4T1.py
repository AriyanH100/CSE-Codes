print("Enter no of process:")
n=int(input())
arrival_time=[]
burst_time=[] 
complete_time=[0]*n 
turnaround_time=[0]*n 
waiting_time=[0]*n
burst_remaining=[]
f=[0]*n #checks process is completed or not
st=0   #system time
tot=0  #no. of completed processes

for i in range(n):
    print("Enter Arrival Time of Process",i+1)
    arrival_time.append(int(input()))
    print("Enter Burst Time of Process",i+1)
    burst_time.append(int(input()))

burst_remaining=burst_time.copy()  #initially burst remaining = burst time

while(True):
    c=n
    minm=999
    if tot==n:  #if total no. of processes = completed processes
        break
    for i in range(n):
        if(arrival_time[i]<=st and f[i]==0):
            if burst_remaining[i]<minm:
                minm=burst_remaining[i]
                c=i
            if burst_remaining[i]==minm:
                if(arrival_time[i]<arrival_time[c]):  #when both have same burst_remanining, we take the process that came first
                    minm=burst_remaining[i]
                    c=i
    if c==n:  #no process arrival time <= starting time
        st+=1
    else:
        burst_remaining[c]=burst_remaining[c]-1
        st+=1
        if(burst_remaining[c]==0):
            complete_time[c]=st
            turnaround_time[c]=complete_time[c]-arrival_time[c]
            waiting_time[c]=turnaround_time[c]-burst_time[c]
            f[c]=1
            tot+=1
        
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