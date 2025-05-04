# def meet(n):
#     return n**n


# print(meet(2))


# def meet(n1,n2):
#     return n1+n2


# print(meet(2,4))

# def multiply(p1, p2):
#     return p1 * p2


# print(multiply(8, 5))
# print(multiply('a', 5))
# print(multiply(5, 'a'))

# import math



# def findArea(r):
#     area=math.floor(math.pi * (r**r))
#     circumference=math.floor(2 * math.pi * r)
#     return area,circumference



# print(findArea(5))


# cube=lambda x:x**3

# print(cube(3))




# def sum_all(*args):
#     print(args)
#     for i in args:
#         print(i * 2)
#     return sum(args)

# print(sum_all(1, 2, 3))
# # print(sum_all(1, 2, 3, 4, 5))
# # print(sum_all(1, 2, 3, 4, 5, 6, 7, 8




# def factorial(n):
#     if n==0:
#         return 1
#     else:
#        return n * factorial(n-1)


# print(factorial(5))



def print_kargs(**kwargs):
    print(kwargs)

    for key,value in kwargs.items():
        print(key,value)


print_kargs(name="hashim",power="lazer")    