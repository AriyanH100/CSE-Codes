#Name: Ariyan Hossain, ID: 20101099, Sec: 12

#Task01

def shiftLeft(source,k):
    for i in range(0,len(source)-k,1):
        source[i]=source[i+k]  #left shifting
    for i in range(len(source)-k,len(source),1):
        source[i]=0  #making the rest of elements zero after shifting
    print(source)   


source=[10,20,30,40,50,60]
shiftLeft(source,3)

#Task02

def RotateLeft(source,k):
    newlist=[0]*k  #creating a list to store values that are being replaced
    for i in range(k):
        newlist[i]=source[i]  #values stored
    for i in range(0,len(source)-k,1):
        source[i]=source[i+k]  #left shifting
    a=0  #this variable iterates through newlist
    for i in range(len(source)-k,len(source),1):
        source[i]=newlist[a]  #bringing back and rotating the elements
        a+=1
    print(source)   


source=[10,20,30,40,50,60]
RotateLeft(source,3)
    
#Task03 

def remove(source,size,idx):
    for i in range(idx,size-1,1):
        source[i]=source[i+1]  #left shifting
    source[size-1]=0  #making the last element zero after shifting
    print(source)        
        
       
source=[10,20,30,40,50,0,0]
remove(source,5,2)

#Task04

def removeAll(source,size,element):
    i=0
    while i<len(source):
        if source[i]==element:
            for a in range(i,size-1,1):
                source[a]=source[a+1]  #left shifting
            source[size-1]=0  #making the last element zero after shifting
            size-=1  #reducing the size since one element is reduced
            i=0  #resetting the value of i so that loop can start from the beginning of the list
        else:
            i+=1    
    print(source)


source=[10,2,30,2,50,2,2,0,0]
removeAll(source,7,2)
    
#Task05

def ArraySplit(n):  
    result=0  #this variable helps to print the desired outcome
    x=0  #this variable helps to sum up the left pan values
    y=0  #this variable helps to sum up the right pan values
    for i in range(len(n)):
        for a in range(i+1,len(n)):
            x=x+n[a]  #summing up right pan values
        for b in range(i+1):
            y=y+n[b]  #summing up left pan values
        if x==y:  #checking if summation of values of both sides can be balanced
            result=1   
        else:
            x=0
            y=0
    if result==1:
        print('True')
    else:
        print('False')


ArraySplit([1,1,1,2,1])        

#Task06

def ArraySeries(n):
    newlist=[0]*n*n  #creating a list of length n squared 
    b=n-1  #this variable gives the index of the element from which the elements should be added  
    for i in range(n):
        a=1  #this variable helps to add the new elements in the list  
        if i!=0:  #value of b remains same for the first loop
            b+=n  
        for j in range(b,b-i-1,-1):
            newlist[j]=a  #adding new element instead of zero 
            a+=1
    print(newlist) 


ArraySeries(5)

#Task07

def MaxBunchCount(n):
    a=1  #this variable helps to understand when the first bunch is ended
    c=1  #this variable counts the first bunch then holds the highest count
    d=1  #this variable counts the second next bunch 
    for i in range(len(n)):
        if i!=len(n)-1:
            if n[i+1]==n[i]:  #compares the adjacent elements
                if a==0: #shows first bunch has ended hence 'd' is used to count the next bunch 
                    d=d+1
                else:
                    c=c+1
            else:
                if c!=1:  #checking if first bunch has ended or not
                    a=0
                if d!=1:
                    if d>c:    
                        c=d  #storing the highest count in 'c'
                        d=1  #resetting 'd'
                    else:
                        d=1  #resetting 'd'
        if i==len(n)-1:  
            if d>c:  
                c=d  #storing the highest count in 'c'
    print(c)            


MaxBunchCount([1,2,2,3,4,4,4])

#Task08

def Repetition(n):
    newlist=[]  #list containing unique values from the given list
    for i in n:
        if i not in newlist:
            newlist=newlist+[i]
    c=0  #this variable counts the repetition of a value
    lst=[]  #list containing the counts of the repetition of each values
    for i in range(len(newlist)):
        for j in range(len(n)):
            if newlist[i]==n[j]:
                c=c+1
            if j==len(n)-1:
                if c>1:  #this condition allows only values to be stored that have repetitions 
                    lst=lst+[c]
                c=0 
    a=0  #this variable helps to print the outcome
    for i in range(len(lst)): 
        for j in range(i+1,len(lst)):
            if lst[i]==lst[j]:  #checking if there are same number of repetitions of different values
                a=1                  
    if a==0:
        print("False")
    else:
        print("True")


Repetition([4,5,6,6,4,3,6,4])

#Task09

def Palindrome(n,start,size):
    index1=start
    index2=(start+size-1)%len(n)  #this gives the last index of the circular list 
    a=[0]*size
    b=[0]*size
    for i in range(size):
        a[i]=n[index1]  #foreward adding to list 'a'
        index1=(index1+1)%len(n)  #incrementing the index of circular list 
    for j in range(size) :
        b[j]=n[index2]  #backward adding to list 'b'
        index2=index2-1
        if(index2<0):  #this condition points the index to the end of the array when it becomes negative
            index2=len(n)-1
    if a==b:  #checking if the lists are palindrome or not
        print("True")
    else:
        print("False")             
          

Palindrome([20,10,0,0,0,10,20,30],5,5) 

#Task10

def Intersection(n1,start_1,size_1,n2,start_2,size_2):
    a=[0]*size_1  
    b=[0]*size_2
    index1=start_1
    for i in range(size_1):
        a[i]=n1[index1] #converting into linear list
        index1=(index1+1)%len(n1)  #incrementing the index of circular list
    index2=start_2
    for i in range(size_2):
        b[i]=n2[index2]  #converting into linear list
        index2=(index2+1)%len(n2)  #incrementing the index of circular list
    c=0  #this variable counts the length of the new list where the common elements will be stored
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i]==b[j]:  #checking for common elements
                c+=1
                break
    newlist=[0]*c  #list to store the common elements
    x=0  #variable for index of 'newlist'
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i]==b[j]:  #checking for common elements
                newlist[x]=b[j]
                x+=1
                break            
    print(newlist)
      

Intersection([40,50,0,0,0,10,20,30],5,5,[10,20,5,0,0,0,0,0,5,40,15,25],8,7)      



