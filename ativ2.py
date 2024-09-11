# 2-Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

n=float(input("Digite um valor e eu direi se ele é positivo ou negativo "))

if(n==0):
    print(f"{n} Não é positivo e nem negativo")
elif(n>0):
    print(f"{n} É positivo")
else:
    print(f"{n} É negativo")