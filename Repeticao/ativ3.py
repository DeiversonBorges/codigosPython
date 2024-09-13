multiplicando=int(input("Digite o multiplicando: "))
multiplicador=int(input("Digite o multiplicador: "))
produto=0
for contador in range(multiplicador):
    produto=produto+multiplicando

print(f"O produto é igual a {produto}")