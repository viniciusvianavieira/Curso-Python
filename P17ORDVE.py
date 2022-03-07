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
print("Bem vindo ao programa P17ORDVE: Ordena um vetor em orde crescente\n")
#Diálogo de entrada de dados
x=input("Digite o nome do arquivo:")
vet4 = open(x,'r')
print("Lendo 10 inteiros do arquivo...")
A = list(map(int,vet4.readline().split(" ")))
print("Foram lidos ",len(A)," inteiros para o vetor A")
print(A)
print("Função min: ",min(A)," posição ", A.index(min(A)))
print("Função max: ",max(A)," posição ", A.index(max(A)))
print("Função sorted: ",sorted(A))
#Processamento
for F in range(0,(8+1),1):        #Ordena até o penúltimo
    m=F                           #Hipótese inicial para esta fronteira
    for i in range(F+1,(9+1),1):
        if(A[i]<A[m]):
            m=i
    Aux = A[m]
    A[m]= A[F]
    A[F]= Aux
vet4.close()
#Emissão de relatório de saída
print("Após a ordenação A ficou:\n",A)
#Despedida
print("Execução concluída!")