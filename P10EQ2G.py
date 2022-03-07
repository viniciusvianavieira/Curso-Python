#P10EQ2G.py
#Universidade Federal Fluminense
#Escola de Engenharia
#TCC0326 Programcao de Computadores - T.D1 - Semestre 1/18 - DATA
#Professor John Reed
#Programador Caio Cardoso - Matricula: 017...
#P10EQ2G.py: classifica a equação do segundo grau segundo suas raízes
#Metodo: Peneira de "if`s", com Bhaskara
#
#Descrição dos objetos
#A: COEFICIENTE DE GRAU 2
#B: COEFICIENTE DE GRAU 1
#C: COEFICIENTE DE GRAU 0
#D: DELTA DE BHASKARA
#BOAS VINDAS
print("Bem vindo ao programa P10EQ2G: classifica a equação do segundo grau da forma Ax^2+Bx+C=0 segundo suas raízes")
#DIÁLOGO DE ENTRADA
A = float(input("\nDigite o coeficiente A: "))
B = float(input("\nInsira o coeficiente B: "))
C = float(input("\nInforme o coeficiente C: "))
#PROCESSAMENTO
D = (B**2) - (4*A*C)
if(D==0):
    print("\nEsta equação admite duas raízes reais iguais")
else:
    if(D>0):
        print("\nEsta equação admite duas raízes reais diferentes")
    else:
        if(B!=0):
            print("\nEsta equação admite duas raízes complexas")
        else:
            print("\nEsta equação admite duas raízes puramente imaginárias")
#EMISSÃO DO RELATÓRIO DE SAÍDA
#Neste programa o relatório de saída esta disperso no processamento
#DESPEDIDA
print("\nFim de execução!")
