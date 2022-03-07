#fazer 19 usando funções python
#P20 fazer retirada de inteiro de vetor

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
#B: vetor ordenado com inteiro adicional
#Boas vindas
print("Bem vindo ao programa P19INSX: Insere elemento no vetor mantendo a ordem \n")
#Diálogo de entrada
vet19 = open('arquivo19.txt','r')
print("Lendo 10 inteiros já ordenados do arquivo19.txt...\n")
A = list(map(int,vet19.readline().split(" ")))
x=int(input("Digite o inteiro a ser inserido:"))
#Processamento
A.append(x)
print(A)
B=sorted(A)
A=B
#Emissão de relatório de saída
print("Após a ordenação A ficou:\n",A)
#Despedida
print("Execução concluída!")