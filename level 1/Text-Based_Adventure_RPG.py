while True:

    insira_nome = input("Insira seu nome ou nick: ").strip() #Remove espaços

    print("-" * 40)
    print(f"Bem-vindo jogador {insira_nome} a terra de LOSS!!!")
    print("-" * 40)

    pergunta = input("Você está na entrada de uma floresta densa. O ar é frio e você ouve um leve sussurro. Há um caminho que segue para o NORTE e um aviso. Qual lado voce seguirá?(NORTE,LESTE)").upper()
    
    if pergunta == "SAIR":
        print("\nVocê decidiu não entrar na floresta. Fim de jogo.")
        break

    elif pergunta == "LESTE":
        print("\nVocê ignora o aviso. O caminho está coberto por uma névoa espessa...")
        print("Você tropeça e cai em uma cova. 💀 FIM DE JOGO.")
        break

    elif pergunta == "NORTE":
        print("\nVocê segue por um caminho poeirento. Há pegadas estranhas no chão.")
        resposta = input("Ao NORTE há um velho templo em ruínas. Você segue ao NORTE ou volta ao SUL? ").upper()

        if resposta == "SUL":
            print("\nVocê voltou para a entrada da floresta. O mistério permanece...")
            break

        elif resposta == "NORTE":
            print("\nVocê chega ao templo antigo, coberto por vegetação.")
            acao = input("No centro, há uma ESTÁTUA. Você quer examinar (E) ou voltar (S)? ").upper()

            if acao == "S":
                print("\nVocê decide não mexer com o desconhecido e retorna ao caminho.")
                break
            
            elif acao == "E":
                print("\nA estátua tem um compartimento secreto. Você pega uma CHAVE ENFERRUJADA.")
                acao2 = input("Você ouve um barulho ao OESTE. Quer ir até lá (O) ou voltar (S)? ").upper()

                if acao2 == "S":
                    print("\nVocê volta, mas sente que perdeu algo importante...")
                    break

                elif acao2 == "O":
                    print("\nVocê encontra uma cabana escura. A porta está trancada.")
                    usar = input("Quer usar a CHAVE (S/N)? ").upper()

                    if usar == "S":
                        print("\n🔑 A chave gira lentamente... A porta se abre!")
                        print("Um portal brilhante aparece. ✨ Você ESCAPOU da floresta! VITÓRIA! 🏆")
                        break
                    else:
                        print("\nVocê hesita e decide não abrir a porta. O som na floresta aumenta... 💀 Você perdeu!!!")
                        break

    else:
        print("\nComando inválido! Tente novamente.\n")