import random

f=open("input.txt","r")
line1=list(f.readline().split(' '))
tbats=int(line1[0])
truns=int(line1[1])
batsman=[]
runs=[]
for i in range(tbats):
    line=list(f.readline().split(' '))
    batsman.append(line[0])
    runs.append(int(line[1].strip()))


def population():
    popu=[]
    for i in range(10):
        p=[0]*tbats
        for j in range(len(p)):
            p[j]=random.randint(0,1)
        popu.append(p)
    return popu

fit=[]
fit2=[]
def fitness(x):
    f=0
    for index,k in enumerate(x):
        if k==1:
            f+=runs[index]
    fit2.append(abs(f-truns))
    fit.append(f)
    return f

def select(population,fitness,fitness2):
    s=fitness2.index(min(fitness2))
    selected=population[s]
    population.pop(s)
    fitness.pop(s)
    fitness2.pop(s)
    return selected

def crossover(x,y):
    l=len(x)
    split=random.randint(0,l-1)
    tempx1=x[:split+1]
    tempx2=x[split+1:]
    tempy1=y[:split+1]
    tempy2=y[split+1:]
    ch1=tempx1+tempy2
    ch2=tempy1+tempx2
    return ch1,ch2

def mutation(a,f):
    m=a.copy()
    l=len(m)
    if f>truns:
        while True:
            x=random.randint(0,l-1)
            if m[x]==1:
                m[x]=0
                break
    else:
        while True:
            x=random.randint(0,l-1)
            if m[x]==0:
                m[x]=1
                break

    return m

def genetic():
    p=population()
    for i in p:
        fitness(i)
    for i in range(len(fit2)):
        if fit2[i]==0:
            return p[i]
    for i in range(5000):
        s1=select(p,fit,fit2)
        s2=select(p,fit,fit2)
        ch1,ch2=crossover(s1,s2)
        p.append(ch1)
        p.append(ch2)
        f1=fitness(ch1)
        f2=fitness(ch2)
        if f1==truns:
            return ch1
        if f2==truns:
            return ch2
        cm1=mutation(ch1,f1)
        cm2=mutation(ch2,f2)
        p.append(cm1)
        p.append(cm2)
        f3=fitness(cm1)
        f4=fitness(cm2)
        if f3==truns:
            return cm1
        if f4==truns:
            return cm2
    return -1

print(batsman)
gen=genetic()
if gen==-1:
    print(gen)
else:
    for i in gen:
        print(i,end="")