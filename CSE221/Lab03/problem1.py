f=open("input1.txt","r")
s=f.readline()
d=int(s)
dict={}
for line in f:
    l=line
    val=list(l.split())
    dict[val[0]]=val[1:]

print(dict)
f.close()