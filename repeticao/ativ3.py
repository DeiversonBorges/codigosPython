# 3.0-Sem utilizar a operação de multiplicação, escreva um programa que multiplique dois números inteiros. Por exemplo: 2 * 2 = 2 + 2.


multiplicando=int(input("Digite o multiplicando: "))
multiplicador=int(input("Digite o multiplicador: "))
produto=0
for contador in range(multiplicador):
    produto=produto+multiplicando

print(f"O produto é igual a {produto}")