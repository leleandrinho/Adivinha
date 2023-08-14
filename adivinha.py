import random

print('JOGO DO ADIVINHA')

try:

    continuar = "S"
    pontos = 0

    while continuar == "S":
        numero = random.randint(1,100)
        print("TENTE ADIVINHAR O NÚMERO, VOCÊ TEM 5 CHANCES. BOA SORTE!")
        if pontos == 1:
            print(f"TOTAL PONTOS: {pontos} Ponto")
        else:
            print(f"TOTAL PONTOS: {pontos} Pontos")
        #print(numero) # SPOILER DO NÚMERO SECRETO)
        cont = 1
        reg = 4
        continuar = "S"

        while cont < 6 :
            res = int(input("QUAL É O NÚMERO?: "))
            if res == numero and cont == 1:
                print("PARABÉNS VOCÊ ACERTOU DE PRIMEIRA!") 
                pontos = pontos + 1
                break
            elif res == numero:
                print("PARABÉNS VOCÊ ACERTOU!")
                pontos = pontos + 1
                break
            elif res < numero:
                print(f"O NÚMERO É MAIOR, TENTE NOVAMENTE! VOCÊ TEM {reg} TENTATIVAS")
            elif res > 100 or res < 0:
                print("ESCOLHA UM NÚMERO VÁLIDO!")
                break
            else:
                print(f"O NÚMERO É MENOR, TENTE NOVAMENTE! VOCÊ TEM {reg} TENTATIVAS")
            cont = cont + 1
            reg = reg - 1

        if reg < 0:
            print("VOCÊ PERDEU TODAS SUAS CHANCES!")
            print(f"O NÚMERO ERA {numero}")

        
        continuar = input("Deseja Continuar?: [S/N] ").upper()
    else:
        if pontos == 1:
            print(f"VOCÊ OBTEVE {pontos} PONTO. PARABÉNS!")
        elif pontos == 0:
            print(f"VOCÊ OBTEVE {pontos} PONTOS. BOA SORTE DA PRÓXIMA VEZ!")
        else:
            print(f"VOCE OBTEVE {pontos} PONTOS. PARABÉNS!")
        exit()

except ValueError:
    print("VOCÊ ENTROU COM LETRA NO LUGAR DE NÚMERO. TENTE NOVAMENTE!")