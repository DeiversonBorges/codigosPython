# 4-Escreva uma função que receba dois números e retorne True se o primeiro número for múltiplo do segundo.
# Valores esperados:

def multiplo(numero1,numero2):
    if(numero1%numero2==0):
        return True
    else:
        return False        



numero1=int(input("Digite uma número: "))
numero2=int(input("Digite outro número: "))

if(multiplo(numero1,numero2)):
    print("O primeiro é multiplo do segundo")
else:
    print("O primeiro não é multiplo do segundo")
