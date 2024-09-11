# 16-Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:

# Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
# Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
# Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
# Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;




a=float(input("Digite o valor de A: "))
if(a==0):
    print("Se A é igual a zero não é uma equação do segundo grau")
else:
    b=float(input("Digite o valor de B: "))
    c=float(input("Digite o valor de C: "))
    delta=(b**2)-(4*a*c)
    if(delta<0):
        print("Sua equação não possui raizes")
    elif(delta==0):
        raizUnica=-b/(2*a)
        print(f"A raiz única da sua equação é: {raizUnica}")
    else:
        raiz1=(-b+(delta**0.5))/(2*a)
        raiz2=(-b-(delta**0.5))/(2*a)
        print(f"As raizes da sua equação são {raiz1} e {raiz2}")