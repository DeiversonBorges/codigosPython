# 10-Foi realizada uma pesquisa de algumas características físicas da população de uma região, a qual coletou os seguintes dados referentes a cada habitante para ser analisado:

# Sexo (M - masculino / F - feminino);

# Cor dos olhos (1-azuis, 2-verdes ou 3-castanhos);

# Cor dos cabelos (1-louros, 2-castanhos, 3-pretos);

# Idade;

# Renda mensal.

# Obs: O final do conjunto de habitantes é reconhecido pelo valor -1 informado como idade. Com base nestas informações, escrever um programa que determine e escreva:

# A maior idade dos habitantes do grupo pesquisado;

# A média da idade dos habitantes;

# A quantidade de indivíduos do sexo masculino e feminino (separadamente);

# A quantidade de indivíduos do sexo feminino que está entre 18 e 35 anos de idade e que tenham olhos verdes e cabelos louros;

# A porcentagem de indivíduos que recebem até 3 salários mínimos mensais.
salarioMinimo=1400
maiorIdade=0
somatorio=0
contador=0
quantidadeSexoM=0
quantidadeSexoF=0
cenario4=0
cenario5=0
sexo=input('Digite seu sexo M para masculino e F para feminino: ').strip().lower()
olhos=int(input("Digite a cor dos olhos (1-azuis, 2-verdes ou 3-castanhos): "))
cabelo=int(input("Digite a cor dos cabelos (1-louros, 2-castanhos, 3-pretos: )"))
idade=float(input("Digite a idade: "))
renda=float(input("Digite sua renda mensal: "))

while(idade!=-1):
    if(idade>maiorIdade):
        maiorIdade=idade

    contador=contador+1
    somatorio=somatorio+idade

    if(sexo=='m'):
        quantidadeSexoM=quantidadeSexoM+1
    elif(sexo=='f'):
        quantidadeSexoF=quantidadeSexoF+1

    if(((idade>18)and(idade<35))and(olhos==2)and(cabelo==1)):
        cenario4=cenario4+1

    if(renda<=(salarioMinimo*3)):
        cenario5=cenario5+1

    sexo=input('Digite seu sexo M para masculino e F para feminino: ').strip().lower()
    olhos=int(input("Digite a cor dos olhos (1-azuis, 2-verdes ou 3-castanhos): "))
    cabelo=int(input("Digite a cor dos cabelos (1-louros, 2-castanhos, 3-pretos: )"))
    idade=float(input("Digite a idade: "))
    renda=float(input("Digite sua renda mensal: "))


mediaIdades=somatorio/contador

porcentagemCenario5=(cenario5/contador)*100

print(f'A maior idade do grupo pesquisado é {maiorIdade}\n a média das idades dos trabalhadores é {mediaIdades}\n a quantidade de indivídios do sexo masculino é {quantidadeSexoM} e a quantidade de indivíduos do sexo feminino é {quantidadeSexoF}\n a quantidade de indivíduos do sexo feminino que está entre 18 e 35 anos de idade e que tenham olhos verdes e cabelos louros é {cenario4} e a porcentagem de indivíduos que recebem até 3 salários mínimos mensais é {porcentagemCenario5}%. ')