# # a= int(input("Enter your first number: "))
# # b = int(input("enter your second number: "))
# # c = int(input("enter your third number: "))
# # d = int(input("enter your fourth number: "))
# # l = [a,b,c,d]

# # max = 0
# # min = a
# # for x in l:
# #     if x >= max:
# #         max = x
# #     elif x < min:
# #         min = x
# #     else:
# #         pass
# # print(f"maximun nuber : {max}")
# # # print(f'minimum number : {min}')
# # a=int(input("enter your number:"))
# # fac=1
# # for i in range(1,a+1):

# #     fac = fac*i
# # print(fac)



# '''n=int(input("enter you number :"))
# a = 0
# for x in range(2,n):
#     # print(n%x)
#     if n%x == 0:

#         a = 1
#         break
#         # print("it is not a prime number ")

#     else:
#         # print("it is a prime number")
#         pass
# if a == 1:
#     print("it is composite number")
# else:
#     print("it is a prime number")'''


# # n=int(input("enter you number :"))
# # a = 1
# # for x in range(2,n):
# #     print(n%x)
# #     if n == 1 or n == 0:
# #         print("it is neither a prime number nor a composite")
# #         break
# #     elif n%x != 0:

# #         a = 1
        
# #         # print("it is not a prime number ")

# #     elif n%x == 0 :
# #         # print("it is a prime number")
# #         a = 0
# #         break
# # if a == 0:
# #     print("it is composite number")
# # else:
# #     print("it is a prime number")

# #---------------------------Armstrong number------------------------------


# # a = input("enter you number: ")
# # def run(a):
# #     result = 0
# #     p=len(a)
# #     for x in a:
# #         result += int(x)**p
# #     if int(a) == result:
# #         print("it is Armstrong number")
# #     else:
# #         print("it is not Armstrong number")
# #     # num = int(input("Enter a number: "))
# # run(a)

# # sum = 0
# # n1 = len(str(num))
# # temp = num
# # while temp > 0:
# #    digit = temp % 10
# #    sum += digit ** n1
# #    temp //= 10

# # if num == sum:
# #    print(num,"is an Armstrong number")
# # else:
# #    print(num,"is not an Armstrong number")

# # a = int(input("enter your number: "))



# #-------------------------sum of 1+x+x**2+x**3+.....+x**n
# # a = int(input("enter the value of x: "))
# # b = int(input("Enter the value of n: "))
# # sum = 0
# # for x in range(b+1):
# #     sum += a**x
# # print(sum)

# #---------------------------
# # print(4**(1/2))
# # a = int(input())
# # sum = 0
# # for x in range(1,a):
# #     if a%x== 0:
# #         sum+=x
# #     else:
# #         pass

# # if sum == a:
# #     print("it is perfect number")


# #---------------------------lcm and hcf
# # a = int(input("enter first number: "))
# # b = int(input("enter second number: "))
# # la = []
# # lb = []
# # for x in range(2,a+1):
# #     if a%x== 0:
# #         la.append(x)
# #     else:
# #         pass

# # for x in range(2,b+1):

# #     if b%x== 0:
# #         lb.append(x)
# #     else:
# #         pass
# # lf = []
# # for i in la:
# #     if i in lb :
# #         lf.append(i)
# #     else:
# #         pass
# # if len(lf) == 0:
# #     lf.append(1)
# # print("hcf is",max(lf))
# # lcm = (a*b)/max(lf)
# # print("lcm is ", lcm)
    
# a = input("enter your text: ")
# y =['a',"e","i","o","u"]
# z=[]
# for i in range(65,90):
#     if not chr(i).lower() in y:
#         z.append(chr(i).lower())


# v = 0
# c = 0
# u =0
# l = 0

# for i in a.lower():
#     if i in y:
#         v+=1
#     elif i in z:
#         c+=1
# for ii in a:
#     if ord(ii) >= 65 and ord(ii)<=90:
#         u+=1
#     elif ord(ii) >= 97 and ord(ii)<=122:
#         l+=1
# print("the number of vowel is ",v)
# print("the number of consonants is ",c)
# print("the number of upper case is ",u)
# print("the number of lower case is ",l)



# dict = {1:["m",2],2:['b',3]}
# a = int(input("enter row: "))
# for x in range(a):
#     print(" "*(a-x),end="")
#     print("*"*x*2,end="*")
#     print()
# for i in range(1,a):
#     for j in range(a-i):
#         print(" ",end="")
#     for j in range(1,i):
#         print("*",end='')
#     for j in range(i,0,-1):
#         print("*",end="")
#     print()
