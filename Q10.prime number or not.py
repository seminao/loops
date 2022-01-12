# num=int(input("enter the number"))
# i=2
# while i<=num:
#     a=2
#     c=0
#     while a<i:
#         if i%a==0:
#             c=c+1
#         a=a+1
#     if c==0:
#         print(i)
#     i=i+1

num=int(input("enter the number"))
i=1
n=0
while i<=num:
    if num%i==0:
        n=n+1
    i=i+1
if n==2:
    print(num,"is prime number")
else:
    print("not prime number")
