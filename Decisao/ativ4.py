# 4-Faça um Programa que verifique se uma letra digitada é vogal ou consoante.


l=input("Digite uma letra e eu direi se é volgal ou consoante: ")
letra=l.lower().strip()
if(letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u"): #if letra in "aeiou":
    print(f"{l} é vogal")
else:
    print(f"{l} é consoante")