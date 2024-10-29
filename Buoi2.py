# # a =2
# # print(a)
# # string = "Hello world"
# # print(f'len(string) = {len(string)}')
# s = int(input("s ="))
# volume = s**3
# print(volume)
# import math
# print(math.pi)


# import re
# email = "hungdeptrai@gmail.com"
# pattern = r'^\w+@\w+\.\w+$'
# if re.match(pattern, email):
#     print("Email hợp lệ")
# else:
#     print("Email không hợp lệ")

input =input("nhap vao chuoi: ")
print(any(char.isalnum() for char in input))
print(any(char.isnumeric() for char in input))

