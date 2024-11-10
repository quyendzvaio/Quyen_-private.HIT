def build_matrix(a, n, m):  
    k = len(a)  
    if n * m > k:  
        return "Không thể xây dựng ma trận."  
    
    matrix = []  
    index = 0  
    
    for i in range(n):  
        row = []  
        for j in range(m):  
            row.append(a[index])  
            index += 1  
        matrix.append(row)  
        
    return matrix  

a = [1, 2, 4, 3, 5, 4, 3, 6, 1, 4, 2, 7, 4, 3, 4, 8, 7, 6]  

n = int(input("Nhập số dòng n: "))  
m = int(input("Nhập số cột m: "))  

result = build_matrix(a, n, m)  
print(result)  

if isinstance(result, list):  
    print("[", end="")  
    for i in range(len(result)):  
        print("[", end="")  
        print(", ".join(map(str, result[i])), end="")  
        print("]", end="")  
        if i < len(result) - 1:  
            print(",", end=" ")  
    print("]")