# -*- coding: utf-8 -*-

# Implementación de los tableros semánticos (tableaux)
# Input: cadena de la formula en notacion inorder
# Output: lista de listas de literales

# Importando la libreria tableaux
import tableaux as T


x = T.par_complementario([T.Tree('-',None,T.Tree('Z1',None,None)), T.Tree('S1',None,None), T.Tree('-',None,T.Tree('S10',None,None)), T.Tree('Z10',None,None)])
print(x)

b= T.par_complementario([T.Tree('b',None,None), T.Tree('-',None,T.Tree('a',None,None)), T.Tree('-',None,T.Tree('c',None,None)), T.Tree('a',None,None), T.Tree('d',None,None)])
print(b)