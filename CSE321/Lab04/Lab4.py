num = int(input("Please give the number of processes : "))

pid =[]
arrival_time =[]
burst_time = []
star_time=[0]*num
complete_time = [0]*num
turnaround_time = [0]*num
waiting_time=[0]*num
f=[]
burst_remaining=[]
is_completed=[0]*num
for i in range(0,num):
    a = int(input("Please give the arrival time of Process no "+str(i+1)+" : "))
    b = int(input("Please give the burst time of Process no "+str(i+1)+" : "))
    f.append(0)
    pid.append(i+1)
    arrival_time.append(a)
    burst_time.append(b)
    burst_remaining.append(b)
current_time=0
completed=0
prev=0
while(completed!=num):
    idx = -1
    mn = 999
    for i in range(0,num):
        if(arrival_time[i]<=current_time and is_completed[i]==0):
            if burst_remaining[i]<mn:
                mn=burst_remaining[i]
                idx=i
            if burst_remaining[i]==mn:
                if(arrival_time[i]<arrival_time[idx]):
                    mn=burst_remaining[i]
                    idx=i
    if(idx!=-1):
        if(burst_remaining[idx]==burst_time[idx]):
            star_time[idx]=current_time
        burst_remaining[idx]=burst_remaining[idx]-1
        current_time+=1
        prev=current_time
        if(burst_remaining[idx]==0):
            complete_time[idx]=current_time
            turnaround_time[idx]=complete_time[idx]-arrival_time[idx]
            waiting_time[idx]=turnaround_time[idx]-burst_time[idx]
            is_completed[idx]=1
            completed+=1
print(complete_time)
print(turnaround_time)
print(waiting_time)