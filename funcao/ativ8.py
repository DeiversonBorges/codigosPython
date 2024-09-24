# 8-Faça um programa que solicite ao usuário três números diferentes e exiba o dobro do maior número. 
# Para fazer isso separe seu código em duas funções diferentes: Uma função para retornar o maior dos três números e outra função para dobrar o número.


def maior(valor1,valor2,valor3):
    if((valor1>valor2) and (valor1>valor3)):
        return valor1
    elif(valor2>valor3):
        return valor2
    else:
        return valor3
    
def dobra(valor1):
    return valor1*2

valor1=float(input("Digite um valor: "))
valor2=float(input("Digite outro valor: "))
valor3=float(input("Digite mais outro valor: "))


print(f"O dobro do maior valor quue você digitou é {dobra(maior(valor1,valor2,valor3))}")