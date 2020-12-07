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

  def myfunc(self):
    print("Hello my name is " + self.name)

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



iris_dataset = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'], random_state=0)

tree = myDecisionTreeREPrune()

tree.fit(X_train, y_train)
print(tree.score(X_test,y_test))

#falta implementar o Reduced-error pruning (slides)


