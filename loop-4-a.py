def prime(num):
    if num==0 or num==1:
        print("number is not prime")
      
    count=0
    for i in range(2,num):
        if  num%i==0:
            count=1
         
    if count==0:
        print("the number is prime")
    elif count==1:
        print("the number is not prime")            

num=int(input("enter the number :"))
prime(num)