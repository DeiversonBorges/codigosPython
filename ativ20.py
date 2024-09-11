# 20-Faça um algoritmo que leia um número de 1 a 5 e escreva por extenso. Caso o usuário digite um número que não esteja neste intervalo, exibir mensagem: número inválido.

n=int(input("Digite um número de 1 até 5 e ele será escrito por extenso: "))

match n:
    case 1:
        print("Um")
    case 2:
        print("Dois")
    case 3:
        print("Três")
    case 4:
        print("Quatro")
    case 5:
        print("Cinco")
    case _:
        print("Número Inválido")