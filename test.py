import math
import numpy

def entropy(p,n):
    return (-p/(p+n)) * math.log2(p/(p+n)) - (n/(p+n)) * math.log2(n/(p+n))

# def entropy_value(p_atribute,n_atribute,p,n):
    # return ((p_atribute+n_atribute) / (p + n)) * entropy(p_atribute,n_atribute)

#def entropy_class(class, value):
    #encontrar quantos sim e não

# 2º Calcular entropy para cada value de cada atributo. Ex: Sunny, Rainny, Overcast do Outlook

def count_p_n_global(data):
    p,n = 0,0
    for value in data:
        if value == "yes":
            p +=1
        elif value == "no":
            n +=1
    return p,n

data=numpy.genfromtxt("dados/weather.nominal.csv", delimiter=",", dtype=None, encoding=None)
xdata=data[1:,0:-1]
ydata=data[1:,-1]
attributeList=data[:1]

# 1º Calcular entropia global: entropy(p,n) p = numeros de sim n = numeros de nao
p,n = count_p_n_global(ydata)
globalEntropy = entropy(p,n)

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
    for x,y in zip(xdata,ydata):
        if x[0] == value:
            if y == "yes":
                countP += 1
            elif y == "no":
                countN += 1
    return countP,countN

values= getValues(xdata, attributeList, "outlook")
valuePOrN = countValuePOrN("outlook", attributeList, "sunny", xdata, ydata)
print(valuePOrN)
