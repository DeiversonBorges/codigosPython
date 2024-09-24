# 9-Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta. 
# O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função valorPagamento,
# que calculará o valor a ser pago e devolverá este valor ao programa que a chamou.
# O programa deverá então exibir o valor a ser pago na tela. 
# Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação. 
# Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia. 
# O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor da prestação. 
# Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.

def valorPagamento(prestacao,diasAtrasados):
    if(diasAtrasados==0):
        return prestacao
    else:
        multa=0.03
        juros=0.001*diasAtrasados
        return prestacao+(prestacao*(multa+juros))
    
prestacao=float(input("Digite a sua prestação ou 0 para sair: "))
if(prestacao!=0):
    diasAtrasados=int(input("Digite a quantidade de dias atrasados: "))
cont=0
somador=0
while(prestacao!=0):
    valorPagamento1=valorPagamento(prestacao,diasAtrasados)
    print(f"O valor a ser pago é {valorPagamento1}")
    cont=cont+1
    somador=somador+valorPagamento1
    prestacao=float(input("Digite a sua prestação ou 0 para sair: "))
    if(prestacao!=0):
        diasAtrasados=int(input("Digite a quantidade de dias atrasados: "))

print(f"O valor de contas pagas no dia é de {cont} e o valor total das prestações é {somador}")