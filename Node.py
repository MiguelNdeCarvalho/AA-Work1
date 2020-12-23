class Node:

    def __init__(self):

        self.sons = []
        self.data = ""

    def __str__(self):
        return "Data: " + str(self.data) + ", Filhos:" + str(self.sons)


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

    def set_Data(self,data):
        self.data = data
    
    def get_Data(self):
        return self.data
    
    
    def add_son(self,node):
        self.sons.append(node)

    def remove_son(self,node):
        
        self.sons.remove(node)
    
    
if __name__ == '__main__':

    no1 = Node()
    data = "outlook"
    no = Node(data)
    print(no.get_Data())
