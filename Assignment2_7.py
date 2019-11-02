print("enter num")
num=int(input())

def fun(a):
    for i in range(1,num+1):
        for j in range(1,num+1):
            print(j,end="")
        print("\r")
fun(num)
