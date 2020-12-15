
from sklearn.model_selection import train_test_split
import numpy as np
import argparse

class myDecisionTreeREPrune: 
    
    #construtores
    def __init__(self):
        
        self.criterion='gini'
        self.prune=True

        self.sample_size = 0
        self.root = Node()


    def __init__(self,crit,pru):

        self.criterion = crit
        self.prune = pru



    #metodos
    def fit(self,x,y):
        
        D = [x,y]

        if Homogeneo(D): 
            return Etiqueta(D)
        

        """
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

    def score(self,x,y):
        
        #percorrer a arvore com cada um dos exemplos (interate_for)
        return 0

    def iterate_for(self,objeto):
        return 0 #class atribuida ao objeto

    def prune(self):
        return 0

    #funçoes auxiliar
    def homogeneous(D):     #folha instantanea 
        
        
        
        return 0  #true/false

    def tag(D):      
        return 0 #node

    def bestDivision(D, F):
        
        """
        Função deve medir a pureza da divisão
            ○Os filhos são "puros" se todos os seus exemplos pertencerem à mesma classe

        Função de impureza (assume atributos booleanos e 2 classes)
            ○depende apenas da magnitude relativa (proporção p) do nº de exemplos de cada classe○deve ter o mesmo valor trocando a classe positiva e negativa
            ○deve ser 0 sempre que a proporção é 0 ou 1
            ○deve ser máxima quando a proporção é 1/2
        """

        return 0 #node

    def entropy(D):
        
        
        return 0
    
    def gini(D):
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
    attributes = data[0,:-1]
    classes = data[0,-1]


    print(attributes)
    print(xdata)
    print(classes)
    print(ydata)

    x_train, x_test, y_train, y_test = train_test_split(xdata, ydata, random_state=0) #default test_size=25

