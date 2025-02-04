def numbers(x):
    i=0
    num=str(x)
    b=len(num)
    for z in num:
       i=i+int(z)**b
    print("the total of each number at power of digits is:",i) 
    if i==int(x):
        print("this number is armstrong.")
    else:
        print("this number is not armstrong.")
        
x=int(input("enter a number : "))
numbers(x)        