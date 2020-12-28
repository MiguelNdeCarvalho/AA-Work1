
from sklearn.model_selection import train_test_split
import argparse
import math
import numpy
from Node import Node

class myDecisionTreeREPrune: 
    
    #construtores
    def __init__(self):
        
        self.criterion='gini'
        self.prune=True

        self.sample_size = 0
        self.root = Node()

    #metodos
    def fit(self,x,y,attributeList):
        
        is_homegenus,homo_classe = homogeneous(y)
        
        if is_homegenus: 
            self.root = makeLeaf(homo_classe)
        else:
            entropyGlobalValues = entropyGlobalCount(y)
            entropyGlobal=entropyCalc(entropyGlobalValues)

            rootNode = chooseNode(attributeList,x,y,entropyGlobalValues, entropyGlobal)
            print("Root:", rootNode)
            self.root = Node()
            self.root.set_Data(rootNode)

            valuesLeafs,classeLeafs = checkLeaf(rootNode, attributeList, x, y)
            not_leafs,sons_order = valuesNotToLeafs(valuesLeafs,x,self.root.get_Data(),attributeList)
            print(f"ValueLeafs: {valuesLeafs}, classeLeafs: {classeLeafs}")

            setSons(self.root,sons_order,not_leafs,valuesLeafs,classeLeafs)
            self.root.set_Sons(sons_order)

            #↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
            if valuesLeafs != []:
                new_x,new_y = update_data(x,y,sons_order,valuesLeafs[0])
            
            #↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑

            #print(f"New_X: {new_x}, New_Y: {new_y}, attributeList: {attributeList}")
            
            print(f"not_leafs: {not_leafs}, sons_order: {sons_order}")

            
            for i in range(len(self.root.sons)):
                new_x,new_y = update_data(x,y,self.root.sons[i],sons_order[i])
                attributeList = removeAttribute(attributeList,self.root.get_Data())
                #print(f"New_X: {new_x}, New_y: {new_y}, son: {sons_order[i]} ")
                grow_tree(self.root.sons[i],new_x,new_y,attributeList)

        #PrintTree(self.root)
        
        return 0



    def score(self,x,y,attributeList):
        
        total = len(x)
        count_hit = 0
        #count_miss = 

        for row in range(len(x)): 
            print("----------------")
            result = iterate_for(self,xdata[row,0:],ydata[row],attributeList)
            #print(xdata[row,0:],ydata[row])
            #print(result)
            if result == "hit":
                count_hit+=1

        #print(count_hit,total)
        return count_hit/total *100
        
def iterate_for(self,x_object,y_object,attributeList):
    
    node_atual = self.root
    print(attributeList)

    while not node_atual.is_leaf():
        
        node_data = node_atual.get_Data()
        node_sons = node_atual.get_Sons()

        print(node_atual.get_Data())
        print(node_atual.get_Sons())

        for i in range(len(attributeList[0])):
            print(attributeList[0][i] == node_data)
            if attributeList[0][i] == node_data:
                break
        
        print(i)
        print(x_object[i])

        for x in range(len(node_atual.get_Sons())):
            if x_object[i] == node_sons[x]:
                break

        node_atual = node_atual.sons[x]

    print(f"folha: {node_atual.get_Data()}, must_be: {y_object}")            
    if node_atual.get_Data() == y_object:
        return "hit"
    
    return "miss" #class atribuida ao objeto

    """
    def prune(self):
        
        self
        iter_order = 
        
        return 0
"""

def grow_tree(node,x,y,attributeList):
    print("----------------------")
    if node.get_Data()=="": #
        
        entropyGlobalValues = entropyGlobalCount(y)
        entropyGlobal=entropyCalc(entropyGlobalValues)

        print(f"attributeList: {attributeList},x:{x},y:{y}, Values: {entropyGlobalValues}, Entropy: {entropyGlobal}")
        new_branch = chooseNode(attributeList,x,y,entropyGlobalValues, entropyGlobal)
        print(new_branch)

        print(f"Escolhe Node: {new_branch}, Y: {y}, Count: {entropyGlobalValues} , EntropyGlobal: {entropyGlobal}")
        valuesLeafs,classeLeafs = checkLeaf(new_branch, attributeList, x,y)

        print("valuesLeafs:",valuesLeafs,"classeLeafs:",classeLeafs)


        node.root = Node()
        node.set_Data(new_branch)

        not_leafs,sons_order = valuesNotToLeafs(valuesLeafs,x,node.get_Data(),attributeList)
        node.set_Sons(sons_order)
        print(f"Node_Sons: {node.get_Sons()}")

        print("not_Leafs:",not_leafs,"sons_order:",sons_order)

        setSons(node,sons_order,not_leafs,valuesLeafs,classeLeafs)

        for i in range(len(node.sons)):
            print(node.sons[i],sons_order[i])
            new_x,new_y = update_data(x,y,node.sons[i],sons_order[i])
            #print(f"grow_x: {new_x},grow_x: {new_y}")
            grow_tree(node.sons[i],new_x,new_y,attributeList)


