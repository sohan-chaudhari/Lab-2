def number(num):
    square=num**2
    
    if str(square).endswith(str(num)):
        print("the number is automorphic number")
    else:
        print("the number is not automorphic number") 


num=int(input("enter the number :"))
number(num)