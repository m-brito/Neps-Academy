#Seu professor lhe passou um exercício onde você deve encontrar
#a raiz quadrada de vários números, como você não quer perder
#tempo com essa tarefa tosca e sem sentido você resolveu fazer
#um programa que dados N números ele retorna a raiz quadrada de
#cada um desses números

#Entrada
#A primeira linha de entrada contém um número inteiro N
#representando a quantidade de números dos quais você terá
#que responder qual a raiz quadrada. A segunda linha da entrada
#contém os N números separados por um espaço em branco.

#Saída
#Seu programa deve imprimir N linhas, cada uma contendo
#a raiz do número na ordem, cada raiz com precisão de 4
#casas decimais.

import math
NQ=int(input())
N=input().split()
b=0
for i in range(len(N)):
    N[i]=float(N[i])
for a in (N):
    b=(math.sqrt(a))
    print("{:.4f}".format(b))
