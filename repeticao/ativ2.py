# 2-Um hotel com 30 quartos cobra R$ 50,00 por diária e mais uma taxa de serviços. A taxa de serviços é de:

# • R 4,00 por diária, se o número de diárias for < 15;

# • R 3,60 por diária, se o número de diárias for = 15;

# • R 3,00 por diária, se o número de diárias for > 15.

# Faça um programa que imprima o nome e o total da conta de cada cliente do hotel. Imprima também o total ganho pelo hotel.




numeroQuartos=4

for contador in range(numeroQuartos):
    nome=input("Digite seu nome: ")
    dias=int(input("Digite a quantidade de dias que você ficou: "))

    if (dias==15):
        total=(50+4)*dias
    elif(dias>15):
        total=(50+3)*dias
    else:
        total=(50+3.6)*dias
    
    print(f"Olá, cliente {nome}, o total da sua conta é {total}")