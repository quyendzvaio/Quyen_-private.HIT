def find_intersection(num_list1, num_list2):  
    result = []  
    count_dict = {}  

    for num in num_list1:  
        count_dict[num] = count_dict.get(num, 0) + 1  

    for num in num_list2:  
        if num in count_dict and count_dict[num] > 0:  
            result.append(num)  
            count_dict[num] -= 1  

    return result  

# Case 1  
nums1_case1 = [1, 2, 2, 1]  
nums2_case1 = [2, 2]  
output_case1 = find_intersection(nums1_case1, nums2_case1)  
print("Output Case 1:", output_case1)  

# Case 2  
nums1_case2 = [4, 9, 5]  
nums2_case2 = [9, 4, 9, 8, 4]  
output_case2 = find_intersection(nums1_case2, nums2_case2)  
print("Output Case 2:", output_case2)