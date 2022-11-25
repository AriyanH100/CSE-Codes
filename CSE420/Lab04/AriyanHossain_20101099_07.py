with open("input.txt","r") as file:
    lines = [line.rstrip() for line in file]  
    lst=[]
    for i in lines:
        if "public" in i and "public class" not in i and "public static void main" not in i:
            lst.append(i)
    methods=[]
    returnType=[]
    for i in lst:
        if "static" in i:
            a=list(i.split(" ",3))
            methods.append(a[3])
            returnType.append(a[2])
        else:
            a=list(i.split(" ",2))
            methods.append(a[2])
            returnType.append(a[1])
print("Methods:")
for i in range(len(methods)):
    print(f"{methods[i]}, return type: {returnType[i]}")