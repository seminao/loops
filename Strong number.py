# n=int(input("enter the number"))
# strong=n
# sum=0
# while(n>0):
#     r=n%10
#     fact=1
#     for i in range (1,r+1):
#         fact=fact*i
#     sum=sum+fact
#     n=n//10
# if (strong==sum):
#     print("strong number")  
# else:
#     print("not a strong number")  
num=int(input("enter the number"))
s=0
strong=num
while strong>0:
    f=1
    i=1
    r=strong%10
    while i<=r:
        f=f*i
        i=i+1
    s=s+f
    strong=strong//10
if s==num:
    print("strong number")
else:
    print("not a strong number")

 

