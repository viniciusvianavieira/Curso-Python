#P20 fazer retirada de inteiro de vetor

#P20INSBA.py
#Universidade Federal Fluminense
#Escola de Engenharia
#TCC0326 Programcao de Computadores - T.D1 - Semestre 1/18 - DATA
#Professor John Reed
#Programador Caio Cardoso - Matricula: 017...
#P20INSBA.py: Retira elemnto do vetor mantendo a ordem
#Metodo: Inserção direta

#Descricao dos objetos
#A: vetor já ordenado
#B: vetor já ordenado

#Boas vindas
print("Bem vindo ao programa P20INSBA: Insere o vetor B no vetor A mantendo a ordenção\n")
#Diálogo de entrada
vet20 = open('arquivo20.txt','r')
print("Lendo 10 inteiros já ordenados do arquivo20.txt...\n")
A = list(map(int,vet20.readline().split(" ")))
print(A)
print("Lendo 5 inteiros já ordenados do arquivo20.txt...\n")
B = list(map(int,vet20.readline().split(" ")))
print(B)
#Processamento
for k in range(0,len(B),1):
    A.append(B[k])  # Pré insere o B[k]
    if (B[k]< A[len(A) - 2]):  # Se B[k] vai entrar no meio
        i = 0
        while (A[i] < B[k]):  # Localiza
            i = i + 1
        for j in range(len(A) - 2, i - 1, -1):  # Move o bloco ...
            A[j + 1] = A[j]  # ... para a direita
        A[i] = B[k]  # Insere o x
#Relatório de saída:
print("Após a inserção de B em A, A ficou:")
print(A)
vet20.close()
#DEspedida
print("Fim de execução!")