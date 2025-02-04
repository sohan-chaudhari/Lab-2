
def count(str):
    no_of_alfa=0
    no_of_digit=0
    for char in str:
        if char.isalpha():
            no_of_alfa+=1
        if char.isdigit():
            no_of_digit+=1
    print("number = ",no_of_digit,"ALFABET=",no_of_alfa)        

str=input("enter the str :")
count(str)