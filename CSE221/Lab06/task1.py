with open("input1.txt",'r') as f:
    n1=f.readline()
    n1=n1.strip('\n')
    X=f.readline()
    X=X.strip('\n')
    Y=f.readline()
    Y=Y.strip('\n')

zone={"Y":"Yasnaya","R":"Rozhok","S":"School","P":"Pochinki","F":"Farm","M":"Mylta","H":"Shelter","I":"Prison"}

def Lcs(X,Y):
    m=len(X)
    n = len(Y)

    c=[[None]*(n + 1) for i in range(m + 1)]
    t=[[None]*(n + 1) for i in range(m + 1)]
    
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                c[i][j]=0
            elif X[i-1]==Y[j-1]:
                c[i][j]=c[i-1][j-1]+1
                t[i][j]="diagonal"
            else:
                if c[i-1][j]>=c[i][j-1]:
                    t[i][j]="up"
                else:
                    t[i][j]="left"
                c[i][j]=max(c[i-1][j], c[i][j-1])
    
    i=m
    j=n
    s=[]
    while i>0 and j>0:
        if t[i][j]=='diagonal':
            s.append(i)
            i-=1
            j-=1
        elif t[i][j]=='up':
            i-=1
        elif t[i][j]=='left':
            j-=1
    output=''
    for i in range(len(s)):
        output+=Y[s[i]-1]
    output=output[::-1]
    correctness=(c[m][n]*100)/int(n1)
    with open("output1.txt",'w') as g:
        for i in output:
            g.write(zone[i]+' ')
        g.write('\n')
        g.write('Correctness of prediction: '+str(correctness)+"%")

Lcs(X, Y)


