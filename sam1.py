n=int(input("Enter the number of views:"))
if int(n<=100000):
    rem=int(n/1000)
    print(rem,"k")
elif(n<=10000000):
    rem=int(n/1000000)
    print(rem,"M")
elif(n<=100000000000):
    rem=int(n/1000000000)
    print(rem,"B")
else:
    print("invalid")



