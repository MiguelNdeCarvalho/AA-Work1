"""
Objetivo:

O objetivo deste trabalho é implementar um algoritmo de árvore de 
decisão (parcialmente) compatível com o sklearn que implemente um 
método de poda "reduced error prunning". 
Este trabalho será a base para um dos trabalhos práticos sujeitos 
avaliação (os detalhes sobre a submissão, prazo, testes, etc serão 
indicados nas próximas 2 semanas).  Deverá implementar uma árvore de 
decisão de acordo com o algoritmo apresentado nos slides da disciplina 
usando uma função de impureza parameterizável (considere que o default
 será  a percentagem de casos mal classificados, e como alternativas o 
 GINI e a entropia).
 
"""
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.utils import resample

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

class myDecisionTreeREPrune: 
    
  def __init__(self):
    self.tree = DecisionTreeClassifier(min_impurity_decrease=0) #defaul: (criterion='gini')
    self.impureza = 0; 

  def setGini(self):
    self.tree = DecisionTreeClassifier(criterion="gini")
  
  def setEntropy(self):
    self.tree = DecisionTreeClassifier(criterion="entropy")

  def setImpureza(self,x):
    self.impureza = x
    self.tree = DecisionTreeClassifier(min_impurity_decrease=x,criterion=self.tree.criterion)
      
  def getImpureza(self):
    return self.impureza 
  


  def fit(self,X_train, y_train):
      
      self.tree.fit(X_train,y_train)

      return self.tree 

  def score(self,X_test,y_test):
      
      return self.tree.score(X_test, y_test)*100 #+ conjunto de teste

#falta implementar o Reduced-error pruning (slides)

"""
# imports
# código
# etc  

data=np.genfromtxt("weather.nominal.csv", delimiter=",", dtype=None, encoding=None)
xdata=data[1:,0:-1]    #  dados: da segunda à ultima linha, da primeira à penúltima coluna  
ydata=data[1:,-1]      # classe: da segunda à ultima linha, só última coluna

x_train, x_test, y_train, y_test = train_test_split(xdata, ydata, random_state=0)

classifier = myDecisionTreeREPrune()
classifier.fit(x_train, y_train)
result = classifier.score(x_test, y_test)
print("Percentagem de casos corretamente classificados {:2.2%}".format(result))
"""

if __name__ == '__main__':
  iris_dataset = load_iris()
  X_train, X_test, y_train, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'], random_state=0)

  tree = myDecisionTreeREPrune()

  tree.fit(X_train, y_train)
  print(tree.score(X_test,y_test))