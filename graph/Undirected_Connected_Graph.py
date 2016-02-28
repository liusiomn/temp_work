'''
Created on 2016年2月27日
encoding: utf-8
@author: tcliu
'''
import random 
from collections import OrderedDict
from complete_binary_tree import Complete_Binary_Tree
from pprint import pprint

class Undirected_Connected_Graph(Complete_Binary_Tree):
    def gen_matrix(self):
        tree_matrix = Complete_Binary_Tree.gen_matrix(self)
        for line_num in range(1, self.n):
            for column_num in range(1, self.n):
                flag = random.randint(0, 1)
                if tree_matrix[line_num][column_num] == 9999 and flag==1:
                    tree_matrix[line_num][column_num] = 1
        graph_matrix = tree_matrix
        pprint(graph_matrix)
        return graph_matrix 
    
               
if __name__ =='__main__':
    g = Undirected_Connected_Graph(5)
    g.gen_matrix()                            


