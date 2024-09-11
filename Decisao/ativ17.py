# 17-Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.


ano=int(input("Digite um ano e eu direi se é bicesto: "))

terminacao=(ano%1000)%100

if(terminacao==0):
    if(ano%400==0):
        print("Ano Biscesto")
    else:
        print("Não é Bicesto")
else:
    if(ano%4==0):
        print("Ano Bicesto")
    else:
        print("Não é Bicesto")