def update_data(x,y,attri,value):

    new_x = []
    new_y = []

    if len(value) == 0:
        return

    #print(f"Attrib: {attri}, Value: {value}  ")
    for row in zip(x,y):
        for i in row[0]:
            if i == value:
                #print(f"I: {i}, Linha: {row[0]}")
                new_x.append(list(row[0])) 
                new_y.append(row[1])
    for row in new_x:
        row.remove(value)

    return new_x, new_y



def removeAttribute(attributeList,attri):

    aux = []

    for row in attributeList:
        for pos in row:
            if pos not in aux and pos != attri:
                aux.append(pos)
    return numpy.array([aux])


def PrintTree(node):
    
    if node == None:
        pass
    
    print(node.get_Data())

    if not node.is_leaf():
        for sons in range(len(node.sons)):
            PrintTree(node.sons[sons])
        


def setSons(node,sons_order,valuesNotLeafs,valuesLeafs,classeLeafs):
    
    for sons in range(len(sons_order)):
        
        if sons_order[sons] in valuesLeafs:
            for pos in range(len(valuesLeafs)):
                if sons_order[sons] == valuesLeafs[pos]:
                    node.sons.append(makeLeaf(classeLeafs[pos]))
        
        if sons_order[sons] in valuesNotLeafs:
            for pos in range(len(valuesNotLeafs)):
                if sons_order[sons] == valuesNotLeafs[pos]:
                    no = Node()
                    node.sons.append(no)


def makeLeaf(classe):
    
    no = Node()
    no.set_Data(classe)

    return no


def valuesNotToLeafs(valuesLeafs,x,atr,attributeList):
    atribute_values = getValues(x,attributeList,atr)

    aux = [] 

    for atri_val in atribute_values:
        if atri_val not in valuesLeafs:
            aux.append(atri_val)

    return aux,atribute_values

def isLeaf(attribute, attributeList, value, xdata, ydata): #checks if that value only has the same value
    '''
    Função que verifica se um atributo é uma folha, ou seja, só já tem uma classe
    1º - verifica quais as classes existentes para esse atributo
    2º - caso seja só 1, diz que é um Leaf.
    '''
    attributePos = numpy.where(attributeList == attribute)
    aux = []
    for x,y in zip(xdata, ydata):
        if x[attributePos[1][0]] == value and y not in aux:
            aux.append(y)
    if len(aux) == 1:
        return True,aux[0]
    return False,[]

def checkLeaf(rootNode, attributeList, xdata, ydata):
    '''
    Verifica se o atributo principal (rootNode) apresenta leafs.
    Retorna um array com os values sem os leafs
    '''
    aux=[]
    aux_class = []
    values = getValues(xdata, attributeList, rootNode)
    for value in values:
        condition,classe = isLeaf(rootNode, attributeList, value, xdata, ydata)
        if condition:
            aux.append(value)
            aux_class.append(classe)
    return aux,aux_class

def entropyGlobalCount(ydata):
    '''
    Esta função retorna num array quantas vezes aparece cada class
    1º For - adiciona no array possible todas as classes possiveis
    2º For - percorre e verifica quantas vezes aparece cada posição possivel
    '''
    possible = []
    aux = []
    for data in ydata:
        if data not in possible:
            possible.append(data)
            aux.append(0)
    for data in ydata:
        count = 0
        for value in possible:
            if data == value:
                aux[count] +=1
            count +=1
    return aux

def entropyCalc(array):
    '''
    recebe como argumento o nmero de vezes que cada classe aparece e calcula a entropia
    1º for - Calcula o número total de classes
    2º for - Calcula a Entropia em si
    '''
    total, result = 0,0
    for pos in array:
        total += pos
    for pos in array:
        result -= (pos/total * math.log2(pos/total))
    return result

#entropyGlobalValues = entropyGlobalCount(ydata)
#entropyGlobal=entropyCalc(entropyGlobalValues)

# 2º Calcular entropy para cada value de cada atributo. Ex: Sunny, Rainny, Overcast do Outlook

