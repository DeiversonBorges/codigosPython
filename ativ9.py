# 9-Faça um Programa que leia três números e mostre-os em ordem decrescente.

n1=float(input("Digite um numero: "))
n2=float(input("Digite outro numero: "))
n3=float(input("Digite mais um numero: "))

if(n1!=n2 or n1!=n3 or n2!=n3):
    if(n1>=n2 and n1>=n3):
        if(n2>=n3):
            print(f"{n1},{n2},{n3}")
        else:
            print(f"{n1},{n3},{n2}")
    elif(n2>=n3):
        if(n3>=n1):
            print(f"{n2},{n3},{n1}")
        else:
            print(f"{n2},{n1},{n3}")
    else:
        if(n2>=n1):
            print(f"{n3},{n2},{n1}")
        else:
            print(f"{n1},{n1},{n2}") 
else:
    print(f"{n1},{n2},{n3}")