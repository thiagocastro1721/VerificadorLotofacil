#Instale a biblioteca loteria-caixa com o comando "pip install loteria-caixa"
#Mais detalhes em "https://pypi.org/project/loteria-caixa/" 
#github do criador:
#https://github.com/thiagocastro1721/VerificadorLotofacil
# -*- coding: utf-8 -*-
from loteria_caixa import (LotoFacil)

concurso = LotoFacil()
        
apostaA = [1,2,3,4,5,8,9,10,11,12,16,18,21,22,23,24,25]
apostaB = [4,5,6,7,8,9,11,12,13,14,16,18,19,20,21,22,24]

resultado = [int(val) for val in concurso.listaDezenas()]

def verificarAcertos(aposta):
    acertos = 0
    numerosAcertados = []
    for itemA in aposta:
        for itemR in resultado:
            if itemA == itemR:
                numerosAcertados.append(itemA)
                acertos = acertos + 1
    print("Numeros acertados:", numerosAcertados)
    print("Quantidade de acertos:", acertos)
        
print("****************************************************************************************")
print("Concurso mais recente:", concurso.numeroConcursoProximo() - 1)
print("Resultado do concurso:", resultado)
print("\n")
print("Aposta A:", apostaA)
verificarAcertos(apostaA)
print("\n")
print("Aposta B:", apostaB)
verificarAcertos(apostaB)
print("\n")

print("Data do próximo concurso:", concurso.dataProximoConcurso())
print("****************************************************************************************")
