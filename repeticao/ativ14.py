# 14-Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:

# Tabuada de 5:

# 5 X 1 = 5

# 5 X 2 = 10

# ...

# 5 X 10 = 50

tabuada=int(input("Digite um número inteiro e eu vou gerar a tabuada de 1 até 10 dele: "))

for cont in range(1,11,1):
    print(f'{tabuada}X{cont}={tabuada*cont}')