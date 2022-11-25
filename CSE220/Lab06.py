#Name:Ariyan Hossain ID:20101099 Sec:12

#Task01
def selection_sort(a,i,j):
  size=len(a)
  if i==size and j==size:
    return -1
  if i<size-1:
    minm=i
    while j<size:
      if a[j]<a[minm]:
        minm=j
      j+=1
    if minm!=i:
      temp=a[i]
      a[i]=a[minm]
      a[minm]=temp
    selection_sort(a,i+1,j+1)

#Task02
def insertion_sort(a,i):
  size=len(a)
  if i==size:
    return -1
  if i<size:
    j=i-1
    temp=a[i]
    while j>=0 and temp<a[j]:
      a[j+1]=a[j]
      j=j-1
    a[j+1]=temp
    insertion_sort(a,i+1)

#Task03
class Node:
    def __init__(self,value,next):
        self.value=value
        self.next=next

class SinglyLinkedList:
    head=None
    #Creating constructors
    def __init__(self,a):  
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

    def showList(self):  
        n=self.head
        if self.head is None:
            print("Empty list")
        else:
            while n is not None:
                print(n.value)
                n=n.next

    def sll_bubble_sort(self):
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

#Task04
    def sll_selection_sort(self): 
        n=self.head
        while n is not None: 
            minm=n
            nxt=n.next
            while nxt is not None:
                if(minm.value>nxt.value):
                    minm=nxt      
                nxt=nxt.next
            temp=n.value
            n.value=minm.value
            minm.value=temp
            n=n.next    

#Task05
class Node1:
    def __init__(self,value,next,prev):
        self.value=value
        self.next=next
        self.prev=prev

class DoublyLinkedList:
    head=None
    #Creating constructors
    def __init__(self,a=None):  
        self.head = None
        tail = None
        for i in range(0, len(a)):  
            newNode = Node1(a[i], None,None)
            if(self.head == None):
                self.head = newNode
                tail = newNode
            else:
                tail.next = newNode
                newNode.prev=tail
                tail = newNode

    def showList(self):  
        n=self.head
        if self.head is None:
            print("Empty list")
        else:
            while n is not None:
                print(n.value)
                n=n.next
    
    def dll_insertion_sort(self): 
      n=self.head
      while n is not None: 
          m=n.prev
          while m is not None:
              if(m.value>m.next.value):
                  temp=m.value
                  m.value=m.next.value
                  m.next.value=temp
              else:
                  break
              m=m.prev
          n=n.next

#Task06
def binary_search(a,val,L,R):
  M = (L+R)//2
  if(val == a[M]):
    return M
  elif (val > a[M]):
    return binary_search(a,val,M+1,R)
  else:
    return binary_search(a,val,L,M-1)

#Task07
dict = {}
def fibo(n):
  if(n == 0 or n==1):
    return n
  if n in dict: 
    return dict[n]  
  else:
    dict[n]=fibo(n-1)+fibo(n-2)
    return dict[n] 

#--------------------------Tester Class----------------------------#
#Task01
# a=[5,3,2,7,8]
# i=0
# j=i+1
# selection_sort(a,i,j)
# print(a)

#Task02
# a=[5,3,2,7,8]
# i=1
# insertion_sort(a,i)
# print(a)

#Task03
# a=[5,3,2,7,8]
# lst=SinglyLinkedList(a)
# lst.sll_bubble_sort()
# lst.showList()

#Task04
# a=[5,3,2,7,8]
# lst=SinglyLinkedList(a)
# lst.sll_selection_sort()
# lst.showList()

#Task05
# a=[5,3,2,7,8]
# lst=DoublyLinkedList(a)
# lst.dll_insertion_sort()
# lst.showList()

#Task06
# a=[1,2,3,4,5]
# L=0
# R=len(a)
# print(binary_search(a,5,L,R))

#Task07
# print(fibo(3))