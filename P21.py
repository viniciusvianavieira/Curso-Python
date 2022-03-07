#P21RETX.py
#Universidade Federal Fluminense
#Escola de Engenharia
#Programação de computadores - Período 2018.1 - 04/06/2018
#Professor John Reed
#Programador Thauan Faria
#P12RETX: Retira um elemento com valor x, mantendo a ordem.
#Estratégia: Método "For"
#Descrição dos Objetos:
#A: É uma lista já ordenada
#X: Vetor a ser retirado da lista
#Boas Vindas
print("Bem vindo ao programa P12RETX: Retira um elemento da lista A, mantendo a ordem.")
vet21=open('arquivo20.txt','r')
A=list(map(int,vet21.readline().split(" ")))
print("Lista A:", A)
X=int(input("Informe o elemento a ser retirado da lista: "))
#Processamento
if(X<=A[len(A)-1]):
  i=0
  while(A[i]<X):
      i=i+1
  if(A[i]==X):
    for j in range(i,len(A)-1,1):            #Move o bloco
      A[j]=A[j+1]                            #Para esquerda
    A.pop()                                  #Remove o último
    print(X, " foi retirado da posição", i)
    print("Após a remoção ficou: ", A)
  else:
      print("Esse elemento não está na lista")
else:
    print("Esse elemento não está na lista")
print("Agora usando métodos facilitadores:")
print("Lista A:", A)
X=int(input("Digite o elemento a ser retirado: "))
if(X in A):
  A.remove(X)
  print("Após a remoção ficou:", A)
else:
  print("Esse elemento não pertence à lista.")
#Emissão do Relatório de Dados
#Esse programa possui a emissão do relatório de dados diluído no processamento.
#Despedida
print("Fim de execução.")