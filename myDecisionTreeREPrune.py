
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

            self.root = Node()
            self.root.set_Data(rootNode)

            valuesLeafs,classeLeafs = checkLeaf(rootNode)

            not_leafs,sons_order = valuesNotToLeafs(valuesLeafs,x,self.root.get_Data(),attributeList)

            print(valuesLeafs,classeLeafs)
            
            setSons(self.root,sons_order,not_leafs,valuesLeafs,classeLeafs)

            print(self.root)

            PrintTree(self.root)
                    
            """
            divide D em subconjuntos Di de acordo com os literais em S;
            foreach i do
                if Di não vazio:
                        Ti = CresceArvore(Di , F) 
                    else
                        Ti é uma folha com etiqueta Etiqueta(D);
                    end
                end
            return uma árvore de raíz com etiqueta S e filhos T
            """
        
        return 0

    def score(self,x,y):
        
        #for row in 
        result = iterate_for(self,xdata[1,0:-1],ydata[1])
        print(result)
        #percorrer a arvore com cada um dos exemplos (iterate_for)
        return 0

def iterate_for(self,x_object,y_object):
    
    node_atual = self.root

    while not node_atual.is_leaf():
        break

    if node_atual.get_Data() == y_object[0]:
        return "hit"
    
    return "miss" #class atribuida ao objeto

    def prune(self):
        return 0

def PrintTree(node):
    
    if node == None:
        pass
    
    if node.is_leaf():
        print(node.get_Data())
    else:
        for sons in range(len(node.sons)):
            PrintTree(node.sons[sons])
        


def setSons(node,sons_order,valuesNotLeafs,valuesLeafs,classeLeafs):
    
    print(node,sons_order,valuesNotLeafs,valuesLeafs,classeLeafs)

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

def checkLeaf(rootNode):
    '''
    Verifica se o atributo principal (rootNode) apresenta leafs.
    Retorna um array com os values sem os leafs
    '''
    aux=[]
    aux_class = []
    values = getValues(xdata, rootNode, attributeList)
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
    attributePos = numpy.where(attributeList == attribute)
    for value in data:
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
                aux[count] +=1
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
        aux.append(calculateGain(attribute, attributeList, xdata, ydata, entropyGlobalValues, entropyGlobal))
    index = aux.index(max(aux))
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
    tree.fit(x_train,y_train,attributeList)
    print(attributeList)
    tree.score(x_test,y_test)

