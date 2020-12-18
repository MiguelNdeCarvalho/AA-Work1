class Node:

    def __init__(self):

        self.sons = []
        self.data = ""
    
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
data = "outlook"
no = Node(data)
print(no.get_Data())