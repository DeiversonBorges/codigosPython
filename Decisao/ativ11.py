
# 11-As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.

# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:

# salários até 280,00 (incluindo): aumento de 20%

# salários entre 280,00 e 700,00: aumento de 15%

# salários entre 700,00 e 1500,00: aumento de 10%

# salários de R$ 1500,00 em diante: aumento de 5% Após o aumento ser realizado, informe na tela:

# salário antes do reajuste;
# percentual de aumento aplicado;
# valor do aumento;
# novo salário, após o aumento.



salario=float(input("Digite seu salário: "))

if (salario<=280):
    percentual=0.2
    aumento=salario*percentual
    novoSalario=salario+aumento
elif(salario<=700):
    percentual=0.15
    aumento=salario*percentual
    novoSalario=salario+aumento
elif(salario<1500):
    percentual=0.1
    aumento=salario*percentual
    novoSalario=salario+aumento
else:
    percentual=0.05
    aumento=salario*percentual
    novoSalario=salario+aumento

print(f"O valor do salário antes do reajuste é {salario}, o percentual do aumento aplicado é {percentual*100}%, o valor do aumento é {aumento} e o novo salário após o aumento é {novoSalario}")