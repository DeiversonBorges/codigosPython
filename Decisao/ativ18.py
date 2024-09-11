# 18-Uma empresa de vendas tem três corretores. A empresa paga ao corretor uma comissão calculada de acordo com o valor de suas vendas.

# Se o valor da venda de um corretor for maior que R$ 50.000.00 a comissão será de 12% do valor vendido.

# Se o valor da venda do corretor estiver entre R$ 30.000.00 e R50.000.00 (incluindo extremos) a comissão será de 9.5%.

# Em qualquer outro caso, a comissão será de 7%. Escreva um algoritmo que gere um relatório contendo nome, valor da venda e comissão de cada um dos corretores. O relatório deve mostrar também o total de vendas da empresa


totVenda=0
for i in range(3):

    nome=input("Digite seu nome: ")
    venda=int(input("Digite o valor da venda: "))

    if((venda>30000) and (venda<50000)):
        comissao=venda*0.095
    elif(venda>=50000):
        comissao=venda*0.12
    else:
        comissao=venda*0.07
    totVenda=totVenda+venda
    print(f"Corretor: {nome}, sua venda foi de {venda} e sua comissão foi de {comissao}")

print(f"O total de vendas da empresa foi de {totVenda}")