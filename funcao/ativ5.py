# 5-Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo 
# de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.

def funcaoImposto(taxaImposto,custo):
    return custo+(custo*(taxaImposto/100))

custo=float(input("Digite o custo: "))
taxaImposto=float(input("Digite sua porcentagem: "))

print(f"O valor da venda com a porcentagem é {funcaoImposto(custo,taxaImposto)} ")