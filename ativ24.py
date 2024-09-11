
# Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.

n=int(input("Digite um número e eu direi se ele é primo ou não: "))
if(n==2):
    primo=True
else:    
    for a in range(n-2):
        if(n%(a+2)==0):
            primo=False
            break
        else:
            primo=True

if(primo==True):
    print("É primo")
else:
    print("Não é primo")

#Meu objetivo aqui é garantir que sejam analizados os numeros acima de um e do próprio número para isso eu tive que adicionar 2 na contagem para eliminar o 0 e 1 da análise de divisão(linha 9) e compensei essa diferença no range subtrainda a quantidade de vezes que será contada por 2(linha 8)