'''
Created on 2016年1月18日
# encoding: utf-8
@author: tcliu


'''
from random_list import RandomList
R = RandomList(5, 10)
lst = R.gen()
def sub_sort(array,low,high):
    key = array[low]
    while low < high:
        while low < high and array[high] >= key:
            high -= 1
        while low < high and array[high] < key:
            array[low] = array[high]
            low += 1
            array[high] = array[low]
    array[low] = key
    return low

def quick_sort(array,low,high):
    if low < high:
        key_index = sub_sort(array,low,high)
        quick_sort(array,low,key_index)
        quick_sort(array,key_index+1,high)                   
    
    
print(lst)        
quick_sort(lst, 0, len(lst)-1)
print(lst)       

