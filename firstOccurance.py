n=int(input("Enter the number of elements : "))
a=[]
for x in range(n):
    c=int(input("Enter the element : "))
    a.append(c)
print("The elements are : " ,a)


def checkSame(a,n):
    least=0
    diff=999
    for x in range(n):
        for y in range(x+1,n):
            if a[x]==a[y]:
                if (x-y)<diff:
                    least=a[x]
                    diff=y-x
    return least

                

c=checkSame(a,n)
if c:
    print("First occured duplicate element : ",c)
else:
    print("No duplicate elements found")