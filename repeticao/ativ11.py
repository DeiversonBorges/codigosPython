# 11-Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

usuario=input('Digite seu nome de usuario: ')
senha=input('Digite sua senha: ')

while(usuario==senha):
    print("O nome de usuário não pode ser igual a senha.")
    usuario=input('Digite seu nome de usuario: ')
    senha=input('Digite sua senha: ')

print("Concluido!")