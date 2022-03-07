#P16DIZMEN
#Universidade Federal Fluminense
#Escola de Engenharia
#TCC0326 Programcao de Computadores - T.D1 - Semestre 1/18 - DATA
#Professor John Reed
#Programador Caio Cardoso - Matricula: 017...
#P16DIZMEN.py: Localiza o menor elemento de um vetor
#Metodo: Trivial

#Descricao dos objetos
#A: vetor de 10 inteiros
#m: posição do menor elemento
#Boas vindas
print("Bem vindo ao programa P16DIZMEN: Localiza o menor elemento do vetor\n")

#Dialogo de entrada de dados
vet3 = open('arquivo3.txt','r')
print("Lendo 10 inteiros do arquivo3.txt...")
A = list(map(int,vet3.readline().split(" ")))
print("Foram lidos ",len(A)," inteiros para o vetor A")
print(A)
#Processamento
m=0                  #hipótese inicial
for i in range(1,(9+1),1):
    if(A[i]<A[m]):
        m=i
vet3.close()
#Emissão de relatório de saída
print("O menor elemento do vetor está na posição: ",m," e vale: ",A[m])
#Despedida
print("Fim de execução!")