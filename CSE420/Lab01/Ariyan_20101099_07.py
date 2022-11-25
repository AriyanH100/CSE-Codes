with open("input.txt","r") as file:
    lines = [line.rstrip() for line in file]  #creates list for each line
    lst=[]
    for i in lines:  #creates list for each word
        lst.append(i.split(" "))
    lst1=[]
    for i in lst:
        for j in i:
            if j not in lst1:  #creates list for each word without duplication
                lst1.append(j)
    keywords=['auto','break','case','char','const','continue','default','do','double','else','enum','extern','float','for','goto','if','int','long','register','return','short','signed','sizeof','static','struct','switch','typedef','union','unsigned','void','volatile','while']
    moperators=['+','-','*','/','%','=','++','--']
    loperators=['==','!=','!','>','<','>=','<=','&&','||']
    numerical=['0','1','2','3','4','5','6','7','8','9']
    others=[',',';','(',')','{','}','[',']']

    k=[]
    m=[]
    l=[]
    n=[]
    o=[]
    e=[]

    for i in lst1:
        if i in keywords:
            k.append(i)
        elif i in moperators:
            m.append(i)
        elif i in loperators:
            l.append(i)
        elif i in numerical:
            n.append(i)
        elif '.' in i:
            n.append(i)
        elif i in others:
            o.append(i)
        else:
            e.append(i)

    print("Keywords: ",end="")
    for i in range(len(k)):
        if i==len(k)-1:
            print(k[i])
        else:
            print(k[i],end=", ")
    print("Identifiers: ",end="")
    for i in range(len(e)):
        if i==len(e)-1:
            print(e[i])
        else:
            print(e[i],end=", ")
    print("Math Operators: ",end="")
    for i in range(len(m)):
        if i==len(m)-1:
            print(m[i])
        else:
            print(m[i],end=", ")
    print("Logical Operators: ",end="")
    for i in range(len(l)):
        if i==len(l)-1:
            print(l[i])
        else:
            print(l[i],end=", ")
    print("Numerical Values: ",end="")
    for i in range(len(n)):
        if i==len(n)-1:
            print(n[i])
        else:
            print(n[i],end=", ")
    print("Others: ",end="")
    for i in range(len(o)):
        print(o[i],end="")
        

            
