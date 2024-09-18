# 0-Faça um programa que solicite o nome e a idade do usuário, depois disso exiba a mensagem: "{nome} possui {idade} anos.". Esta mensagem deve ser escrita em uma função.

def exibir(nome,idade):
    print(f"{nome} possui {idade} anos")

nome=input("Digite seu nome: ")
idade=int(input("Digite a sua idade: "))

exibir(nome,idade) 