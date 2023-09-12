#
# #%%
# # Q1
# import math
# from math import sin, cos, tan
#
# columns = ["deg", "sin", "cos", "tan"]
# # right aligned
# columns = [column.rjust(8) for column in columns]
# print("".join(columns))
#
# degs = [i for i in range(0, 361, 30)]
# funs = [sin, cos, tan]
# for deg in degs:
#     radian_deg = math.radians(deg)
#     # calculate the sin, cos, tan value with respect to radian_deg, and change tan(pi/2), tan(3pi/2) to "undef"
#     values = [format(fun(radian_deg), ".3f") if fun(radian_deg) < 2 else "undef" for fun in funs]
#     # change "-0.000" to "0.000"
#     for i in range(len(values)):
#         if values[i] == "-0.000":
#             values[i] = "0.000"
#     values.insert(0, str(deg))
#     # right aligned
#     values = [value.rjust(8) for value in values]
#     print("".join(values))
#
#
# #%%
# # Q2
# def count_zeros(matrix):
#     """
#     :param matrix: The input matrix.
#     :return zeros_num: The number that how many zeros on both diagonal of the matrix
#     """
#     n = len(matrix[0])
#     zeros_num = 0
#     for i in range(n):
#         if matrix[i][i] == 0:
#             zeros_num += 1
#         if matrix[n-i-1][i] == 0:
#             zeros_num += 1
#     # if n is an odd and the central element is 0, then subtract 1 for repeated calculation above
#     if n % 2 == 1 and matrix[n//2][n//2] == 0:
#         zeros_num -= 1
#
#     return zeros_num
#
#
# #%%
# # Q3
# def hellow_square(a, b):
#     """
#     Print out a square of size a made of blank space with padding of width b made of the symbol #
#     """
#     n = a + 2*b
#     for i in range(n):
#         if b <= i <= a+b-1:
#             print("#"*b + " "*a + "#"*b)
#         else:
#             print("#"*n)
#
# def hellow_square2():
#     """
#     print out a square of size a made of blank space with padding of width b made of the symbol #
#     """
#     print("This is a game for printing out a square of size a made of blank space with padding of width b made of "
#           "the symbol #.")
#     print("By inputting a and b consecutively, you will get the square as described above. Otherwise, you may input "
#           "Q or q to quit the game.")
#     print("----------Game Started----------\n")
#
#     nums = "0123456789"
#     a_legal = False
#
#     while True:
#         # If "a" is legal for the condition being a non-negative number. We do not ask for a new input of "a" in any
#         # possible loop.
#         if not a_legal:
#             a = input("Please input a non-negative integer a: ")
#             # If the input is Q/q, break the loop.
#             if a in ["Q", "q"]:
#                 break
#             # To determine whether the input is legal or not.
#             # If the input string is totally consist of pure numbers, the expression "sum([_ in nums for _ in a]) ==
#             # len(a)" will hold, since the judgement "_ in nums" is always True.
#             # Or if the input string has characters other than numbers, which means these characters are not in the
#             # string "01234456789", the judgement "_ in nums" will be False for them. Thus, the sum will be smaller
#             # than len(a).
#             # The explanation above is also applicable to the block code corresponding to b.
#             elif sum([_ in nums for _ in a]) < len(a):
#                 print("Please notice that the input should be an NON-NEGATIVE INTEGER. Now please try again.")
#                 continue
#             else:
#                 a = int(a)
#                 a_legal = True
#
#         b = input("Please input a non-negative integer b: ")
#         # If the input is Q/q, break the loop.
#         if b in ["Q", "q"]:
#             break
#         elif sum([_ in nums for _ in b]) < len(b):
#             print("Please notice that the input should be an NON-NEGATIVE INTEGER. Now please try again.")
#             continue
#         else:
#             b = int(b)
#
#         print("\nHere is the square for %d and %d:" % (a, b))
#         hellow_square(a, b)
#         break
#
#     print("\n----------Game End----------")
#
# hellow_square2()
#
#
# #%%
# # Q4
# # If I have already input non-numeric values for the first 3 times, but I still have the last chance to input something
# # according the original code. And if this time I input the correct number, since "count_num" is 4, so the program will
# # still indicate I am stupid and set the height/time to 10/1. The modified version is as follows:
# input_right = 0
# count_num = 0
# while input_right == 0:
#     h_tmp = input("Enter the height:")
#     try:
#         h_val = float(h_tmp)
#         input_right = 1
#     except ValueError:
#         print("Your input should be a number")
#     count_num += 1
#
#     if input_right == 1 and h_val < 0:
#         print("Your input should be a POSITIVE number")
#         input_right = 0
#     # change the original code "if count_num > 3" into something right below
#     if input_right == 0 and count_num > 3:
#         h_val = 10
#         print("You are so stupid! I have to stop you and set the initial height as 10 meters")
#         break
# h = h_val
#
# input_right = 0
# count_num = 0
# while input_right == 0:
#     t_tmp = input("Enter the time:")
#     try:
#         t_val = float(t_tmp)
#         input_right = 1
#     except ValueError:
#         print("Your input should be a number")
#     count_num += 1
#
#     if input_right == 1 and t_val < 0:
#         print("Your input should be a POSITIVE number")
#         input_right = 0
#
#     # change the original code "if count_num > 3" into something right below
#     if input_right == 0 and count_num > 3:
#         t_val = 1
#         print("You are so stupid! I have to stop you and set the time as 1 second")
#         break
# t = t_val
#
# # do the calculations
# s = h - 9.81 * t**2 / 2
#
# # print out the results
# print("\nThe initial height of the ball is ", h, " meters")
# if s < 0:
#     print("Before", t, " seconds, the ball has already hit the ground.")
# else:
#     print("After", t, " seconds, the height is ",s, " meters")
#
#
# #%%
# # Q5
# while True:
#     a = input("Please input a REAL NUMBER of a: ")
#     try:
#         a = float(a)
#     except ValueError:
#         continue
#     else:
#         break
#
# while True:
#     b = input("Please input a REAL NUMBER of b: ")
#     try:
#         b = float(b)
#     except ValueError:
#         continue
#     else:
#         break
#
# while True:
#     c = input("Please input a REAL NUMBER of c: ")
#     try:
#         c = float(c)
#     except ValueError:
#         continue
#     else:
#         break
#
#
# print("The quadratic equation: %fx^2 + %fx + %f" % (a, b, c))
#
# delta = b**2 - 4*a*c
# if delta >= 0:
#     x1 = (-b - delta**0.5) / 2*a
#     x2 = (-b + delta**0.5) / 2*a
#     if x1 == x2:
#         print(x1)
#     else:
#         print(x1, x2)
# else:
#     real_part = -b / 2 * a
#     imaginary_part = (-delta) ** 0.5 / 2*a
#
#     if real_part == 0:
#         x1 = "%.3fi" % (imaginary_part)
#         x2 = "%.3fi" % (imaginary_part)
#     else:
#         x1 = "%.3f-%.3fi" % (real_part, imaginary_part)
#         x2 = "%.3f+%.3fi" % (real_part, imaginary_part)
#     print(x1, x2)
#
#
# #%%
# # Q6
# import numpy as np
#
# def draw_mountains(heights):
#
#     max_height = max(heights)
#     width = 2*sum(heights) - (2*len(heights)-1)
#     grid = np.zeros((max_height, width))
#     x, y = max_height-1, 0
#     grid[x, y] = 1
#     num = 1
#     for i in range(len(heights)):
#
#         while y < 2*sum(heights[:i+1])-heights[i]-num:
#             x -= 1
#             y += 1
#             grid[x, y] = 1
#         num += 1
#         while y < 2*sum(heights[:i+1])-num:
#             x += 1
#             y += 1
#             grid[x, y] = 1
#         num += 1
#     for x in range(max_height):
#         for y in range(width):
#             if grid[x, y] == 1:
#                 print("#", end="")
#             else:
#                 print(" ", end="")
#         print("\n")
#

def isValid(s):
    left = ["(", "[", "{"]
    right = [")", "]", "}"]
    memo = dict()
    for tmp in s:
        try:
            memo[tmp] += 1
        except KeyError:
            memo[tmp] = 1
    for i in range(3):
        if memo[left[i]] != memo[right[i]]:
            return False
    return True

print(isValid("()"))