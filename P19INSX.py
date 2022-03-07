#P19INSX.py
#Universidade Federal Fluminense
#Escola de Engenharia
#TCC0326 Programcao de Computadores - T.D1 - Semestre 1/18 - DATA
#Professor John Reed
#Programador Caio Cardoso - Matricula: 017...
#P19INSX.py: Insere elemnto no vetor mantendo a ordem
#Metodo: Inserção direta

#Descricao dos objetos
#A: vetor já ordenado
#x: inteiro a ser inserido
#i,j: variável de percorrimento
#Boas vindas
print("Bem vindo ao programa P19INSX: Insere elemento no vetor mantendo a ordem \n")
#Diálogo de entrada
vet19 = open('arquivo19.txt','r')
print("Lendo 10 inteiros já ordenados do arquivo19.txt...\n")
A = list(map(int,vet19.readline().split(" ")))
print(A)
x=int(input("Digite o inteiro a ser inserido:"))
#processamento
A.append(x)                               #Pré insere o x
if(x<A[len(A)-2]):                        #Se x vai entrar no meio
    i=0
    while(A[i]<x):                       #Localiza
      i=i+1
    for j in range(len(A)-2,i-1,-1):      #Move o bloco ...
      A[j+1]=A[j]                         #... para a direita
    A[i]=x                                #Insere o x
print("Após a inserção o vetor ficou:")
print(A)
vet19.close()
print("--------------------------------------------")
print("Agora usando métodos facilitadores")
vet19 = open('arquivo19.txt','r')
print("Lendo 10 inteiros já ordenados do arquivo19.txt...\n")
A = list(map(int,vet19.readline().split(" ")))
print(A)
x=int(input("Digite o inteiro a ser inserido:"))
if(x<A[len(A)-1]):
  i=0
  while(A[i]<x):
      i=i+1
  A.insert(i,x)
else:
  A.append(x)
vet19.close()
#Emissão do relatório de saída
print("Após a inserção o vetor A ficou:")
print(A)
#Despedida
print("Fim de execução!")