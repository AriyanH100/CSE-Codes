#Name: Ariyan Hossain ID: 20101099 Sec: 12

#Task1
class ArrayBasedStack:
    stack=[]
    pointer=-1
    def push(self,element):
        self.stack=self.stack+[element]
        self.pointer=self.pointer+1
    def peek(self):
        return(self.stack[self.pointer])
    def pop(self):
        value=self.stack[self.pointer]
        self.stack=self.stack[:-1]
        self.pointer=self.pointer-1
        return value

    def ParenthesesBalancing(self,a):
        x=1 
        j=1
        for i in a:
            #pushing into stack
            if i=="(" or i=="{" or i=="[":
                self.push(i)
            #popping out of stack and checking
            elif i==")" or i=="}" or i=="]":
                if i==")":
                    rev="("
                if i=="}":
                    rev="{"
                if i=="]":
                    rev="["    
                if len(self.stack)==0:
                    print("This expression is NOT correct.")
                    print(f"Error at character # {j}. '{i}' - not opened.")
                    x=0
                    break
                else:
                    value=self.pop()
                    if value!=rev:
                        j=1
                        for i in a:
                            if i==value:
                                break
                            j+=1
                        print("This expression is NOT correct.")
                        print(f"Error at character # {j}. '{value}' - not closed.")
                        x=0
                        break
            j+=1    
        if x!=0:
            if len(self.stack)!=0:
                print("This expression is NOT correct.")
                #pops out the last opening bracket 
                value=self.pop()
                j=1
                for i in a:
                    if i==value:
                        break
                    j+=1
                print(f"Error at character # {j}. '{value}' - not closed.")
            else:
                print("This expression is correct.")

#Task2
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class LinkedListBasedStack:
    head=None
    def push(self,data):
        if self.head==None:
            self.head=Node(data)
        else:
            newNode=Node(data)
            newNode.next=self.head
            self.head=newNode  
    def peek(self):
        return(self.head.value)
    def pop(self):
        temp=self.head
        self.head=self.head.next
        a=temp.value
        temp.value=None
        temp.next=None
        return a
    
    def ParenthesesBalancing(self,a):
        x=1
        j=1
        for i in a:
            #pushing into stack
            if i=="(" or i=="{" or i=="[":
                self.push(i)
            #popping out of stack and checking
            elif i==")" or i=="}" or i=="]":
                if i==")":
                    rev="("
                if i=="}":
                    rev="{"
                if i=="]":
                    rev="[" 
                if self.head is None:
                    print('This expression is NOT correct.')
                    print(f"Error at character # {j}. '{i}' - not opened.")
                    x=0
                    break
                else:
                    temp=self.pop()
                    if temp!=rev:
                        j=1
                        for i in a:
                            if i==temp:
                                break
                            j+=1
                        print("This expression is NOT correct.")
                        print(f"Error at character # {j}. '{temp}' - not closed.")
                        x=0
                        break
            j+=1    
        if x!=0:
            if self.head is not None:
                print("This expression is NOT correct.")
                #pops out the last opening bracket 
                value=self.pop()
                j=1
                for i in a:
                    if i==value:
                        break
                    j+=1
                print(f"Error at character # {j}. '{value}' - not closed.")
            else:
                print("This expression is correct.")

#Tester Class

# a=ArrayBasedStack()
# a.ParenthesesBalancing('1+2*(3/4)') 
# b=ArrayBasedStack()
# b.ParenthesesBalancing('1+2*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14')
# c=ArrayBasedStack()
# c.ParenthesesBalancing('1+2*[3*3+{4–5(6(7/8/9)+10)}–11+(12*8)/{13+13}]+14')
# d=ArrayBasedStack()
# d.ParenthesesBalancing('1+2]*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14')

e=LinkedListBasedStack()
e.ParenthesesBalancing('1+2*(3/4)') 
f=LinkedListBasedStack()   
f.ParenthesesBalancing('1+2*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14')  
g=LinkedListBasedStack()
g.ParenthesesBalancing('1+2*[3*3+{4–5(6(7/8/9)+10)}–11+(12*8)/{13+13}]+14')
h=LinkedListBasedStack()
h.ParenthesesBalancing('1+2]*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14')