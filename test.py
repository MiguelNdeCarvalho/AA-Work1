import math
import numpy


# 2º Calcular entropy para cada value de cada atributo. Ex: Sunny, Rainny, Overcast do Outlook

def count_p_n_global(data):
    p,n = 0,0
    for value in data:
        if value == "yes":
            p +=1
        elif value == "no":
            n +=1
    return p,n

data=numpy.genfromtxt("dados/vote.csv", delimiter=",", dtype=None, encoding=None)
xdata=data[1:,0:-1]
ydata=data[1:,-1]
attributeList=data[:1]

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

def countValuePOrN(attribute, attributeList, value, xdata, ydata): # Get numbers of Positive and Negatives in a value
    countP, countN = 0,0
    attributePos = numpy.where(attributeList == attribute)
    for x,y in zip(xdata,ydata):
        if x[attributePos[1][0]] == value:
            if y == "yes":
                countP += 1
            elif y == "no":
                countN += 1
    return countP,countN



# values= getValues(xdata, attributeList, "outlook")
# valuePOrN = countValuePOrN("windy", attributeList, "TRUE", xdata, ydata)
# print(values)
