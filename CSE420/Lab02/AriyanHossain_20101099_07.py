def emailchecker(x):
    if "@" not in  x:
        return -1
    lst=list(x.split('@'))
    a=lst[0]  #before @
    b=lst[1]  #after @
    if a == "" or b == "":  #if there is nothing before or after @
        return -1 
    if a[0].isalpha() == False:  #checking if it starts with an alphabet
        return -1
    for i in range(1,len(a)):  #checking validity of string before @ and after the first alphabet
        if a[i].isalnum() == True:  #allowing alphabets and numbers
            continue
        elif a[i] == "_" or a[i] == "-" or a[i] == ".":  #if these characters are present, the next character should be alphabet or number
            if a[i+1].isalnum() == True:
                continue
            else:
                return -1
        else:
            return -1
    for i in range(len(b)):  #checking validity of string after @ 
        if "." not in b:  #invalid if there is no "."
            return -1
        if b[i].isalnum() == True or b[i] == "-":  #allowing alphabets and numbers and "-"
            continue
        elif b[i] == ".":  #if "." is present, the next character should be alphabet or number and also "." cannot be present after "@"
            if b[i+1].isalnum() == True and i!=0:
                continue
            else:
                return -1
        else:
            return -1
    return 1


def webchecker(x):
    if x[0:4] != "www.":
        return -1
    a=x[4:]
    for i in range(len(a)):
        if "." not in a:  #invalid if there is no "."
            return -1
        if a[i].isalnum() == True:  #allowing alphabets and numbers
            continue
        elif a[i] == ".":  #if "." is present, the next character should be alphabet or number and also "." cannot be present after "www."
            if a[i+1].isalnum() == True and i!=0:
                continue
            else:
                return -1
        else:
            return -1
    return 1

with open("input.txt","r") as file:
    s=file.readline()
    n=int(s)
    a=[]
    for i in range(n):
        s=file.readline().split("\n")
        a.append(s[0])
    for i in range(len(a)):
        if emailchecker(a[i]) == 1:
            print("Email,",i+1)
        if webchecker(a[i]) == 1:
            print("Web",i+1)



    

