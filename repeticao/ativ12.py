# 12-O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:

# Lojas Tabajara
somador=0
contador=1
while(True):
    valor=float(input(f'Produto {contador}: R$ '))
    if(valor!=0):
        contador=contador+1
        somador=somador+valor
    else:
        print(f'Total: R$ {somador}')
        dinheiro=float(input('Dinheiro: R$ '))
        print(f'Troco: R$ {somador-dinheiro}')
        somador=0

