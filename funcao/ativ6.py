# 6-Escreva uma função para imprimir o valor absoluto de um número.

def valorAbsoluto(valor):
    if valor<0:
        return -(valor)
    else:
        return valor

valor=float(input("Digite um valor e eu direi o seu valor absoluto: "))

print(f"O valor absoluto é {valorAbsoluto(valor)}")