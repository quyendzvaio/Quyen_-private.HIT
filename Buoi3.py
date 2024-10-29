# even_numbers = [num for num in range(1, 11) if num % 2 == 0]
# print(even_numbers)

# numbers = [1, 4, 2, 9, 7, 3]
# result = list(filter(lambda x: x > 5, numbers))
# print(result)

# numbers = [1, 2, 3, 4, 5]
# squares = list(map(lambda x: x**2, numbers))
# print(squares)

#ham zip() -> tra ve 1 tuple gom cac phan tu cung vi tri cua 2 interable: 
# l1 = [1,2,3,4]
# l2 = ['a','b','c','d']
# zip = zip(l1,l2)
# for items in zip:
#     print(items)

def giaithua(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * giaithua(n-1)
    
def TQ(n):
    result = 0 
    x =1
    while(n)
    z = lambda(x:result + (x**x)/giaithua(x))
    if 