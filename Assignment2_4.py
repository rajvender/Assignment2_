print("enter number ")
number=int(input())
def fun(inputnum):
    num=1
    for i in range(number, 1, -1):
            if number%i==0:
               num=num+i
    return num
print("addition of all the factors is ",fun(number))