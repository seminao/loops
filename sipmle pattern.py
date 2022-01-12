# i=1
# while i<=7:
#     print(i*"#")
#     i=i+1
    

# nested loops
# n=int(input("enter the number"))
# i=n
# while i>=1:
#     j=1   
#     while j<=n:
#         print(i,end=" ") 
#         j=j+1
#     i=i-1
#     print()

# a=int(input("enter the number"))
# i=a
# while i>=1:
#     j=1
#     while j<=i:
#         print(i,end=" ")
#         j=j+1
#     i=i-1
#     print()

num=int(input("enter the number"))
row=0
while row<num:
    star=row+1
    while star>0:
        print("*",end=" ")
        star-1
    row=row+1
    print()