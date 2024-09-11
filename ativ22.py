# 22-Um hotel cobra R$ 60.00 a diária e mais uma taxa de serviços. A taxa de serviços é de:

# • R$ 5.50 por diária, se o número de diárias for maior que 15;

# • R$ 6.00 por diária, se o número de diárias for igual a 15;

# • R$ 8.00 por diária, se o número de diárias for menor que 15.

# Construa um algoritmo que mostre o nome e o total da conta de um cliente


nome=input("Digite seu nome: ")
dias=int(input("Digite quantos dias você ficou: "))

diaria=60

if (dias==15):
    taxa=6
elif(dias>15):
    taxa=5.5
else:
    taxa=8

print(f"Hóspede {nome} e total da sua conta é {(diaria+taxa)*dias}")