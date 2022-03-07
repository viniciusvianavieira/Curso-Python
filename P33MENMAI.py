#P33MENMAI.py
#Universidade Federal Fluminense
#Escola de Engenharia
#TCC00326 Programação de Computadores - T.D1 - Semestre 1/18 - 21/06/2018
#Professor: John Reed
#Programador: João Wilson da Silva Costa - Matrícula: 118037025
#POCABECA: Apresenta a estrutura usual de um programa
#Método: Funções
#Descrição dos Objetos
def levetin(arq,frase):
  print(frase)
  lin=list(map(int,arq.readline().split(" ")))
  return lin
def impvetin(vet,frase):
  print(frase)
  print(vet)
def locmenmai(vet):
  menor=0  # Hipótese inicial
  maior=0
  for i in range(1, len(vet), 1):
    if (vet[i] < vet[menor]):
      menor=i
    else:
      if(vet[i]>vet[maior]):
        maior=i
  return menor,maior
#Boas Vindas
print("Bem vindo ao P33MENMAI: ")
#Dialogo de Entrada de Dados
ARQVET=open('menmai.txt','r')
A=levetin(ARQVET,"Lendo 10 inteiros do arquivo menmai.txt...")
impvetin(A,"Vetor A lido:")
#Processamento
men,mai=locmenmai(A)
#Emissão de Relatório de Saida
print("O menor elemento está na posição:", men)
print("O maior elemento está na posição:", mai)
#Despedida
print("Fim de execução!")
#FIM!
