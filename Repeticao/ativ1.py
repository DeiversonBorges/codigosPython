# 1-Faça um programa que calcule a média de salários de uma empresa, pedindo ao usuário a quantidade de funcionários, o nome e o salário de cada funcionário e devolvendo a média, o salário mais alto e o salário mais baixo.

quantidade=int(input("Digite a quantidade de funcionários da sua empresa: "))
somador=0
maiorSalario=0
menorSalario=0
for contador in range(quantidade):
    nome=input("Digite seu nome: ")
    salario=float(input("Digite seu salário: "))
    if (contador==0):
        menorSalario=salario

    somador=somador+salario

    if(salario>maiorSalario):
        maiorSalario=salario

    if(salario<menorSalario):
        menorSalario=salario

print(f"A média de salário é {somador/quantidade} o salário mais alto é {maiorSalario} e o salário mais baixo é {menorSalario}")
    