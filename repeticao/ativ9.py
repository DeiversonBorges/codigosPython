# 9-Num frigorífico existem 100 bois. Cada boi traz em seu pescoço um cartão contendo seu número de identificação e seu peso. Faça um algoritmo que escreva o número de identificação do boi e o peso do boi mais gordo e do boi mais magro.

maiorboi=0
idDoMaior=0
menorBoi=0
idDoMenor=0

for a in range(100):
    id=int(input("Digite a identificação do boi: "))
    peso=float(input("Digite o peso do boi: "))

    if(a==0):
        menorBoi=peso
    
    if(peso>maiorboi):
        maiorboi=peso
        idDoMaior=id
    
    if (peso<menorBoi):
        menorBoi=peso
        idDoMenor=id

print(f'O boi com maior peso pesa {maiorboi} com identificação de {idDoMaior}\n e o boi de menor peso pesa {menorBoi} e seu identificador é {idDoMenor}.')