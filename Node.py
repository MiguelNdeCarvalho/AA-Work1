class Node:

    def __init__(self):

        self.sons = []
        self.sons_order = []
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
    
    def set_Sons(self,data):
        self.sons_order = data
    
    def get_Sons(self):
        return self.sons_order

    def printData(self):
        print(self.data)

    def printSons(self):
        print(self.sons)

    
    
if __name__ == '__main__':

    no1 = Node()
    data = "outlook"
    no = Node(data)
    print(no.get_Data())
