def main():
    print("enter numbre of star")
    a=int(input())
    for i in range(a):
        for j in range(a):
            print("*",end=" ")
        print("")

if __name__==('__main__'):
    main()
