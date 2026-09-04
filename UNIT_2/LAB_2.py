n=int(input("Enter a number: "))
if n<1:
    print("Please enter a number greater than or equal to 1")
else:

    
        fact=1
        i=1
        for i in range (1,n):
            i=i+1
            fact=fact*i
        print ("factorial of " , n , "is " , fact )

