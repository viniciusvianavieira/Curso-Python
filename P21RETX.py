#P21RETX.py
#Universidade Federal Fluminense
#Escola de Engenharia
#TCC0326 Programcao de Computadores - T.D1 - Semestre 1/18 - DATA
#Professor John Reed
#Programador Caio Cardoso - Matricula: 017...
#P21RETX.py: Retira elemnto do vetor mantendo a ordem
#Metodo: Inserção direta

#Descricao dos objetos
#A: vetor já ordenado
#x: elemento a ser retirado
#Boas vindas
print("Bem vindo ao programa P21INSBA: Retira elemento do vetor A mantendo a ordenção\n")
#Diálogo de entrada
vet21 = open('arquivo20.txt','r')
print("Lendo 10 inteiros já ordenados do arquivo20.txt...\n")
A = list(map(int,vet21.readline().split(" ")))
print(A)
x=int(input("Digite o valor do inteiro a ser removido:"))
#Processamento
if(x<=A[len(A)-1]):
  i=0
  while(A[i]<x):                       #Localiza
        i=i+1
  if(A[i]==x):
      for j in range(i,len(A)-1,1): #Move o bloco
          A[j] = A[j+1]             # ... para a esquerda
      A.pop()                       #Retirando o último
      print(x," foi retirado da posição ",i," de A")
      print("Após a retirada o vetor ficou")
      print(A)
  else:
      print(x," não pertence ao vetor A")
else:
    print(x," não pertence ao vetor A")
vet21.close()
print("----------------------------------")
print("Utilizando facilitadores")
x=int(input("Digite um novo elemento a ser retirado:"))
if(x in A):
  A.remove(x)
  print("Após a retirada o vetor ficou")
  print(A)
else:
    print(x," não pertence a A")
#Despedida
print("Fim de execução!")

