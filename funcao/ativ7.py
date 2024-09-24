# 7-Escreva uma função que recebe um número como parâmetro e para cada número menor que o parâmetro, a função imprime "Fizz" se o número for múltiplo de três,
#  imprime "Buzz" se o número for múltiplo de cinco, e imprime "FizzBuzz" se o número for múltiplo de três e cinco.
#  Caso o número não seja múltiplo nem de três nem de cinco, ele deve ser impresso. 
# Note que, ao contrário das funções anteriores, sua função não deve retornar nada. Ela precisa simplesmente imprimir o que foi pedido.

def multiplo(valor):
    for cont in range(0,valor,1):
        if((cont%3==0)and(cont%5==0)):
            print("FizzBuzz")
        elif(cont%3==0):
            print("Fizz")
        elif(cont%5==0):
            print("Buzz")
        else:
            print(cont)

valor=int(input("Digite um valor: "))

multiplo(valor)