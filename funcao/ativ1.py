def par_ou_impar(valor):
    if(valor%2==0):
        print("Par")
    else:
        print("Impar")

valor=int(input("Digite um valor e eu direi se ele é par ou é impar: "))
par_ou_impar(valor)