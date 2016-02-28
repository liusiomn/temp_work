'''
Created on 2016年1月12日
# encoding: utf-8
@author: tcliu
'''
import random
class RandomList():
    def __init__(self, n, k):
        self.n = n
        self.k = k
        self.randomlist = []
        
    def gen(self): 
        for i in range(self.n):
            self.randomlist.append(random.randint(0, self.k))
        print(self.randomlist)    
        return self.randomlist    
               
        
