# https://github.com/darkprinx/100-plus-Python-programming-exercises-extended

# ------------___Exercise_1__--------------------

# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line.

# ans_list = []
# for x in range(2000, 3201):
#     if x % 7 == 0 and x % 5 != 0:
#         print(i, end=",")
#     else:
#         continue


# print(*(i for i in range(2000, 3201) if i % 7 == 0 and i % 5 != 0), sep=",")

# -------------------end-------------------------

# ------------___Exercise_2__--------------------
# Write a program which can compute the factorial of a given numbers.The results should be printed in a comma-separated sequence on a single line.Suppose the following input is supplied to the program: 8 Then, the output should be:40320

from functools import reduce  # used in solution c

# solution a


def factorial(input_num):
    n = int(input_num)
    sum = 1
    for x in range(1, input_num + 1):
        sum = sum * x
    print(sum)


factorial(8)

# solution b
n = int(input())
def shortFact(x): return 1 if x <= 1 else x*shortFact(x-1)


print(shortFact(n))

# solution c


def fact(acc, item):
    return acc * item


num = int(input())
print(reduce(fact, range(1, num+1), 1))
# reduce takes a callable, an iterable, and a start point. perfect!
# -------------------end-------------------------


# ------------___Exercise_3__--------------------


# -------------------end-------------------------


# ------------___Exercise_____--------------------
# -------------------end-------------------------
