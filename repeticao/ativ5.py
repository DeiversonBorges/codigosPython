# 5-Foi feita uma pesquisa com um grupo de alunos de uma universidade, na qual se perguntou para cada aluno, o número de vezes que utilizou o restaurante da universidade no último mês. Construa um programa que determine:

# O percentual de alunos que utilizaram menos que 10 vezes o restaurante;
# O percentual de alunos que utilizaram entre 10 e 15 vezes;
# O percentual de alunos que utilizaram o restaurante acima de 15 vezes.


cenario1=0
cenario2=0
cenario3=0
numeroVezes=int(input("Digite quantas vezes você utilizou o restaurante no últimos mês: "))

while(numeroVezes!=-1):
    if(numeroVezes<10):
        cenario1=cenario1+1
    elif((numeroVezes>=10)and(numeroVezes<=15)):
        cenario2=cenario2+1
    else:
        cenario3=cenario3+1

    numeroVezes=int(input("Digite quantas vezes você utilizou o restaurante no últimos mês: "))



todosOsCenarios=cenario1+cenario2+cenario3

if(todosOsCenarios!=0):
    porcentagemCenario1=(cenario1/todosOsCenarios)*100
    porcentagemCenario2=(cenario2/todosOsCenarios)*100
    porcentagemCenario3=(cenario3/todosOsCenarios)*100
else:
    print("Ninguem digitou quantas vezes usou o restaurante: ")

print(f'O primeiro cenário resultou em {porcentagemCenario1}% dos alunos o segundo cenário resultou em {porcentagemCenario2}% dos alunos e o terceiro cenário resultou em {porcentagemCenario3}% dos alunos.')