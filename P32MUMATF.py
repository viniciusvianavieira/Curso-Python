#P32MUMATF.py
#Universidade Federal Fluminense
#Escola de Engenharia
#TCC00326 Programação de Computadores - T.D1 - Semestre 1/18 - 21/06/2018
#Professor: John Reed
#Programador: João Wilson da Silva Costa - Matrícula: 118037025
#P32MUMATF: Multiplica matrizes com funções
#Método: Funções
#Descrição dos Objetos
def lematin(arq,lin,frase):
  print(frase)
  mat=[]
  for i in range(0,lin,1):  # percorre as linhas
    LIN = list(map(int,arq.readline().split(' ')))
    mat.append(LIN)
  return mat
def impmatin(mat,lin,frase):
  print(frase)
  for i in range(0,lin,1):
    print(mat[i])
def mumatin(matA,m,n,matB,p):
  mat=[]
  for i in range(0, m, 1):  # linhas de A
    LIN=[0]*p  # colunas de B
    for j in range(0,p,1):  # colunas de B
      for k in range(0,n,1):   #Colunas de A ou linhas de B
        LIN[j] = LIN[j] + matA[i][k] * matB[k][j]
    mat.append(LIN)
  return mat
#Boas Vindas
print("Bem vindo ao programa P32MUMATF: Multiplica duas matrizes de inteiros.")
#Dialogo de Entrada de Dados
ARQMAT=open('MATRIZES2.txt','r')
A=lematin(ARQMAT,3,'Lendo a matriz A(3x4) do arquivo MATRIZES2.txt...')
impmatin(A,3,'Matriz A lida:')
ARQMAT.readline()            #Para pular uma linha no arquivo
B=lematin(ARQMAT,4,'Lendo a matriz B(4x2) do arquivo MATRIZES2.txt...')
impmatin(B,4,'Matriz B lida:')
#Processamento
C=mumatin(A,3,4,B,2)
#Emissão de Relatório de Saida
impmatin(C,3,'A multiplicação computado de AxB é:')
#Despedida
print("Fim de execução!")
#FIM!
