pontuacao_final = 0

print("Seja bem vindo ao meu quiz sobre programação!")
nome = input("Insira seu nome: ")
print(nome)
comecar = input("Deseja começar o quiz? (S/N) ")
if comecar == "S":
    print("1 - Qual o ano que foi criado a internet?")
    print("(A) - 1980")
    print("(B) - 1969")
    print("(C) - 1968")
    print("(D) - 1979")
    resposta1 = input("Informe sua resposta: ")
    if resposta1 == "B":
        print("Resposta correta!")
        pontuacao_final = pontuacao_final + 1
    else: 
        print("Resposta incorreta!") 
    
    print("2 - Quem criou a internet?")
    print("(A) - Robert Richards")
    print("(B) - Neymar")
    print("(C) - Willian Bonner")
    print("(D) - Tim Berners-Lee")
    resposta1 = input("Informe sua resposta: ")
    if resposta1 == "D":
        print("Resposta correta!")
        pontuacao_final = pontuacao_final + 1
    else: 
        print("Resposta incorreta!")

    print("2 - Quem criou o python?")
    print("(A) - Guido van Rossum")
    print("(B) - Katy Perry")
    print("(C) - Marie Curie")
    print("(D) - Stephen Hawking")
    resposta1 = input("Informe sua resposta: ")
    if resposta1 == "A":
        print("Resposta correta!")
        pontuacao_final = pontuacao_final + 1
    else: 
        print("Resposta incorreta!")
    if pontuacao_final == 0:
        sugestao = "estude muito mais"
    elif  pontuacao_final == 1:
        sugestao = "tem que melhorar"
    elif  pontuacao_final == 2:
        sugestao = "na média"
    elif pontuacao_final == 3:
        sugestao = "você é um gênio"

    print(f"{nome}, você acertou {pontuacao_final} de 3 {sugestao}")

else:
    quit()