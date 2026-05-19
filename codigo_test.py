#DESAFIO 2.0
senha= input("Digite sua senha: ")
letras_min=0 #Criar variaveis, para inicar uma contagem
letras_max=0 #Criar variaveis, para inicar uma contagem
numeros=0 #Criar variaveis, para inicar uma contagem
caracteres=0 #Criar variaveis, para inicar uma contagem
for letra in senha : #for para repetir essas etapas para todos os caracteres
    if letra.isupper(): #contar quantas letras maiusculas existem
        letras_max+=1
    elif letra.islower(): #contar quantas letras minusculas existem
        letras_min+=1
    elif letra.isdigit(): #contar quantos numeros tem
        numeros+=1
    elif not letra.isalnum():
        caracteres+=1
letras_totais= letras_min + letras_max #criar variavel após o "for", pois assim ela consegue analisar o valor novo não o 0
if len(senha)>=8 and numeros>0 and letras_min>0 and letras_max>0 and caracteres>0:
    print("Senha Forte!")
elif len(senha)>=8 and numeros>0 and letras_totais>0:
    print("Senha Média!")
elif len(senha)<8:
    print("Senha Fraca")

resposta = input("Deseja saber informações da sua senha?\n").upper()
if resposta == "SIM":
    print("Total de caracteres:", len(senha))
    print("Letras minúsculas:", letras_min)
    print("Letras maiúsculas:", letras_max)
    print("Números:", numeros)
    print("Caracteres especiais:", caracteres)
else:
    print("OK!")