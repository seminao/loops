# n=int(input("enter the number"))
# i=1
# sum=0
# while i<=n:
#     sum=sum+i
#     print(i)
#     i=i+1
# print("sum of te number=",sum)


n=int(input("enter the number"))
i=1
total=0
while i<=n:
    sum=0
    j=1
    while j<i:
        sum=sum+j
        j=j+1
    print("sum of the number=",sum)
    i=i+1
    total=total+sum
print("sum of the number is=",total)