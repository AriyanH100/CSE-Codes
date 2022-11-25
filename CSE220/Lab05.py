#Task01
def fact(num):
  if num == 0:
    return 0
  elif num == 1:
    return 1
  else:
    return num*fact(num-1)

#Task02
def fibo(num):
    if num==0 or num==1:
        return num
    return fibo(num-1)+fibo(num-2)

#Task03
def printArray(n):
    if len(n) == 0:
        return ''              
    else:
        print(n[0])               
        return printArray(n[1:]) 

#Task04
def dec2bin(num):
    if num > 1:
        dec2bin(num//2)
    print(num % 2,end = '')
dec2bin(5)

#Task05
def power(m,n):
    if n==1:
        return m
    else:    
        return power(m,n-1)*m

#Task06
def sumElement(head):
    if head.next==None:
        return head.value
    else:    
        return head.value + sumElement(head.next)

#Task07
def reverse(head):
    if head==None:
        return 
    reverse(head.next) 
    print(head.value)
