with open("input1.txt","r") as f:
    content=f.read()
    lst1=list(content.split("\n"))
    lst1=lst1[1:]
    lst1.remove('')
    numbers=[]
    for i in lst1:
        lst2=list(i.split(" "))
        for i in lst2:
            numbers.append(i)

n=int(content[0])  

A=[]     
for i in range(n): 
    row1=[]                                      
    for j in range(n): 
        row1.append(int(numbers[0]))
        numbers=numbers[1:]           
    A.append(row1) 


B=[]      
for i in range(n): 
    row2=[]                                    
    for j in range(n): 
        row2.append(int(numbers[0]))
        numbers=numbers[1:]          
    B.append(row2) 


C=[[0]*(n) for i in range(n)] 

for i in range(n): 
    for j in range(n): 
        for k in range(n): 
            C[i][j] += A[i][k] * B[k][j]

with open("output1.txt","w") as g:
    for r in C: 
        for x in r:
            g.write(str(x)+" ")
        g.write("\n")

    
