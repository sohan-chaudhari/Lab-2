#print Fibonacci series till given number
def numbers(num):
    if num==1:
       print(1)
    if num>=2:
        print(1,1,end=" ")
    sum,a,b=0,1,1
    for i in range(3,num+1):
        sum=a+b
        a=b
        b=sum
        print(sum,end=" ")
num=int(input("enter the number :"))
sum=numbers(num)

