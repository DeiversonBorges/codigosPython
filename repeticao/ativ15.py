# 15-(Hard)-Faça uma um programa que computa a potência a^b para valores a e b (assuma números inteiros) passados por parâmetro (não use o operador **)

base=int(input("Digite a base: "))
expoente=int(input("Digite o expoente: "))
potencia=base
for cont in range(expoente-1):
    potencia=potencia*base

print(f'A potência é {potencia}')