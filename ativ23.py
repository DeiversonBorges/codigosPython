# 23-Uma empresa produz três tipos de peças mecânicas: parafusos, porcas e arruelas. Têm-se os preços unitários de cada tipo de peça e sabe-se que sobre estes preços incidem descontos de 10% para porcas, 20% para parafusos e 30% para arruelas. Escreva um programa que calcule o valor total da compra de um cliente. Deve ser mostrado o nome do cliente. O número de cada tipo de peça que o mesmo comprou, o total de desconto e o total a pagar pela compra.





print("Porcas R$ 3,00(10% de desconto); Parafusos R$ 5,00(20% de desconto) e Arruelas R$ 4,00(30% desconto)")


nome=input("Digite seu nome: ")
porca=int(input("Digite quantas porcas deseja comprar: "))
parafuso=int(input("Digite quantos parafusos deseja comprar: "))
arruela=int(input("Digite quantas arruelas deseja comprar: "))

totPorca=3*porca
totParafuso=5*parafuso
totArruela=4*arruela
total=totPorca+totParafuso+totArruela


descontoPorca=totPorca*0.1
descontoParafuso=totParafuso*0.2
descntoArruela=totArruela*0.3
totalDesconto=descontoPorca+descontoParafuso+descntoArruela

print(f"Cliente {nome} o valor total da compra foi de {total}, foi comprado {porca} porca(s), {parafuso} parafuso(s) e {arruela} arruela(s), o total de descontos foi de {totalDesconto} e o total a pagar é de {total-totalDesconto}")