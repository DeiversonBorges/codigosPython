# 8-Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.


n1=float(input("Digite o preço do produto 1: "))
n2=float(input("Digite o preço do produto 2: "))
n3=float(input("Digite o preço do produto 3: "))

if(n1!=n2 or n1!=n3 or n2!=n3):
    if(n1<=n2 and n1<=n3):
        print(f"O produto mais marato é o produto 1 que custa {n1}")
    elif(n2<=n3):
        print(f"O produto mais marato é o produto 2 que custa {n2}")
    else:
        print(f"O produto mais marato é o produto 2 que custa {n3}")
else:
    print("Todos os preços são iguais")