from typing import NamedTuple

class Data(NamedTuple):

    #identificadores de nos

    imp: float #se folha then = 0
    values: list

class Node:

    def __init__(self):

        self.sons = []
        self.data = Data()
    
    def __init__(self,data=None):

        if data is not None:
            self.data = data
        self.sons = []

    def __str__(self):
        return "Filhos:" + str(self.sons) + " " + str(self.data)

    def is_leaf(self):
        if len(self.sons) == 0:
            return True
        else:
            return False

    def set_Data(self,data):
        self.data = data
    
    def get_Data(self):
        return self.data
    
    def printData(self):
        print(self.data)

    def printSons(self):
        print(self.sons)

no1 = Node()
data = Data(imp=0.5,values=[3,2])
no = Node(data)
print(no.is_leaf())