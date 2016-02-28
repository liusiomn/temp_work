'''
Created on 2016年1月18日
# encoding: utf-8
@author: tcliu


'''
from random_list import RandomList
R = RandomList(5, 10)
#lst = R.gen()
lst = [5,7,1,3,9]

def quick_sort(lst):
    base = lst[0]
    i = 0
    j = len(lst) -1 
    while i != j:
        while (lst[j] >= base and i < j):
            j -= 1
        while (lst[i] <= base and i<j):
            i += 1
        if i<j:
            lst[i], lst[j] = lst[j], lst[i]
    return lst    
    quick_sort(lst)
     
a = quick_sort(lst)
print(a)                    
            
        

