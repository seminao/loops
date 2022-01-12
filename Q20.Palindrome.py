n=int(input("enter the number"))
pal=n
rev=0
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
if pal==rev:
        print("is palindrome")
else:
        print("not palindrome")
# num=int(input("enter the number"))
# if num%2==0:
#     print(num+2,num+4,num+6 )
# elif num%2!=0:
#     print(num+2,num+4,num+6)
# else:
#     print("not")

