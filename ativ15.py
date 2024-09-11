
# 15-Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

# Dicas:

# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;

# Triângulo Equilátero: três lados iguais;

# Triângulo Isósceles: quaisquer dois lados iguais;

# Triângulo Escaleno: três lados diferentes;




lado1=float(input("Escreva o primeiro lado do triângulo: "))
lado2=float(input("Escreva o segundo lado do triângulo: "))
lado3=float(input("Escreva o terceiro lado do triângulo: "))

if((lado1+lado2>lado3) and (lado1+lado3>lado2) and (lado3+lado2>lado1)):
    if(lado1==lado2==lado3):
        print("Triângulo Equilatero")
    elif((lado1==lado2) or (lado1==lado3) or (lado3==lado2)):
        print("Triângulo Isoseles")
    else:
        print("Triângulo Escaleno")
else:
    print("Esses valores não podem ser um triângulo")