
# 13- O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas. (use o valor 999 para encerrar)

maiorTemperatura=0
somador=0
contador=0
primeiroMenorValor=False

temperatura=int(input("Digite a temperatura: "))

while(temperatura!=999):
    

    somador=somador+temperatura
    contador=contador+1

    if(primeiroMenorValor==False):
        menorTemperatura=temperatura
        primeiroMenorValor=True
    
    if(temperatura>maiorTemperatura):
        maiorTemperatura=temperatura

    if(temperatura<menorTemperatura):
        menorTemperatura=temperatura

    temperatura=int(input("Digite a temperatura: "))
if(contador!=0):
    print(f'A menor temperatura é {menorTemperatura} a maior temperatura é {maiorTemperatura} e a média das temperaturas é {somador/contador}')
else:
    print("Não foram digitados valores.")
