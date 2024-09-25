# 7-Escreva um programa que exiba uma lista de opções (menu): adição, subtração, divisão, multiplicação e sair. Imprima o cálculo da operação escolhida. Repita até que a opção saída seja escolhida.

while(True):
    escolha=int(input(f"Escolha uma das opções:\n Adição-1\n Subtração-2\n Multiplicação-3\n Divisão-4\n Sair-5: "))

    match(escolha):
        case 1:
            parcela1=float(input("Digite uma parcela: "))
            parcela2=float(input("Digite uma outra parcela: "))
            print(f'A soma ou produto é {parcela1+parcela2}')
        case 2:
            minuendo=float(input("Digite o minuendo: "))
            subtraendo=float(input("Digite o subtraendo: "))
            print(f" A diferença é {minuendo-subtraendo}")
        case 3:
            multiplicando=float(input("Digite o multiplicando: "))
            multiplicador=float(input("Digite o multiplicador: "))
            print(f"O produto é {multiplicando*multiplicador}")
        case 4:
            dividendo=float(input("Digite o dividendo: "))
            divisor=float(input("Digite o divisor: "))
            print(f'O quociente é {dividendo/divisor}')
        case 5:
            break