def getValues(data, attributeList, attribute):

    '''
    Função que retorna um array com os valores de um dado atributo
    '''
    values = []
    #print(f"attributeList: {attributeList}, attribute: {attribute}")
    attributePos = numpy.where(attributeList == attribute)
    """
    if(attribute == ""):
        print("Nada!")
        return 0
    
    """
    #print(f"Attribute: {attribute}, Lista: {attributeList}, Pos: {attributePos[1][0]}\n Tamanho do Data: {len(data[0])}, Tamanho da AttributeList: {len(attributeList[0])}")
    for value in data:
        #print(f"Value: {value} Pos: {attributePos[1][0]}")
        if value[attributePos[1][0]] not in values:
            values.append(value[attributePos[1][0]])
    return values

def entropyValueCount(attribute, attributeList, value, xdata, ydata):
    '''
    Função que conta o número de classes correspondentes a um value de um atributo
    1º For - adiciona no array possible todas as classes possiveis
    2º For - percorre e verifica quantas vezes aparece cada posição possivel
    '''
    possible = []
    aux = []
    attributePos = numpy.where(attributeList == attribute)
    for x,y in zip(xdata,ydata):
        if x[attributePos[1][0]] == value and y not in possible:
            possible.append(y)
            aux.append(0)
    for x,y in zip(xdata,ydata):
        count = 0
        for i in possible:
            if x[attributePos[1][0]] == value and y == i:
                aux[count]+=1
            count +=1
    return aux

def calculateGain(attribute, attributeList, xdata, ydata, entropyGlobalValues ,entropyGlobal):
    '''
    Função que calcula:
    1º - entropia para cada value de um atributo
    2º - a informação entropia de um atributo
    3º - o ganho (gain) de um atributo
    retorna o ganho de uma class
    '''
    values = getValues(xdata,attributeList, attribute)
    #print(f"Attribute: {attribute} Values: {values}")
    total = 0
    for value in values:
        entropyValues = entropyValueCount(attribute, attributeList, value, xdata, ydata)
        entropy = entropyCalc(entropyValues)
        total += (sum(entropyValues) / sum(entropyGlobalValues)) * entropy    
    gain = entropyGlobal - total
    return gain

def chooseNode(attributeList,xdata, ydata,entropyGlobalValues, entropyGlobal):
    '''
    Função que recebe a lista de attributes e calcula o ganho de cada e retorna o attributo com maior ganho,
    o atributo principal
    '''
    aux = []
    for attribute in attributeList[0]:
        #print(f"Attribute: {attribute},Gain: {calculateGain(attribute, attributeList, xdata, ydata, entropyGlobalValues, entropyGlobal)}")
        aux.append(calculateGain(attribute, attributeList, xdata, ydata, entropyGlobalValues, entropyGlobal))
    index = aux.index(max(aux))
    #print(f"Escolheu Root: {attributeList[0][index]}")
    return attributeList[0][index]

#rootNode = chooseNode(attributeList)
# 3º Passo, ver se chegamos a um leaf(folha) e retirar



#valuesWithoutLeafs = checkLeaf(rootNode)

# 4º Passos Calcular a entropia Global

def entropyRootValues(rootNode, attributeList, valuesWithoutLeafs, xdata, ydata):
    '''
    Função que devolve a entropia de cada value do Atributo Principal (RootNode)
    '''
    aux=[]
    for attribute in valuesWithoutLeafs:
        count = entropyValueCount(rootNode, attributeList, attribute, xdata, ydata)
        aux.append(entropyCalc(count))
    return aux

#funçoes auxiliar

def homogeneous(y):     #folha instantanea 
    

    ref_value = y[0][0]


    for samples in range(len(y)):
        if ref_value != y[samples][0]:
            return False,""

    return True,ref_value  

if __name__ == '__main__':

    parser = argparse.ArgumentParser()        
    parser.add_argument('-f', "-file", action='store', dest='file_location', help='Path to the file that contains the data', required=True)
    parser.add_argument('-c', '-criterion', action='store', dest='criterion', help='Choose criterion, it can be Gini or Entropy. By default: Gini', default='gini')
    parser.add_argument('-p', '-prune', action='store_false', dest='prune', help='Set prune. By default: False', default=False)              
    results = parser.parse_args()


    data=numpy.genfromtxt(results.file_location, delimiter=",", dtype=None, encoding=None)
    xdata=data[1:,0:-1]    #  dados: da segunda à ultima linha, da primeira à penúltima coluna  
    ydata=data[1:,-1]      # classe: da segunda à ultima linha, só última coluna
    attributeList=data[:1,:-1]

    x_train, x_test, y_train, y_test = train_test_split(xdata, ydata, random_state=0) #default test_size=25

    tree = myDecisionTreeREPrune()
    tree.fit(xdata,ydata,attributeList)
    #print(attributeList)
    #PrintTree(tree.root)
    print(x_test)
    print(tree.score(x_test, y_test,attributeList))

