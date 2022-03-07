#P13EQ2GP.py
#Universidade Federal Fluminense
#Escola de Engenharia
#TCC0326 Programcao de Computadores - T.D1 - Semestre 1/18 - DATA
#Professor John Reed
#Programador Caio Cardoso - Matricula: 017...
#P13EQ2GP.py: classifica a equação do segundo grau segundo suas raízes, e as calcula com eficiência
#Metodo: Peneira de "if`s", com Bhaskara
#
#Descrição dos objetos
#A: COEFICIENTE DE GRAU 2
#B: COEFICIENTE DE GRAU 1
#C: COEFICIENTE DE GRAU 0
#D: DELTA DE BHASKARA
#X1: PRIMEIRA RAÍZ
#X2: SEGUNDA RAÍZ
#R: PARTE REAL DA RAÍZ COMPLEXA
#I: PARTE IMAGINÁRIA DA RAÍZ COMPLEXA
#BOAS VINDAS
print("Bem vindo ao programa P13EQ2GP: classifica a equação do segundo grau da forma Ax^2+Bx+C=0 segundo suas raízes, e as calcula")
#DIÁLOGO DE ENTRADA
A = float(input("\nDigite o coeficiente A: "))
B = float(input("\nInsira o coeficiente B: "))
C = float(input("\nInforme o coeficiente C: "))
#PROCESSAMENTO
D = (B*B)-((A+A)*(C+C))       #(B**2) - (4*A*C)
AA=A+A
X1=((-B)+((B**2)-(4*A*C))**(1/2))/AA
X2=((-B)-((B**2)-(4*A*C))**(1/2))/AA
print("X1:",X1,"\nX2:",X2)
if(D==0):
    print("\nEsta equação admite duas raízes reais iguais")
    X1 = (-B)/(A+A)           #(-B/(2*A))
    X2 = X1
    print("X1:",X1,"\nX2:",X2)
else:
    if(D>0):
        print("\nEsta equação admite duas raízes reais diferentes")
        X1 = ((-B)+D**(0.5))/(A+A)       #((-B) + D**(1/2))/ (2*A)
        X2 = ((-B)-D**(0.5))/(A+A)       #((-B) - D**(1/2))/ (2*A)
        print("X1:", X1, "\nX2:", X2)
    else:
        I = ((-D) ** (0.5)) / (A + A)  # ((-D)**(1/2))/(2*A)
        if(B!=0):
            print("\nEsta equação admite duas raízes complexas")
            R = (-B)/(A+A)              #(-B)/(2*A)
            print("X1:", R ,"+", I ,"i", "\nX2:", R ,"-", I ,"i")
        else:
            print("\nEsta equação admite duas raízes puramente imaginárias")
            print("X1: +", I , "i" , "\nX2: -", I , "i")
#EMISSÃO DO RELATÓRIO DE SAÍDA
#Neste programa o relatório de saída esta disperso no processamento
#DESPEDIDA
print("\nFim de execução!")