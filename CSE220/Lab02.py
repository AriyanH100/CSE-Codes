#Task1
class Node:
    def __init__(self,value,next):
        self.value=value
        self.next=next

class MyList:
    head=None
    #Creating constructors
    def __init__(self,a=None):  #Task2,1a
        if a==None:
            self.head=None
        elif isinstance(a, list):  #Task2,1b
            self.head = None
            tail = None
            for i in range(0, len(a)):  
                newNode = Node(a[i], None)
                if(self.head == None):
                    self.head = newNode
                    tail = newNode
                else:
                    tail.next = newNode
                    tail = newNode
        elif isinstance(a, MyList):  #Task2,1c
            self.head = None
            copyTail = None
            n = a.head
            while n is not None:
                newNode = Node(n.value, None)
                if(self.head == None):
                    self.head = newNode
                    copyTail = newNode
                else:
                    copyTail.next = newNode
                    copyTail = newNode
                n = n.next                  
        else:
            print("Wrong datatype passed in the constructor so creating an empty MyList")
            self.head=None
       
#Task2,2           
    def showList(self):  
        n=self.head
        if self.head is None:
            print("Empty list")
        else:
            while n is not None:
                print(n.value)
                n=n.next

#Task2,3   
    def isEmpty(self):  
        if self.head is None:
            return True
        else:
            return False

#Task2,4   
    def clear(self):  
        n=self.head
        while n is not None:
            n.value=None
            temp=n.next
            n.next=None
            n=temp
        self.head=None          
 
#Task2,5 & 6   
    def insert(self, newElement, index=None):  
        if (index==None):
            c=0
            n=self.head
            while n is not None:
                if (n.value==newElement):
                    c=1
                    print("The key already exists")
                    break
                else:    
                    n=n.next
            if c==0:
                newNode=Node(newElement,None)
                n=self.head
                while(n.next):
                    n=n.next
                n.next=newNode
        else:
            count=0
            n=self.head
            while n is not None:
                count=count+1
                n=n.next
            if (index<0 or index>count):
                raise Exception("Invalid index")
            newNode=Node(newElement,None)
            if(index==0):
                newNode.next=self.head
                self.head=newNode
            else:
                n=self.head
                for i in range(index-1):
                    n=n.next
                pred=n
                newNode.next=pred.next
                pred.next=newNode
    
#Task2,7   
    def remove(self, deletekey):  
        n=self.head
        i=0
        while n is not None:
            if i==0:
                if n.value==deletekey:
                    removedNode=self.head
                    self.head=self.head.next
                    temp=removedNode
                    removedNode.value=None
                    removedNode.next=None
                    return temp                  
            else:
                if n.value==deletekey:
                    a=self.head
                    for j in range(i-1):
                        a=a.next
                    pred=a
                    removedNode=pred.next
                    pred.next=removedNode.next
                    temp=removedNode
                    removedNode.value=None
                    removedNode.next=None
                    return temp
            i=i+1
            n=n.next            

#Task3,1  
    def EvenNum(self):
        n=self.head
        self.head1=None
        tail=None
        while n is not None:
            if n.value%2==0:
                newNode=Node(n.value,None)
                if self.head1 is None:
                    self.head1=newNode
                    tail=newNode
                else:
                    tail.next= newNode
                    tail=newNode 
            n=n.next
        n=self.newhead
        while n is not None:
            print(n.value)
            n=n.next  
    
    
    # def EvenNum(self):
    #     self.new_head=None
    #     tail=None
    #     x=None  #this variable checks if there are any more even no. after detecting one even no.
    #     n=self.head
    #     while n is not None:
    #         if (n.value%2==0):
    #             if(self.new_head is None):
    #                 self.new_head=n
    #                 tail=n                    
    #             else:
    #                 tail.next = n
    #                 tail = n
    #             #checking if there are anymore even numbers 
    #             temp=n.next
    #             while temp is not None:
    #                 if (temp.value%2==0):
    #                     x=1
    #                     break
    #                 else:
    #                     x=0
    #                 temp=temp.next          
    #             #ending the new linked list if there are no more even numbers 
    #             if(x==0):
    #                 n.next=None  
    #         n=n.next
    #     #printing the new linked list containing even numbers
    #     n=self.new_head
    #     if self.new_head is None:
    #         print("Empty list")
    #     else:
    #         while n is not None:
    #             print(n.value)
    #             n=n.next          

#Task3,2
    def ElemChecker(self,elem):
        n=self.head
        x=0
        while n is not None:
            if (n.value==elem):
                x=1
            n=n.next    
        if(x==1):
            print("True")
        else:
            print("False")
                       
#Task3,3
    def reverse(self):
        n=self.head
        i=0
        while n is not None:
            if i==0:
                nextNode=n.next
                temp=nextNode.next
                nextNode.next=n
                self.head=nextNode
                n.next=None
            else:
                nextNode=temp
                temp=nextNode.next
                nextNode.next=n
                self.head=nextNode
            n=nextNode
            i+=1
            if temp is None:
                break
        #printing the reversed linked list
        n=self.head
        while n is not None:
            print(n.value)
            n=n.next 
 
#Task3,4
    def sort(self):
        count=0
        n=self.head
        while n is not None:
            count=count+1
            n=n.next
        for i in range(count):
            current=self.head
            tail=current.next
            previous=None
            while tail is not None: 
                if current.value>tail.value:
                    if previous==None:
                       previous=current.next
                       tail=tail.next
                       previous.next=current
                       current.next=tail
                       self.head=previous
                    else:   
                        temp=tail
                        tail=tail.next
                        previous.next=current.next
                        previous=temp
                        temp.next=current
                        current.next=tail
                else:           
                    previous=current
                    current=tail
                    tail=tail.next
            i=i+1
        #printing the sorted linked list
        MyList.showList(self)
           
#Task3,5
    def Sum(self):
        a=0
        n=self.head
        while n is not None:
            a=a+n.value
            n=n.next
        print(a)                     

#Task3,6
    def rotate(self,direction,k):
        if (direction=="left"):
            for i in range(k):
                oldHead=self.head
                self.head=self.head.next
                tail=self.head
                while tail.next is not None:
                    tail=tail.next
                tail.next=oldHead
                oldHead.next=None
        elif (direction=="right"):
            for i in range(k):
                oldHead=self.head
                tail=self.head
                n=self.head
                while tail.next is not None:
                    tail=tail.next
                while n is not None:
                    if n.next.next is None:
                        n.next=None 
                    n=n.next       
                self.head=tail
                tail.next=oldHead
        #printing the rotated list
        MyList.showList(self)                 

lst = MyList([5,2,6,1,4])
lst.sort()