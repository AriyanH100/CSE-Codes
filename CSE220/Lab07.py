#Name:Ariyan Hossain ID:20101099 Sec:12

#Task1
class KeyIndex:
    def __init__(self,a):
        self.a=a
        self.neg=0  #checking if there is any negative number in the list
        for i in self.a:
            if i<0:
                self.neg=1
                break
        if self.neg==0:
            #finding maximum
            maxm=self.a[0]
            for i in range(len(self.a)):
                if self.a[i]>maxm:
                    maxm=self.a[i]
            #creating new list and adding 1
            self.k=[0]*(maxm+1)
            for i in range(len(self.a)):
                self.k[self.a[i]]+=1
        else:
            #finding most negative
            minm=self.a[0]
            for i in range(len(self.a)):
                if self.a[i]<minm:
                    minm=self.a[i]
            self.x=minm*(-1)
            #making all element positive by adding x to each element
            for i in range(len(self.a)):
                self.a[i]+=self.x
            #finding maximum
            maxm=self.a[0]
            for i in range(len(self.a)):
                if self.a[i]>maxm:
                    maxm=self.a[i]
            #creating new list and adding 1
            self.k=[0]*(maxm+1)
            for i in range(len(self.a)):
                self.k[self.a[i]]+=1

    def search(self,val):
        #for positive
        if self.neg==0:
            if val<0 or val>len(self.k)-1:  #checking if the index exists or not
                return False
            else:
                if self.k[val]!=0:  #checking if the value exists or not
                    return True
                else:
                    return False
        #for negative
        else:
            if val+self.x<0 or val+self.x>len(self.k)-1:  #checking if the index exists or not
                return False
            else:
                if self.k[val+self.x]!=0:  #checking if the value exists or not
                    return True
                else:
                    return False
    def sort(self):
        #for positive
        if self.neg==0:
            ind=0  #index of the list that was originally given
            for i in range(len(self.k)):
                if self.k[i]!=0:
                    for j in range(self.k[i]):
                        self.a[ind]=i  #making the index of list k the element of list a
                        ind+=1
        #for negative
        else:
            ind=0  #index of the list that was originally given
            for i in range(len(self.k)):
                if self.k[i]!=0:
                    for j in range(self.k[i]):
                        self.a[ind]=i-self.x  #making the index-x(to get the original value) of list k the element of list a
                        ind+=1
        return(self.a)

#Tester Class
# b=KeyIndex([-9,0,2,3,2,1,-3])
# print(b.search(0))
# print(b.sort())


#Task2
def hashtable(a):
    lst=[0]*9  #creating a hashtable of length 9 
    vowel=['A','E','I','O','U']
    digit=['0','1','2','3','4','5','6','7','8','9']
    for j in a:
        
        #hash function
        sumdigits=0
        count=0
        for i in j:
            if i in digit:
                sumdigits=sumdigits+int(i)
            elif i not in vowel:
                count+=1       
        h=(count*24+sumdigits)%9  #index of the hashtable
        
        #linear probing
        index=h
        while True:
            if lst[index]==0:
                lst[index]=j
                break
            else:
                index=(index+1)%9
    print(lst)

#Tester Class
hashtable(['12P', 'E10', 'EE2', 'PP9', 'PO9', 'T2T', 'SS3', 'UV1', 'TT4'])
