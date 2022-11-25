with open("task1_input.txt","r") as f:
    s=f.readline()
    n=int(s)
    arr=[]
    for line in f:
        l=line
        val=list(map(int,l.split()))
        arr.append(val)

def sortSecond(val):
    return val[1]

arr.sort(key=sortSecond)

selected=[]

f=arr[0][1]
x=arr.pop(0)
selected.append(x)
count=1

for i in range(len(arr)):
    if arr[i][0]>=f:
        count+=1
        f=arr[i][1]
        selected.append(arr[i])

with open("task1_output.txt","w") as g:
    g.write(str(count))
    g.write('\n')
    for i in selected:
        for j in i:
            g.write(str(j)+" ")
        g.write('\n')