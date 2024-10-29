friends_info = []  
num_friends = int(input("Nhập số lượng bạn cần nhập thông tin: "))  

for i in range(num_friends):  
    print(f"\nNhập thông tin cho bạn thứ {i + 1}:")  
    
    name = input("Họ và tên: ")  
    age = input("Tuổi: ")  
    gender = input("Giới tính (Nam/Nữ): ")  
    marital_status = input("Tình trạng hôn nhân (Độc thân/Có gia đình): ")  
  
    friends_info.append({  
        name : "Họ và tên",  
        age : "Tuổi",  
        gender : "Giới tính" ,  
        marital_status : "Tình trạng hôn nhân"  
    })  
    
print("\nThông tin về các bạn HIT 15:")  
for friend in friends_info:  
    print(f"\nHọ và tên: {friend['Họ và tên']}")  
    print(f"Tuổi: {friend['Tuổi']}")  
    print(f"Giới tính: {friend['Giới tính']}")  
    print(f"Tình trạng hôn nhân: {friend['Tình trạng hôn nhân']}")