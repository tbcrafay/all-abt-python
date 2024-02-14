def duplicate_list(original_list,num_of_copies):
    
    duplicated_list = []
    for i in range(num_of_copies):
        
        duplicated_list.append(original_list)
    return duplicated_list

original_list = [1,2,3,4,5]
num_of_copies = 3
duplicate_list = duplicate_list(original_list,num_of_copies)


print("Duplicated lists:")
for i in duplicate_list:
    print(i)
    
    