# 2-Fazer uma função que recebe três argumentos, e que retorne o produto desses três argumentos.

def somar(valor1,valor2,valor3):
    soma=valor1*valor2*valor3
    return soma

valor1=int(input("Digite um valor: "))
valor2=int(input("Digite outro valor: "))
valor3=int(input("Digite mais um valor: "))



print(f"A soma é {somar(valor1,valor2,valor3)}")