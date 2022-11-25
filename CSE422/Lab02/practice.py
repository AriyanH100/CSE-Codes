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
    for i in range(5):
        p=[0]*tbats
        for j in range(len(p)):
            p[j]=random.randint(0,1)
        popu.append(p)
    return popu

fit=[]
fit2=[]
def fitness(x):
    f=0
    f1=0
    for index,k in enumerate(x):
        if k==1:
            f+=runs[index]
    f1=truns-f
    fit2.append(f1)
    fit.append(abs(f1))
    return f

def select(population,fitness):
    s=fitness.index(max(fitness))
    selected=population[s]
    population.pop(s)
    fitness.pop(s)
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

def mutation(a):
    m=a.copy()
    l=len(m)
    x=random.randint(0,l-1)
    if m[x]==0:
        m[x]=1
    else:
        m[x]=0
    return m

def genetic():
    p=population()
    for i in p:
        fitness(i)
    for i in range(2):
        print(p)
        print(fit)
        print(fit2)
        s1=select(p,fit)
        s2=select(p,fit)
        # print("s1",s1)
        # print("s2",s2)
        ch1,ch2=crossover(s1,s2)
        # print("ch1",ch1)
        # print("ch2",ch2)
        p.append(ch1)
        p.append(ch2)
        f1=fitness(ch1)
        f2=fitness(ch2)
        if f1==truns:
            return ch1
        if f2==truns:
            return ch2
        cm1=mutation(ch1)
        cm2=mutation(ch2)
        # print("cm1",cm1)
        # print("cm2",cm2)
        p.append(cm1)
        p.append(cm2)
        f3=fitness(cm1)
        f4=fitness(cm2)
        if f3==truns:
            return cm1
        if f4==truns:
            return cm2


print(genetic())