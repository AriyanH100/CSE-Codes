with open("input1.txt","r") as f:
    content=f.read()
    n=int(content[0])
    lst=list(content.split("\n"))
    lst1=list(lst[1].split(" "))
    arr=[]
    for i in lst1:
            arr.append(int(i))

def bubbleSort(arr):
    for i in range(len(arr)-1):
        bestcase=True  #This variable checks if it is best case
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1] :
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
                bestcase=False  #If there is any swapping, this is not a base case
        if bestcase==True:  #Directly returns the array after the first loop since all numbers are already sorted
            return arr
    return arr  

bubbleSort(arr)

with open("output1.txt","w") as g:
    for i in arr:
        g.write(str(i)+" ")

