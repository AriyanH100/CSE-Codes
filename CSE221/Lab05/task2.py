with open("task2_input.txt","r") as f:
    s=f.readline()
    n=int(s[0])
    m=int(s[2])
    arr=[]
    for line in f:
        l=line
        val=list(map(int,l.split()))
        arr.append(val)

def sortSecond(val):
    return val[1]

c=[]

for j in range(m):
    
    arr.sort(key=sortSecond)

    selected=[]

    f=arr[0][1]
    x=arr.pop(0)
    selected.append(x)
    count=1

    i=0
    while i<len(arr):
        if arr[i][0]>=f:
            count+=1
            f=arr[i][1]
            selected.append(arr[i])
            b=arr.pop(i)
        else:
            i+=1

    c.append(count)

total=sum(c)

with open("task2_output.txt","w") as g:
    g.write(str(total))
