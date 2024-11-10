def merge_lists(a, b):  
    c = []  
    n, m = len(a), len(b)  
    min_length = min(n, m)  
    
    for i in range(min_length):  
        c.append(a[i])  
        c.append(b[i])  
    
    if n > min_length:  
        c.extend(a[min_length:])  
    
    if m > min_length:  
        c.extend(b[min_length])  
    
    return c  

# Test case 1: a dài hơn b  
a1 = ['a', 'b', 'c', 'd']  
b1 = [1, 2, 3]  
print("Test case 1:", merge_lists(a1, b1))  

# Test case 2: a dài bằng b  
a2 = ['x', 'y', 'z']  
b2 = [4, 5, 6]  
print("Test case 2:", merge_lists(a2, b2))  

# Test case 3: a ngắn hơn b  
a3 = [10, 20]  
b3 = [1, 2, 3, 4, 5]  
print("Test case 3:", merge_lists(a3, b3))  

# Test case 4: a và b chứa toàn số  
a4 = [1, 3, 5]  
b4 = [2, 4, 6, 8, 10]  
print("Test case 4:", merge_lists(a4, b4))  

# Test case 5: a chứa dữ liệu là xâu ký tự còn b chứa dữ liệu số  
a5 = ['apple', 'banana', 'cherry']  
b5 = [1, 2, 3, 4, 5]  
print("Test case 5:", merge_lists(a5, b5))