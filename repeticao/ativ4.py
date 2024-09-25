# 4-Faça um programa que leia um conjunto de números (X) e imprima a quantidade de números pares (QPares) e a quantidade de números impares (QImpares) lidos. Admita que o valor 9999 é utilizado como sentinela para fim de leitura.



par=0
impar=0

numero=int(input("Digite um conunto de números inteiros e eu direi se é par ou impar, digite 9999 para encerrar a verificação: "))

while(numero!=9999):
    

    if(numero%2==0):
        par=par+1
    else:
        impar=impar+1

    numero=int(input("Digite um conunto de números inteiros e eu direi se é par ou impar, digite 9999 para encerrar a verificação: "))

print(f"A quantidade de números pares é {par} e de impares é {impar}")