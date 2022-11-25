#Name: Ariyan Hossain  ID:20101099  Sec:12
#Task1
class Node:
    def __init__(self,value,next,prev):
        self.value=value
        self.next=next
        self.prev=prev

class DoublyList:
    head=None
    #Creating constructor
    def __init__(self,a):  #Task2,1a
        self.head=Node(None,None,None)
        self.head.next=self.head
        self.head.prev=self.head
        tail=None
        for i in range(0, len(a)):  
            if i==0:
                newNode = Node(a[i],None,None)
                newNode.next=self.head.next
                newNode.prev=self.head
                self.head.next=newNode
                newNode.next.prev=newNode
                tail=newNode
            else:
                newNode = Node(a[i],None,None)
                newNode.next=self.head
                newNode.prev=tail
                tail.next=newNode
                newNode.next.prev=newNode
                tail=newNode

#Task2,2
    def showList(self):  
        n=self.head.next
        if n is self.head:
            print("Empty list")
        else:
            while n is not self.head:
                print(n.value)
                n=n.next

#Task2,3 & 4    
    def insert(self, newElement, index=None):  
        if (index==None):
            c=0
            n=self.head.next
            while n is not self.head:
                if (n.value==newElement):
                    c=1
                    print("The key already exists")
                    break
                else:    
                    n=n.next
            if c==0:
                newNode=Node(newElement,None,None)
                n=self.head.next
                while n is not self.head.prev:
                    n=n.next
                n.next=newNode
                newNode.next=self.head
                newNode.prev=n
        else:
            count=0
            n=self.head.next
            while n is not self.head:
                count=count+1
                n=n.next
            if (index<0 or index>count):
                raise Exception("Invalid index")
            newNode=Node(newElement,None,None)
            n=self.head
            for i in range(-1,index-1,1):
                n=n.next
            pred=n
            newNode.next=pred.next
            newNode.prev=pred
            pred.next.prev=newNode
            pred.next=newNode

#Task2,5    
    def remove(self, index):  
        count=-1
        n=self.head.next
        while n is not self.head:
            count=count+1
            n=n.next
        if (index<0 or index>count):
            raise Exception("Invalid index")
        n=self.head
        for i in range(-1,index-1,):
            n=n.next
        pred=n
        removedNode=pred.next
        pred.next=removedNode.next
        removedNode.next.prev=pred
        removedNode.value=None
        removedNode.next=None

#Task2,6
    def removeKey(self,deletekey):
        n=self.head.next
        while n is not self.head:
            if (n.value==deletekey):
                a=n.value
                n.value=None
                return a
            n=n.next 


lst = DoublyList([1,2,3,4])
