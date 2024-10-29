import math  

def bits(a):  
    if a < 0:  
        a = -a
    if a == 0:  
        return 1
    octal_length = math.ceil(math.log(a, 8)) 
    return octal_length * 3

a = int(input("Nhập vào số a: "))  
num_bits = bits(a)  
print(f"Số lượng các bits cần thiết để biểu diễn số {a} ở dạng bát phân: {num_bits}")