'''
Created on 2016年1月18日
# encoding: utf-8
@author: tcliu


'''
from random_list import RandomList
R = RandomList(5, 10)
lst = R.gen()

def path_sort(list, start_index,end_index):
        flag = list[end_index]
        i = start_index - 1
        for j in range(start_index,end_index):
            if list[j] > flag:
                pass
            else:
                i += 1
                tmp = list[i]
                list[i] = list[j]
                list[j] = tmp
        tmp = list[end_index]
        list[end_index] = list[i+1]
        list[i+1] = tmp

        return i+1

def Quick_sort(list,start_index,end_index):
        if start_index >= end_index:
            return
        middle = path_sort(list,start_index,end_index)
        Quick_sort(list,start_index,middle-1)
        Quick_sort(list,middle+1,end_index)
        print(list)

Quick_sort(lst,0,len(lst)-1)                       
print(lst)       

