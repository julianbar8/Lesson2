#1. Fizzbuzz using functions 2.Using functions check whether the given year is a leap year
def leap_year(year):
    year = int(input("what year u want to check?"))
    if year % 4 == 0:
        print("leap year")
    elif year % 4 == 0 and year % 100 == 0:
        print("not a leap year")
    elif year % 4 == 0 and year % 400 == 0:
        print("leap year")
leap_year(2000)

#
# #for i in range(2000,2101):
#
#     if i % 4 == 0:
#        print("leap year")
# #else:
#     print (i)

#
#
# list1 = ['abc', 'xyz', 'aba', '1221']
#
# counter = 0
# for letter in list1:
#     if letter[0] == letter[-1]:
#         counter = counter +1
# print(counter)


# # creating an empty list
# lst = []
#
# # number of elemetns as input
# n = int(input("Enter number of elements : "))
#
# # iterating till the range
# for i in range(0, n):
#     ele = int(input())
#
#     lst.append(ele)  # adding the element
#
# print(lst)
#
# total = 0
# # Iterate each element in list
# # and add them in variale total
# for ele in range(0, len(lst)):
#     total = total + lst[ele]
#
# # printing total value
# print("Sum of all elements in given list: ", total)
