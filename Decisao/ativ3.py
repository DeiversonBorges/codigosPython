
# 3-Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.


sexo=input("Digite M para masculino e F para feminino: ").lower().strip()

if(sexo=="m"):
    print("Sexo Masculino")
elif(sexo=="f"):
    print("Sexo Feminino")
else:
    print("Sexo Invalido")