# #for loop structure
#a loop is used for iterating over a sequance (that is either list, tuple, a dictionary, a set or a string)
#my exampples
# fruits = ["apple", "banana", "cherry"]
# # for x in fruits:
# #   print(x)
#
# for x in "banana":
#       print(x)

#nested loop
# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]
#
# for x in adj:
#   for y in fruits:
#     print(x, y)

#isabelas 1st example a list
#
# list_data = [1,2,3,4,5]
# for num in list_data:
#     print(num*2)
#

#embedded list

# embedded_lists = [[1,2,3],[5,2,3]]
# for data in embedded_lists:
#     print(data)
#
#loops for dictionaries
# dict_data = {1:{"name":"Bronson","money":"£0.05"},
#              2:{"name":"Masha","money":"£3.66"},
#              3:{"name":"Roscoe","money":"£1.14"}}
# #fetching key values
#
# for k in dict_data:
#     print(k)
#
# #fetching values from the dictionary
#
# for item in dict_data.values():
#     print(item)
#
# for items in dict_data.values():
#     print(items["name"])
#
#
list_data = [1,2,3,4,5]
for num in list_data:
     if num == 3:
         print("i found three")
     elif num > 3:
         print("gone too far")
     else:
         print("too soon")

         