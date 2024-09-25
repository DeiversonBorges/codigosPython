# 1-Faça um programa que calcule a média de salários de uma empresa, pedindo ao usuário a quantidade de funcionários, o nome e o salário de cada funcionário e devolvendo a média, o salário mais alto e o salário mais baixo.


somador=0
maiorSalario=0
quantidadeFuncionarios=int(input("Digite a quantidade de Funcionários: "))

for cont in range(quantidadeFuncionarios):
    nome=input("Funcionário digite seu nome: ")
    salario=int(input("Funcionário digite seu salário: "))

    somador=somador+salario

    if(cont==0):
        menorSalario=salario
    
    if(salario>maiorSalario):
        maiorSalario=salario

    if(salario<menorSalario):
        menorSalario=salario

media=somador/quantidadeFuncionarios

print(f"A média é {media}, o maior salário é {maiorSalario} e o menor salário é {menorSalario}")
    
    