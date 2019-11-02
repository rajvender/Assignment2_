print("enter num")
num = int(input())
var=0
def fun(num):
    var = 0
    while num !=0:
        num=num // 10
        var = var+1
    return var

print(fun(num))
