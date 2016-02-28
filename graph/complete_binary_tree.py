'''
Created on 2016年2月11日
# encoding: utf-8
@author: tcliu
'''
import math
from pprint import pprint
from collections import OrderedDict

class Complete_Binary_Tree():
    def __init__(self, n):
        self.n = n
        self.node_list = ['node' + str(i) for i in range(self.n)]
        
    def gen_dict(self):
        tree = OrderedDict([('node0', ('node1', 'node2'))])
        for node in self.node_list:
            parent_node = list(self.get_parent_node(int(node[4:])))
            children_node = self.get_children_node(int(node[4:]))
            if children_node != []:
                tree[node] = (parent_node, (list(children_node)))
            else:
                tree[node] = [parent_node]    
        print(tree)
    
    def gen_matrix(self):
        matrix = [['node'] + self.node_list]
        for line_number in range(self.n):
            line = [self.node_list[line_number]]
            for column_number in range(self.n):
                if ((('node' + str(column_number)) in self.get_children_node(line_number))) or ('node' + str(column_number)) in self.get_parent_node(line_number) : 
                    line.append(1)
                elif column_number == line_number:
                    line.append(0)
                else:
                    line.append(9999)
            matrix.append(line)
        #pprint(matrix, depth= self.n)    
        return matrix    
    
    def gen_point_edge(self):
        point_list = self.node_list
        edge_list = []
        for line_number in range(self.n):
            for column_number in range(line_number):
                if self.gen_matrix()[line_number][column_number] == 1:
                    edge = ('node'+str(line_number), 'node'+str(column_number))
                    edge_list.append((edge))
        point_edge_set = [point_list, edge_list]
        pprint(point_edge_set)
        return point_edge_set                
    
    def get_layer(self, x):
        layer = int(math.log2(x)) + 1
        return layer
    
    def get_left_brother(self, x):
        max_layer = self.get_layer(self.n)
        if x not in [pow(2,n)-1 for n in range(0, max_layer)]:
            left_brother = ['node' + str(i) for i in range((pow(2, (int(math.log2(x))))-1), x)]
        else:
            left_brother = []
        return left_brother
    
    def get_right_brother(self, x):
        max_layer = self.get_layer(self.n)
        if x not in [pow(2,n)-2 for n in range(0, max_layer)]:
            right_brother = ['node' + str(i) for i in range(x+1, pow(2, (int(math.log2(x)) + 1))-1)]
        else:
            right_brother = []
        return right_brother         
                  
    def get_parent_node(self, x):
        if x != 0:
            parent_node = ['node' + str(int(x/2)+ (x % 2) -1)]
        else:
            parent_node = []
        return parent_node
    
    def get_children_node(self, x):
        if (x+1) * 2 <= self.n:
            children_node = ('node'+ str(x *2 + 1), 'node'+ str((x + 1)*2))
        elif ((x+1) * 2 >self.n and x *2 + 1 <= self.n):
            children_node = ['node' + str(x *2 + 1)]        
        else:
            children_node = []
        return children_node                    
        
    def get_info(self, x):
        layer = self.get_layer(x)
        print("node{0} 's layer is {1}".format(x, layer))
        left_brother = self.get_left_brother(x)
        print("node{0} 's left_brother is {1}".format(x, left_brother))
        right_brother = self.get_right_brother(x)
        print("node{0} 's right_brother is {1}".format(x, right_brother))
        children_node = self.get_children_node(x)
        print("node{0} 's children_node is {1}".format(x, children_node))
        parent_node = self.get_parent_node(x)
        print("node{0} 's parent_node is {1}".format(x, parent_node))
    
    def add_nodes(self, n):
        nodes_num = self.n + n
        self.node_list = ['node' + str(i) for i in range(nodes_num)]
        self.gen_dict()               
  

if __name__=='__main__':
    t = Complete_Binary_Tree(11) 
    #t.get_info(11)
    t.gen_point_edge()       