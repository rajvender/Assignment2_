print("enter num")
num=int(input())

def fun(a):
    for i in range(num):
        var=1
        for j in range(0, i+1):
            print(var,end=" ")
            var=var+1
        print("\r")
fun(num)