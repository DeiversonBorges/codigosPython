# 1-Faça um Programa que peça dois números e imprima o maior deles.


n1=float(input("Digite um numero "))
n2=float(input("Digite outro numero "))

if (n1==n2):
    print("Nenhum desses numeros é maior que o outro")
elif(n1>n2):
    print(f"{n1} é maior que {n2}")
else:
    print(f"{n2} é maior que {n1}")