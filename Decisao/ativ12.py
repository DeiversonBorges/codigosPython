# 12-Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

# Desconto do IR:

# Salário Bruto até 900 (inclusive) - isento

# Salário Bruto até 1500 (inclusive) - desconto de 5%

# Salário Bruto até 2500 (inclusive) - desconto de 10%

# Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.

# Exemplo:

# Salário Bruto: (5 * 220)          : R$ 1100,00
#   (-) IR (5%)                     : R$   55,00  
#   (-) INSS ( 10%)                 : R$  110,00
#   FGTS (11%)                      : R$  121,00
#   Total de descontos              : R$  165,00
#   Salário Liquido                 : R$  935,00




valorHora=float(input("Digite o valor da sua hora: "))
hora=int(input("Digite o valor da hora trabalhada no mês: "))
salario=valorHora*hora
Taxafgts=0.11
sind=0.03
if(salario<=900):
    impRenda=0
    liquido=salario-salario*sind
elif(salario<=1500):
    impRenda=0.05
    liquido=salario-salario*(sind+impRenda)
elif(salario<=2500):
    impRenda=0.1
    liquido=salario-salario*(sind+impRenda)
else:
    impRenda=0.2
    liquido=salario-salario*(sind+impRenda)

print(f"Salário Bruto:({hora}*{valorHora})                  :R${salario} \n IR-({impRenda*100}%)                    :R${salario*impRenda} \n FGTS-({Taxafgts*100}%)                 :R${salario*Taxafgts} \n Total de Descontos                 :R${salario*(sind+impRenda)} \n Salário liquido                 :R${liquido}")


