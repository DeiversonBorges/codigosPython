# 10-Crie uma função “verificar_senha” no qual retorna true caso a senha inserida for correta e false caso o contrário. 
# Logo após elabore um “mini-sistema” de checar a senha inserida, 
# onde o usuário tem 3 tentativas de senha e caso esse número seja ultrapassado o programa é encerrado.

def verificar_senha(senha):
    if(senha=='123'):
        return True
    else:
        return False
    
cont=0
while(cont<=2):
    senha=input("Digite sua senha: ")

    if(verificar_senha(senha)==True):
        print("Senha Correta!")
        break
    else:
        print("Senha Incorreta!")
        cont=cont+1


if(cont==3):
    print("Limite Atingido!")