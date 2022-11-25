with open("input2.txt",'r') as f:
    X=f.readline()
    X=X.strip('\n')
    Y=f.readline()
    Y=Y.strip('\n')
    Z=f.readline()
    Z=Y.strip('\n')

def Lcs(X,Y,Z):
    
    m=len(X)
    n=len(Y)
    o=len(Z)

    c=[[[None for k in range(o+1)] for j in range(n+1)] for i in range(m+1)]
    t=[[[None for k in range(o+1)] for j in range(n+1)] for i in range(m+1)]
    
    for i in range(m+1):
        for j in range(n+1):
            for k in range(o+1):
                if i==0 or j==0 or k==0:
                    c[i][j][k]=0
                    t[i][j][k]=None
                elif (X[i-1] == Y[j-1] and X[i-1] == Z[k-1]):
                    c[i][j][k] = c[i-1][j-1][k-1] + 1
 
                else:
                    c[i][j][k] = max(max(c[i-1][j][k],c[i][j-1][k]),c[i][j][k-1])
    
    with open("output2.txt",'w') as g:
        g.write(str(c[m][n][o]))

Lcs(X,Y,Z)