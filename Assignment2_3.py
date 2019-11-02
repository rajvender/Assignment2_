print("enter the number for which factorial calculated")
inputnumber = int(input())
def fun(a):
    num=1
    for i in range (inputnumber):
           num=num*(i+1)
    return num


print(fun(inputnumber))