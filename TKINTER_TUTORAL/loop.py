# numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
# positive_numbers = []


# for num in numbers:
#     if num > 0:
     
#        positive_numbers.append(num)


# print(positive_numbers)


# num=int(input("Please enter a number"))
# sum=0

# for n in range(num):
#     if (n%2==0):
#         sum+=n
 


# print(sum) 


# num=int(input("Please enter a number"))

# for n in range(10):
#     if (n==5):
#         print("returning")
#         continue
#     print("multiply  =",num*n)


# myStr=str(input("Enter a string : "))
# newStr=""


# strLength=len(myStr)-1

# print(strLength)

# for s in range(strLength+1):
#     newStr+=myStr[strLength-s]
 

# print(newStr)


num=5
fact=1

# while num > 0:
#     fact*=num
#     num-=1

# print(fact)    



# num=int(input("Enter number"))

# while num:
#     if num > 10:
#         num=int(input("Enter number again"))
#     else:
#          break
    


# import time

# wait_time = 1
# max_retries = 5
# attempts = 0

# while attempts < max_retries:
#     print("Attempt", attempts + 1, "- wait time", wait_time, )
#     time.sleep(wait_time)
#     wait_time *= 2
#     attempts += 1