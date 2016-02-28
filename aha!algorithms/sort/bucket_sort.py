'''
Created on 2016年1月12日
# encoding: utf-8
@author: tcliu
'''

from random_list import RandomList
R = RandomList(10, 100)
lst = R.gen()

#lst = [1, 3, 5, 3, 9]
def bucket_sort(lst = []):
    sorted_list = []
    lenth = max(lst) - min(lst) + 1
    bucket = [0] * lenth
    for item in lst:
        bucket[item - min(lst)] += 1 
    for i in range(len(bucket)):
        if bucket[i] > 0:
            sorted_list.extend([(i + min(lst))] * bucket[i])
    print(sorted_list)            
    return sorted_list 
bucket_sort(lst)           
    
    