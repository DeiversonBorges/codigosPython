# 1-Crie uma função chamada "par_ou_impar" que receba um número como parâmetro e retorne se o número é par ou ímpar.

def par_ou_impar(valor):
    if(valor%2==0):
        print("Par")
    else:
        print("Impar")

valor=int(input("Digite um valor e eu direi se ele é par ou é impar: "))
par_ou_impar(valor)