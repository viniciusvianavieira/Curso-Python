#P14SEQSF.py
#Universidade Federal Fluminense
#Escola de Engenharia
#TCC0326 Programcao de Computadores - T.D1 - Semestre 1/18 - DATA
#Professor John Reed
#Programador Caio Cardoso - Matricula: 017...
#P14SEQSF.py: gera sequências
#Metodo: "FOR"

#Descrição dos objetos
#Cont: variável de contagem
#Processamento
#Sequência A
print("1,2,3,...,10")
#Cont=1                              #Inicialização
#while(Cont<=10):
#  print(Cont)                        #Utilização
#  Cont = Cont + 1                    #Atualização
for i in range(1,(10+1),1):
    print(i)
#Sequência B
print("2,4,6,...,20")
#Cont = 2                             # Inicialização
#while (Cont <= 20):
#  print(Cont)                        # Utilização
#  Cont = Cont + 2                   #Atualizção
for i in range(2,(20+1),2):
    print(i)
#Seqência C
print("Múltiplos de 3 entre 3 e 30")
#Cont=3                              #Inicialização
#while(Cont<=30):
#  print(Cont)                        #Utilização
#  Cont = Cont + 3                   #Atualização
for i in range(3,(30+1),3):
    print(i)
#Sequência D
print("10,9,8,...,1")
#Cont=10                               #Inicialização
#while(Cont>=1):
#  print(Cont)                        #Utilização
#  Cont = Cont - 1                    #Atualização
for i in range(10,(1-1),-1):
    print(i)
#Sequência E
print("1,9,2,8,3,7,4,6,5,5")
#Cont=1                             #Inicialização
#while(Cont<=5):
# print(Cont)                        #Utilização
# print(10-Cont)                     #Atualização
# Cont = Cont + 1                    #Atualização.2
for i in range(1,(5+1),1):
    print(i)
    print(10-i)

#Sequência F
print("1,2,4,8,...,512")
#cont=1                            #Inicialização
#while(cont<=512):
#    print(cont)                   #Utilização
#    cont=cont + cont              #Atualizaçãp
P=1
for i in range(1,(10+1),1):
    print(P)
    P=P+P
#Sequência G
print("1,4,27,...,10000000000")
#Cont=1                            #Inicialização
#while(Cont<=10):
#  print(Cont**Cont)
#  Cont= Cont + 1
for i in range(1,(10+1),1):
    print(i**i)
#Sequência H
print("Múltiplos de 51 entre 25482 e 25992")
#Cont= (25482-25482%51)+51                            #Inicialização
#while(Cont<=26592):
#  print(Cont)                                   #Utilização
#  Cont = Cont + 51                              #Atualização
for i in range(((25482-25482%51)+51),(25992+1),51):
    print(i)
    '''
#Sequência I
print("1,1,2,3,... (10 elementos)")
p=1
print(p)
u=1
print(u)
cont=3
while(cont<=50):
  f=u+p
  print(f, f/u)
  p=u
  u=f
  cont=cont+1
#Sequência J
print("2,4,2,4,2,4,2")
S=2
cont=1
while(cont<=7):
  print(S)
  S=6-S
  cont=cont+1
'''