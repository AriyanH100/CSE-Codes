with open("input.txt","r") as f:
    content=f.read()
    lst1=list(content.split("\n"))
    output=[]
    count=0
    odd=0
    even=0
    noparity=0
    palindrome=0
    nonpalindrome=0
    for i in lst1:
        lst2=list(i.split(" "))
        try:
            num=int(lst2[0])        
        except:
            num=float(lst2[0])
        if lst2[1]==(lst2[1])[::-1]:
            p=1
        else:
            p=0
        if type(num)==float:
            noparity+=1
            x=lst2[0]+" cannot have parity and "
        elif num%2==0:
            even+=1
            x=lst2[0]+" has even parity and "
        elif num%2!=0:
            odd+=1
            x=lst2[0]+" has odd parity and "
        if p==1:
            palindrome+=1
            b=x+lst2[1]+" is a palindrome"
            output.append(b)
        elif p==0:
            nonpalindrome+=1
            b=x+lst2[1]+" is not a palindrome"
            output.append(b)
        count+=1

with open("output.txt","w") as g:
    for i in range(len(output)):
        if i==len(output)-1:
            g.write(output[i])
        else:
            g.write(output[i]+"\n")
    
with open("record.txt","w") as h:
    if (100*odd)%count==0:
        h.write("Percentage of odd parity: "+str(int(odd/count*100))+"%"+"\n")
    if (100*odd)%count!=0:
        h.write("Percentage of odd parity: "+str(float(odd/count*100))+"%"+"\n")
    if (100*even)%count==0:
        h.write("Percentage of even parity: "+str(int(even/count*100))+"%"+"\n")
    if (100*even)%count!=0:
        h.write("Percentage of even parity: "+str(float(even/count*100))+"%"+"\n")
    if (100*noparity)%count==0:
        h.write("Percentage of no parity: "+str(int(noparity/count*100))+"%"+"\n")
    if (100*noparity)%count!=0:
        h.write("Percentage of no parity: "+str(float(noparity/count*100))+"%"+"\n")
    if (100*palindrome)%count==0:
        h.write("Percentage of palindrome: "+str(int(palindrome/count*100))+"%"+"\n")
    if (100*palindrome)%count!=0:
        h.write("Percentage of palindrome: "+str(float(palindrome/count*100))+"%"+"\n")
    if (100*nonpalindrome)%count==0:
        h.write("Percentage of non-palindrome: "+str(int(nonpalindrome/count*100))+"%")
    if (100*nonpalindrome)%count!=0:
        h.write("Percentage of non-palindrome: "+str(float(nonpalindrome/count*100))+"%")

        




