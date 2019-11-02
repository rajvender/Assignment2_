
print("enter number")
prime=int(input())
def fun(a):
    for i in range(prime-1, 1, -1):
            if prime%i==0:
                print("number is not prime number")
                break
    else:
        print("number is prime number")
fun(prime)