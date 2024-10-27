def merge_two_list(list1, list2):
    list1.extend(list2)
    list1.sort()
    
    return list1

print(merge_two_list([1, 3, 5], [2, 2, 9]))