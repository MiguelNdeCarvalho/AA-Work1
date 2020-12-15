from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder
from sklearn import tree as TreeModule



from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.utils import resample

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import argparse

class myDecisionTreeREPrune: 
    
    #construtores
    def __init__(self):
        
        self.criterion='gini'
        self.prune=True


    def __init__(self,crit,pru):

        self.criterion = crit
        self.prune = pru

    #metodos
    def fit(x,y):
        
        """
        if Homogeneo(D) 
            return Etiqueta(D)
        S = MelhorParticao(D, F) #
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

    def score(x,y):
        
        
        return 0

    def setCriterion(self, criterion):
        return 0

    def setImpureza(self,x):
        return 0

    #funçao auxiliar
    def homogeneo(D):
        return 0

    def etiqueta(D):
        return 0

    def melhorDivisao(D, F):
        
        """
        Função deve medir a pureza da divisão
            ○Os filhos são "puros" se todos os seus exemplos pertencerem à mesma classe

        Função de impureza (assume atributos booleanos e 2 classes)
            ○depende apenas da magnitude relativa (proporção p) do nº de exemplos de cada classe○deve ter o mesmo valor trocando a classe positiva e negativa
            ○deve ser 0 sempre que a proporção é 0 ou 1
            ○deve ser máxima quando a proporção é 1/2
        """

        return 0

if __name__ == '__main__':

    parser = argparse.ArgumentParser()        
    parser.add_argument('-f', "-file", action='store', dest='file_location', help='Path to the file that contains the data', required=True)
    parser.add_argument('-c', '-criterion', action='store', dest='criterion', help='Choose criterion, it can be Gini or Entropy. By default: Gini', default='gini')
    parser.add_argument('-p', '-prune', action='store_false', dest='prune', help='Set prune. By default: False', default=False)              
    results = parser.parse_args()


    data=np.genfromtxt(results.file_location, delimiter=",", dtype=None, encoding=None)
    xdata=data[1:,0:-1]    #  dados: da segunda à ultima linha, da primeira à penúltima coluna  
    ydata=data[1:,-1]      # classe: da segunda à ultima linha, só última coluna
    attributes = data[0,:]

    print(attributes)

    ord_enc = OrdinalEncoder()
    xdata = ord_enc.fit_transform(xdata)
    ydata = np.array(ydata).reshape((len(ydata),1))
    ydata = ord_enc.fit_transform(ydata)

    x_train, x_test, y_train, y_test = train_test_split(xdata, ydata, random_state=0)

    print(x_train)