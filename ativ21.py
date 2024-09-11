# 21-Considere que o último concurso vestibular apresentou três provas: Português, Matemática e Conhecimentos Gerais. Considerando que para cada candidato tem-se um registro contendo o seu nome e as notas obtidas em cada uma das provas, construa um algoritmo que forneça:

# a) o nome e as notas em cada prova do candidato

# b) a média do candidato

# c) uma informação dizendo se o candidato foi aprovado ou não. Considere que um candidato é aprovado se sua média for maior que 7.0 e se não apresentou nenhuma nota abaixo de 5.0


# nome=input("Digite seu nome: ")
# nota1=float(input("Digite sua nota em português: "))
# nota2=float(input("Digite sua nota em matemática: "))
# nota3=float(input("Digite sua nota em conhecimentos gerais: "))

# aluno=[nome,[nota1,nota2,nota3]]



aluno=[["João",10,9,4],["maria",1,2,3]]
soma=0
menor5=False
print(aluno[0])

print(f" O candidato {aluno[0][0]} teve uma nota de {aluno[0][1]} em português, {aluno[0][2]} em matemática e {aluno[0][3]} em Conhecimentos Gerais")

for a in range(3):
    soma=soma+aluno[0][a+1]

media=soma/3

for a in range(3):
    if(aluno[0][a+1]<5):
        menor5=True

print(f"A média do candidato é {media}")

if ((media>7) and (menor5==False)):
    print("APROVADO")
else:
    print("REPROVADO")
