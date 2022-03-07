#P22INORD.py
#Universidade Federal Fluminense
#Escola de Engenharia
#Programação de computadores - Período 2018.1 - 04/06/2018
#Professor John Reed
#Programador Thauan Faria
#P22INORD: Separa os múltiplos de 3 em outra lista.
#Método: Inserção
#Descrição de Objetos
#A: É uma lista com 20 números não ordenados.
#B: É uma lista em vazio.
#i: Variável auxiliar
#Boas vindas
print("Bem vindo ao programa P22INORD: Separa os múltiplos de 3 em outra lista")
#Diálogo de entrada de dados
vet22=open('ARQUIVO22.txt','r')
A=list(map(int,vet22.readline().split(" ")))
print("Lista A:", A)
B=[]
#Processamento
i=0
if(i<=len(A)-1):
  i=i+1
  if(A[i]%3==0):
    B.append(A[i])
    j=0
    while(j<=len(B)-1):
        j=j+1
