#P17ORDVE.py
#Universidade Federal Fluminense
#Escola de Engenharia
#TCC0326 Programcao de Computadores - T.D1 - Semestre 1/18 - DATA
#Professor John Reed
#Programador Caio Cardoso - Matricula: 017...
#P17ORDVE.py: Ordena o vetor crescentimente
#Metodo: Inserção direta

#Descricao dos objetos
#A: vetor a ser ordenado
#F: fronteira
#Boas vindas
print("Bem vindo ao programa P18LOCX: Localiza um elemento do vetor\n")
#Diálogo de entrada de dados
vet18 = open('arquivo18.txt','r')
print("Lendo 10 inteiros do arquivo...")
A = list(map(int,vet18.readline().split(" ")))
print("Foram lidos ",len(A)," inteiros para o vetor A")
print(A)
x = int(input("Digite um inteiro a ser localizado:"))
#Processamento
A.append(x)     #insere x ao final
print(A)
i=0
while(A[i]!=x):
    i=i+1
A.pop(len(A)-1)
print(A)
if(i==len(A)):
    print("x não pertence ao vetor A")
else:
    print(x," esta na posição", i)
print("agora usando a função do python")
print(x," esta na posição",A.index(x))
vet18.close()
#Emissão de Relatório de saída





