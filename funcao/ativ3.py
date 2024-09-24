# 3-Crie uma função chamada "calculadora" que receba dois números e uma operação matemática 
# (soma, subtração, multiplicação ou divisão) como parâmetros e retorne o resultado da operação escolhida.

def calculadora(valor1,valor2,operacao):
    match operacao:
        case "*":
            resultado=valor1*valor2
        case "/":
            resultado=valor1/valor2
        case "+":
            resultado=valor1+valor2
        case "-":
            resultado=valor1-valor2
    return resultado


valor1=int(input("Digite um valor: "))
valor2=int(input("Digite outro valor: "))
valor3=input("Digite a operação * para multiplicação + para adição - para subtração e / para divisão: ")

print(f"O resultado é {calculadora(valor1,valor2,valor3)}")