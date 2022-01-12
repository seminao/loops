# num=int(input("enter the number"))
# temp=num
# sum=0
# while temp>0:
#     digit=temp%10
#     sum=sum+digit*digit*digit
#     temp=temp//10
# if sum==num:
#     print(num,"is armstrong")
# else:
#     print(num,"is not armstrong")


# num=int(input("enter the number"))
# temp=num
# sum=0
# order=len(str(num))
# while temp>0:
#     digit=temp%10
#     sum=sum+digit**order
#     temp=temp//10
# if num==sum:
#     print(num,"is armstrong")
# else:
#     print("not armstrong")
  
n=int(input("enter te number"))
temp=n
s=0
order=len(str(n))
while temp>0:
    digit=temp%10
    s=s+digit**order
    temp=temp//10
if n==s:
    print("armstrng")
else:
    print("not")