#P22INORD.py
#Universidade Federal Fluminense
#Escola de Engenharia
#TCC00326 Programação de Computadores - T.D1 - Semestre 18.1 - 22/05/2018
#Professor John Reed
#Programador Thauan Faria de Souza
#P22INORD: Separa os múltiplos de 3 numa lista B
#Metodo : Inserção

#Descrição dos Objetos
#A: É uma lista com 20 números não ordenados
#B: A lista em vazio
# Boas vindas
print("Bem vindo ao programa P22INORD: Separada os múltiplos de 3 em outra lsita. ")
#Dialogo de entrada de dados
vet22=open('ARQUIVO22.txt', 'r')
print("Lendo 20 inteiros do ARQUIVO22.txt...")
A=list(map(int,vet22.readline().split(" ")))
print(A)
B=[]
#Processamento
L=len(A)-1
i=0
while(i<=L):
  if(A[i]%3==0):
    B.append(A[i])
    j=0
    while(j<=len(B)-1):
      j=j+1                               #J aponta para posição de inserção
    if(j!=len(B)-1):                      #Se não é o último em B
        for k in range(len(B)-2,(j-1),-1): #Move o bloco
          B[k+1]=B                      #Para direita
          B[j]=A[i]
    A.pop(i)
    L=L-1
  else:
    i=i+1
print("Depois da modificação ficou...")
print(A)
print(B)
#Emissão de Relatório de Saída
#...
#Despedida
print ("Fim de execução")
