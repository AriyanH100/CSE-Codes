import random
import math

#Task1

inp=input("Enter your Student ID: ")
inp=inp.replace("0","8")
x=int(inp[4])
total=int(inp[7]+inp[6])
y=math.ceil(total*1.5)
s=int(inp[3])
randompoints=random.sample(range(x,y),8)

lst=[0,0,0,0,0,0,0]
for i in randompoints:
    lst.append(i)

child=[[1,2],[3,4],[5,6],[7,8],[9,10],[11,12],[13,14]]

def minimax(position,depth,alpha,beta,maximizingPlayer):
    if depth==0:
        return lst[position]
    if maximizingPlayer==True:
        maxEval=-5000
        for i in child[position]:
            eval=minimax(i,depth-1,alpha,beta,False)
            maxEval=max(maxEval,eval)
            alpha=max(alpha,eval)
            if beta<=alpha:
                break
        return maxEval
    else:
        minEval=5000
        for i in child[position]:
            eval=minimax(i,depth-1,alpha,beta,True)
            minEval=min(minEval,eval)
            beta=min(beta,eval)
            if beta<=alpha:
                break
        return minEval

result=minimax(0,3,-5000,5000,True)

print("Generated 8 random points between the minimum and maximum point limits:",randompoints)
print("Total points to win:",total)
print("Achieved point by applying alpha-beta pruning =",result)
if result>=total:
    print("The winner is Optimus Prime")
else:
    print("The Winner is Megatron")


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#Task2

shufflepoints=[]
for i in range(s):
    random.shuffle(randompoints)
    lst=[0,0,0,0,0,0,0]
    for i in randompoints:
        lst.append(i)
    result=minimax(0,3,-5000,5000,True)
    shufflepoints.append(result)

print()
print("After the shuffle:")
print("List of all points values from each shuffles:",shufflepoints)
print("The maximum value of all shuffles:",max(shufflepoints))
count=0
for i in shufflepoints:
    if i>=total:
        count+=1
print(f"Won {count} times out of 8 number of shuffles")