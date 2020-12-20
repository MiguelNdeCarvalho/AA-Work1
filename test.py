import math
import numpy

data=numpy.genfromtxt("dados/weather.nominal.csv", delimiter=",", dtype=None, encoding=None)
xdata=data[1:,0:-1]
ydata=data[1:,-1]
attributeList=data[:1,:-1]
# 1º Calcular entropia global: entropy(p,n) p = numeros de sim n = numeros de nao

def entropyGlobalCount(ydata):
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
    values = []
    attributePos = numpy.where(attributeList == attribute)
    for value in data:
        if value[attributePos[1][0]] not in values:
            values.append(value[attributePos[1][0]]) 
    return values

def entropyAttributesCount(attribute, attributeList, value, xdata, ydata):
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
    values = getValues(xdata,attributeList, attribute)
    total = 0
    for value in values:
        entropyValues = entropyAttributesCount(attribute, attributeList, value, xdata, ydata)
        entropy = entropyCalc(entropyValues)
        total += (sum(entropyValues) / sum(entropyGlobalValues)) * entropy    
    gain = entropyGlobal - total
    return gain

def chooseNode(attributeList):
    aux = []
    for attribute in attributeList[0]:
        aux.append(calculateGain(attribute, attributeList, xdata, ydata, entropyGlobalValues, entropyGlobal))
    index = aux.index(max(aux))
    return attributeList[0][index]

rootNode = chooseNode(attributeList)
# 3º Passo, ver se chegamos a um leaf(folha) e retirar

def isLeaf(attribute, attributeList, value, xdata, ydata): #checks if that value only has the same value
    attributePos = numpy.where(attributeList == attribute)
    aux = []
    for x,y in zip(xdata, ydata):
        if x[attributePos[1][0]] == value and y not in aux:
            aux.append(y)
    if len(aux) == 1:
        return True
    return False

def checkLeaf(rootNode):
    aux=[]
    values = getValues(xdata, rootNode, attributeList)
    for value in values:
        if not isLeaf(rootNode, attributeList, value, xdata, ydata):
            aux.append(value)
    return aux

attributesWithoutLeafs = checkLeaf(rootNode)

# 4º Passos Calcular a entropia Global

def globalEntropyNextRun(attributesWithoutLeafs):
    aux=[]
    for attribute in attributesWithoutLeafs:
        count = entropyAttributesCount(rootNode, attributeList, attribute, xdata, ydata)
        aux.append(entropyCalc(count))
    return aux

globalEntropyNextRun(attributesWithoutLeafs)
