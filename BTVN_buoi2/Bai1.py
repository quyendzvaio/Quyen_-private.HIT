a = int(input("Nhập số a: "))  
b = int(input("Nhập số b: "))  

print(f"a cộng b: {a + b}")  

print(f"a trừ b: {a - b}")  
 
print(f"a nhân b: {a * b}")  

if b != 0:  
    print(f"a chia lấy nguyên b: {a // b}")  
else:  
    print("Không thể chia cho 0.")  

print(f"a mũ b: {a ** b}")  

if b != 0:  
    print(f"a chia dư b: {a % b}")  
else:  
    print("Không thể chia cho 0.")  

if a > b:  
    print("a lớn hơn b")  
elif a < b:  
    print("a nhỏ hơn b")  
else:  
    print("a bằng b")  

print(f"a AND b: {a & b}")  

print(f"a OR b: {a | b}")  

print(f"a XOR b: {a ^ b}")  

print(f"NOT a == b: {not (a == b)}")  

print(f"a dịch phải 5 bit: {a >> 5}")  

print(f"a dịch trái 6 bit: {a << 6}")  
  
binary_a = bin(a)[2:]  
reversed_binary_a = binary_a[::-1]
print(f"Hệ cơ số 2 đảo ngược của a: {reversed_binary_a}")