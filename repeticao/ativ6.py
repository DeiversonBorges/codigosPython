# 6-Foi realizada uma pesquisa de algumas características físicas da população de uma certa região, a qual coletaram os seguintes dados referentes a cada habitante para serem analisados:

# sexo (masculino e feminino)
# cor dos olhos (azuis, verdes ou castanhos)
# cor dos cabelos (louros, castanhos, pretos)
# idade
# Faça um um programa que determine e escreva:

# a maior idade dos habitantes;
# a quantidade de indivíduos do sexo feminino cuja idade está entre 18 e 35 anos, inclusive;
# a quantidade de indivíduos que tenham olhos verdes e cabelos louros;
# O final do conjunto de habitantes é reconhecido pelo valor -1 informado como idade.

maiorIdade=0
cenario2=0
cenario3=0


sexo=input("Digite seu sexo M para masculino e F para feminino: ").strip().lower()
olhos=input('Digite sua cor dos olhos "A" para azuis "V" para verdes e "C" para castanhos: ' ).strip().lower()
cabelos=input('Digite a cor dos seus cabelos "L" para louros, "C" para castanhos e "P" para pretos: ').strip().lower()
idade=int(input("Digite sua idade: "))

while(idade!=-1):

    if(idade>maiorIdade):
        maiorIdade=idade


    if((sexo=='f') and ((idade>=18)and(idade<=35))):
        cenario2=cenario2+1


    if((olhos=='v') and (cabelos=='l')):
        cenario3=cenario3+1

    sexo=input("Digite seu sexo M para masculino e F para feminino: ").strip().lower()
    olhos=input('Digite sua cor dos olhos "A" para azuis "V" para verdes e "C" para castanhos: ' ).strip().lower()
    cabelos=input('Digite a cor dos seus cabelos "L" para louros, "C" para castanhos e "P" para pretos: ').strip().lower()
    idade=int(input("Digite sua idade: "))

print(f' A maior idade é {maiorIdade}, a quantidade de indivídos do sexo feminino com idade entre 18 e 35 é {cenario2} e a quantidade de indivídios de olhos verdes e cabelos louros é {cenario3}.')