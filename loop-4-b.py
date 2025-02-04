def number(num):
    if num<=1:
        print("the num is not perfect")
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum +=i
    if sum==num:
        print(f"{num} is the perfect number")     

    else:
        print(f"{num} is not perfect number")       

num=int(input("enter a number : "))
number(num)