#P4TRIANG.PY
#Universidade Federal Fluminense
#Escola de Engenharia
#TCC0326 Programcao de Computadores - T.D1 - Semestre 1/18 - DATA
#Professor John Reed
#Programador Caio Cardoso - Matricula: 017...
#P4TRIANG: Lê 3 lados de um triângulo e diz se é equilátero, isósceles, qualquer ou inexistente(por heron)
#Metodo: Trivial

#Descricao dos objetos
# A = primeiro lado do triângulo
# B = segundo lado do triângulo
# C = terceiro lado do triângulo
# p = semiperímetro

#Boas vindas
print("Bem vindo ao programa P4TRIANG: Lê 3 lados de um triângulo e o classifica \n\n")

#Dialogo de entrada de dados
A = int(input("Insira o primeiro lado:"))
B = int(input("Informe o segundo lado:"))
C = int(input("Digite o terceiro lado:"))

#Processamento
p = float((A+B+C)/2)
#print("\n p:",p)
if((p*(p-A)*(p-B)*(p-C)) > 0):
    if(A==B):
        if(B==C):
            print("Triângulo equilátero")
        else:
            print("Triângulo isósceles")
    else:
        if(B==C):
            print("Triângulo isósceles")
        else:
            if(A==C):
                print("Triângulo isósceles")
            else:
                print("Triângulo Escaleno")
else:
    print("Triângulo não existe")
#Emissão do relatorio de saida
#
#Despedida
print("\nExecucao concluída!")