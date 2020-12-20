import math
import numpy

data=numpy.genfromtxt("dados/weather.nominal.csv", delimiter=",", dtype=None, encoding=None)
xdata=data[1:,0:-1]#tabela sem Atributos e sem as classes
ydata=data[1:,-1]#classes correspondentes
attributeList=data[:1,:-1]#lista de atributos sem as classes

# 1º Calcular entropia global: entropy(p,n) p = numeros de sim n = numeros de nao

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

entropyGlobalValues = entropyGlobalCount(ydata)
entropyGlobal=entropyCalc(entropyGlobalValues)

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

def chooseNode(attributeList):
    '''
    Função que recebe a lista de attributes e calcula o ganho de cada e retorna o attributo com maior ganho,
    o atributo principal
    '''
    aux = []
    for attribute in attributeList[0]:
        aux.append(calculateGain(attribute, attributeList, xdata, ydata, entropyGlobalValues, entropyGlobal))
    index = aux.index(max(aux))
    return attributeList[0][index]

rootNode = chooseNode(attributeList)
# 3º Passo, ver se chegamos a um leaf(folha) e retirar

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
        return True
    return False

def checkLeaf(rootNode):
    '''
    Verifica se o atributo principal (rootNode) apresenta leafs.
    Retorna um array com os values sem os leafs
    '''
    aux=[]
    values = getValues(xdata, rootNode, attributeList)
    for value in values:
        if not isLeaf(rootNode, attributeList, value, xdata, ydata):
            aux.append(value)
    return aux

valuesWithoutLeafs = checkLeaf(rootNode)

# 4º Passos Calcular a entropia Global

def entropyRootValues(rootNode, attributeList, valuesWithoutLeafs, xdata, ydata):
    '''
    Função que devolve a entropia de cada 
    '''
    aux=[]
    for attribute in valuesWithoutLeafs:
        count = entropyValueCount(rootNode, attributeList, attribute, xdata, ydata)
        aux.append(entropyCalc(count))
    return aux

print(entropyRootValues(rootNode, attributeList, valuesWithoutLeafs, xdata, ydata))
