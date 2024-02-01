#1) Input three numbers and display the largest / smallest number.
def ls():
    a = int(input("enter first number: "))
    a
    b = int(input("enter second number: "))
    c = int(input("enter third number: "))
    lis = [a,b,c]
    lis.sort()
    print(f"The largest number is {lis[2]}")
    print(f"The smallest number is {lis[0]}")


#2) Program to Calculate Factorial of a given positive integer number.
def factorial():
    n = int(input("enter number: "))
    i = 1
    for x in range(1,n+1):
        i *= x
    print(f"factorial of {n} is : {i}")

# 3) Program to input a number and test whether it is a prime number or not.
# Ex: number N is prime if it is divisible by 1 or N else not a prime number
# if divisible by 2 to N-1.
def prime():
    N = int(input("enter number: "))
    for i in range(2,N):
        if N%i == 0:
            print(f"{N} is not prime number.")
        else:
            print(f"{N} is a prime number.")


# 4) Program to input a number and test whether it is an Armstrong number.
# An Armstrong number is an integer such that the sum of the cubes of its
# digits is equal to the number itself.
# Ex: 371 is Armstrong number as 33+73+13=371
            
            
def Armstrong():
    num = input("enter your number: ")
    num1 = list(num)
    result = 0
    for x in num1:
        result += int(x)**3
    if result == int(num):
        print(f"{num} is Armstrong number")
    else:
        print(f"{num} is not Armstrong number")


# 5) Write a program to input the value of x and n and print the sum of the
# following series:
# 1+x+x2+x3+x4+. .......... xn