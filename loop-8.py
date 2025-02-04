def fact(num):
    if num==0 or num==1:
        return 1
    sum=1
    for i in range(1,num+1):
        sum=sum*i
    return sum

num=int(input("enter the number : "))
factorial=fact(num)

print(f"your factorial is {factorial}.")