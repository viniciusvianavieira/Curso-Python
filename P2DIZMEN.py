#P2DIZMAI.py
#Universidade Federal Fluminense
#Escola de Engenharia
#TCC0326 Programcao de Computadores - T.D1 - Semestre 1/18 - DATA
#Professor John Reed
#Programador Caio Cardoso - Matricula: 017...
#P2DIZMEN.py:
#Metodo: Trivial

#Descricao dos objetos
# n1 = Primeiro número inteiro
# n2 = Segundo número inteiro
#Boas vindas
print("Bem vindo ao programa P2DIZMAI: Informa o maior de dois inteiros\n")
#Dialogo de entrada de dados
n1 = int(input("Insira o primeiro numero: "))
n2 = int(input("Insira o segundo numero: "))
#Processamento
if(n1>n2):
   print("\nO maior é o primeiro")
else:
   if(n1 == n2):
      print("\nOs numeros sao iguais")
   else:
      print("\nO maior é o segundo")
#Emissão do relatorio de saida
#     Neste programa o relatorio de saida esta disperso no processamento
#Despedida
print("\nExecução concluida!")