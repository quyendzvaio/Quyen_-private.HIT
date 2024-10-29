print("Chao mung den CLB Tin Hoc HIT")   
print("CLB Tin Hoc HIT truc thuoc Khoa CNTT - '10 diem'")  

my_string = "CLB Tin Hoc HIT truc thuoc Khoa CNTT"  

uppercase_letters = ''.join(filter(str.isupper, my_string))  
print(f"Tất cả các chữ cái in hoa: {uppercase_letters}")  
 
lowercase_letters = ''.join(filter(str.islower, my_string))  
print(f"Tất cả các chữ cái thường: {lowercase_letters}")  
 
if 'CNTT' in my_string:  
    print('Yes')  
else:  
    print('No')  

swapped_case = my_string.swapcase()  
print(f"Chuỗi sau khi thay thế chữ hoa thành thường và ngược lại: {swapped_case}")