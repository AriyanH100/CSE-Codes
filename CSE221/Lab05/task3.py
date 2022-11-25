with open("task3_input.txt","r") as f:
    s=f.readline()
    n=int(s)
    t=f.readline()
    act=list(map(int,t.split()))
    call=f.readline()

act.sort()
stack=[]
index=0
sequence=[]
Jackhours=0
jillhours=0

for c in call:
    if c=="J":
        stack.append(act[index])
        sequence.append(act[index])
        Jackhours+=act[index]
        index+=1
        
    elif c=="j":
        x=stack.pop()
        sequence.append(x)
        jillhours+=x

with open("task3_output.txt","w") as g:
    for i in sequence:
        g.write(str(i))
    g.write("\n")
    g.write("Jack will work for "+str(Jackhours)+" hours"+"\n")
    g.write("Jill will work for "+str(jillhours)+" hours")
