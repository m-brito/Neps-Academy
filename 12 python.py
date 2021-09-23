#Enquanto você estava estudando no Neps Academy você viu
#um problema chamado "Potências Simples" e resolveu lê-lo,
#o problema pedia para você ler dois números reais e
#imprimisse um número elevado ao outro. Faça um programa
#que resolva o problema.

#Entrada
#A entrada é composta por apenas uma linha que contem
#dois números reais, x e y.

#Saída
#Seu programa deve imprimir um único número xy com
#4 casas decimais de precisão.

import math
X, Y=input().split()
conta=0
X=float(X)
Y=float(Y)
conta=(math.pow(X, Y))

print("{:.4f}".format(conta))
