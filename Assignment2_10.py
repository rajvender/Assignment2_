print("enter num")
num = int(input())
def fun(num):
    var = 0
    while num !=0:
          var=var+int(num % 10)
          num=num/10
    return var

print(fun(num))
