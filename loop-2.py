def table(num):
    print("your tablr is : \n")
    for i in range(1,11,1):
        print(num,"*" , i , "=" ,num*i)

num=int(input("enter the number : "))
table(num)