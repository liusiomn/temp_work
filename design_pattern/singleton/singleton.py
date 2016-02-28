'''
Created on 2016年2月27日
# coding=utf-8
@author: tcliu
'''
def singleton(cls, *args, **kw):
    instance = {}
    def _singleton():
        if cls not in instance:
            instance[cls] = cls(*args, **kw)
        return instance[cls]
    return _singleton    

class Singleton2(type):  
    def __init__(self, name, bases, class_dict):  
        super(Singleton2, self).__init__(name, bases, class_dict)  
        self._instance = None  
    def __call__(self, *args, **kw):  
        if self._instance is None:  
            self._instance = super(Singleton2, self).__call__(*args, **kw)  
        return self._instance  
    
if __name__ =='__main__':
    class MyClass3(object):  
        __metaclass__ = Singleton2  
   
    one = MyClass3()  
    two = MyClass3()  
    print(id(one))
    print(id(two)) 

#     @singleton  
#     class MyClass4(object):  
#         a = 1  
#         def __init__(self, x=0):  
#             self.x = x 
#     one = MyClass4()  
#     two = MyClass4()        
#     print(id(one))
#     print(id(two))       