# 19-Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.

# Observando os termos no plural a colocação do "e", da vírgula entre outros.

# Exemplo:

# 326 = 3 centenas, 2 dezenas e 6 unidades

# 12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16



while(True):
    valor=int(input("Digite um valor: "))
    if(valor<1000):
        break
    else:
        print("É necessario um valor menor que 1000")

centena=valor//100
dezena=(valor%100)//10
unidade=(valor%100)%10

if(centena==dezena==unidade==0):
    print("O numero não tem centena, dezena ou unidade")


elif(centena==0):
    if(dezena==0):
        
        if(unidade>1):
            print(f"O número tem {unidade} unidades")
        else:
            print(f"O número tem {unidade} unidade")
    elif(dezena>1):
        if(unidade==0):
            print(f"O numero tem {dezena} dezenas")
        elif(unidade>1):
            print(f"O numero tem {dezena} dezenas e {unidade} unidades")
        else:
            print(f"O numero tem {dezena} dezenas e {unidade} unidade")
    else:
        if(unidade==0):
            print(f"O numero tem {dezena} dezena")
        elif(unidade>1):
            print(f"O numero tem {dezena} dezena e {unidade} unidades")
        else:
            print(f"O numero tem {dezena} dezena e {unidade} unidade")


elif(centena>1):
    if(dezena==0):
        if(unidade==0):
            print(f"O número tem {centena} centenas")
        elif(unidade>1):
            print(f"O número tem {centena} centenas e {unidade} unidades")
        else:
            print(f"O número tem {centena} centenas e {unidade} unidade")
    elif(dezena>1):
        if(unidade==0):
            print(f"O numero tem {centena} centenas e {dezena} dezenas")
        elif(unidade>1):
            print(f"O numero tem {centena} centenas, {dezena} dezenas e {unidade} unidades")
        else:
            print(f"O numero tem {centena} centenas, {dezena} dezenas e {unidade} unidade")
    else:
        if(unidade==0):
            print(f"O numero tem {centena} centenas e {dezena} dezena")
        elif(unidade>1):
            print(f"O numero tem {centena} centenas, {dezena} dezena e {unidade} unidades")
        else:
            print(f"O numero tem {centena} centenas, {dezena} dezena e {unidade} unidade")


else:
    if(dezena==0):
        if(unidade==0):
            print(f"O número tem {centena} centena")
        elif(unidade>1):
            print(f"O número tem {centena} centena e {unidade} unidades")
        else:
            print(f"O número tem {centena} centena e {unidade} unidade")
    elif(dezena>1):
        if(unidade==0):
            print(f"O numero tem {centena} centena e {dezena} dezenas")
        elif(unidade>1):
            print(f"O numero tem {centena} centena, {dezena} dezenas e {unidade} unidades")
        else:
            print(f"O numero tem {centena} centena, {dezena} dezenas e {unidade} unidade")
    else:
        if(unidade==0):
            print(f"O numero tem {centena} centena e {dezena} dezena")
        elif(unidade>1):
            print(f"O numero tem {centena} centena, {dezena} dezena e {unidade} unidades")
        else:
            print(f"O numero tem {centena} centena, {dezena} dezena e {unidade} unidade")     
    
