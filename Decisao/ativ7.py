
# 7-Faça um Programa que leia três números e mostre o maior e o menor deles.



n1=float(input("Digite um numero: "))
n2=float(input("Digite outro numero: "))
n3=float(input("Digite mais um numero: "))

if(n1!=n2 or n1!=n3 or n2!=n3):
    if(n1>=n2 and n1>=n3):
        if(n2>=n3):
            print(f"O Maior é {n1} e o menor {n3}")
        else:
            print(f"O Maior é {n1} e o menor {n2}")
    elif(n2>=n3):
        if(n3>=n1):
            print(f"O Maior é {n2} e o menor {n1}")
        else:
            print(f"O Maior é {n2} e o menor {n1}")
    else:
        if(n2>=n1):
            print(f"O Maior é {n3} e o menor {n1}")
        else:
            print(f"O Maior é {n3} e o menor {n2}")  
else:
    print("Todos os valores são iguais")