
print("enter a number")
num=int(input())
def fun(a):
     for i in range(num):
        for j in range(num, i, -1):
            print("* ",end="")
        print("\r")
fun(num)
