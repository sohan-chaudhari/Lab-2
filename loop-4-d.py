def number(num):
    if num<1:
        print("the number is not pellidrome")
    # number=str(num)
    # length=len(number)
    sum,rem,number1=0,0,0
    while num>0:
        rem=num%10
        sum=sum*10+rem
        num=num//10
    return sum



num=int(input("enter the number :"))      
reversed_num=number(num) 
if num==reversed_num:
    print(f"{num} is pellidrome")
else:
    print(f"{num} is not pellidrome")



    