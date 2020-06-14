import Arithmetic
def main():
    print("operations on two numbers")
    print("enter the first number")
    a=int(input())
    print("enter the second number")
    b=int(input())
    print("addition is ",Arithmetic.Add(a,b))
    print("subtraction is ",Arithmetic.Sub(a,b))
    print("multiplication is ",Arithmetic.Mult(a,b))
    print("Division is",Arithmetic.Div(a,b))
    print("I did the changes") 
if __name__=='__main__':
    main()




