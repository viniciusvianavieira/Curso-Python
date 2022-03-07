#P6ABCRAP.py
#Universidade Federal Fluminense
#Escola de Engenharia
#TCC0326 Programcao de Computadores - T.D1 - Semestre 1/18 - DATA
#Professor John Reed
#Programador Caio Cardoso - Matricula: 017...
#P6ABCRAP.py: organiza os inteiros A,B,C, de forma que que ao final A<B<C
#Metodo: Trivial

#Resolução
#Casos: 123, 132, 213, 231, 312, 321
#Se (A>B) casos: 213, 312, 321
#   Se (B>C) caso: 321
#   print caso321
#   trocar A com C
#   Senão casos 213, 312
#      Se (A>C) caso: 312
#      print caso312
#      trocar A com B
#      trocar B com C
#      Senão caso 213
#      Print caso213
#      trocar A com B
#      fim do se
#   fim do se
#Senão casos: 123, 132, 231
#   Se(B>C) casos: 132, 231
#      Se(A>C) caso 231
#      print caso 231
#      trocar A com B
#      trocar A com C
#      Senão caso 132
#      print caso 132
#      trocar B com C
#      fim do se
#   fim do se
#fim do se
#print A,B,C

#Descricao dos objetos
# A,B, e C são números inteiros escolhidos pelo usuário
# Aux é uma variável que auxilia a ordenação dos números
#Boas vindas
print("Bem vindo ao programa P7VARABC: Ordena 3 números inteiros várias vezes\n\n")
#Dialogo de entrada de dados
A = int(input("Insira o primeiro número (A=0 para encerrar):\n"))
while(A!=0):
 B = int(input("Insira o segundo número:\n"))
 C = int(input("Insira o terceiro número\n"))
#Processamento
 if(A>B): # casos 2 1 3, 3 1 2, 3 2 1
    Aux=A
    A=B
    B=Aux # 2 1 3 --> 1 2 3 / 3 1 2 --> 1 3 2 / 3 2 1 --> 2 3 1
 if(B>C): # casos 1 3 2, 2 3 1
    Aux=C
    C=B
    B=Aux # 1 3 2 --> 1 2 3 / 2 3 1 --> 2 1 3
 if(A>B): #caso 2 1 3
    Aux=A
    A=B
    B=Aux # 2 1 3 --> 1 2 3
#Emissão do relatorio de saida
 print("\n",A,"<",B, "<",C)
 A = int(input("Insira o primeiro número (A=0 para encerrar):\n"))
#Despedida
print("\nExecução concluída!")