import random

valores_cartas = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

def distribuir_carta(mao):
    carta = random.choice(valores_cartas)
    mao.append(carta)
    return carta

def soma_mao(mao):
    total = sum(mao)
    # Ajustar Ás (11) para 1 se passar de 21
    for _ in range(mao.count(11)):
        if total > 21:
            total -= 10
    return total

def turno_jogador(nome, mao):
    while True:
        print(f"{nome}, suas cartas: {mao} = {soma_mao(mao)}")
        if soma_mao(mao) > 21:
            print(f"{nome} estourou!")
            return False  # Jogador perdeu
        decisao = input(f"{nome}, quer comprar mais uma carta? [S/N]: ").upper()
        if decisao == 'S':
            carta = distribuir_carta(mao)
            print(f"{nome} recebeu {carta}")
        else:
            break
    return True  # Jogador parou sem estourar

def jogar():
    nome1 = input("Insira seu nome jogador 1: ")
    nome2 = input("Insira seu nome jogador 2: ")
    print("-" * 30)
    print(f"Bem-vindos, {nome1} e {nome2}, ao BlackJack!")
    print("-" * 30)

    while True:
        mao_jogador1 = []
        mao_jogador2 = []

        # Distribuição inicial: duas cartas para cada jogador
        distribuir_carta(mao_jogador1)
        distribuir_carta(mao_jogador1)
        distribuir_carta(mao_jogador2)
        distribuir_carta(mao_jogador2)

        # Turno do jogador 1
        print(f"\nTurno de {nome1}:")
        jogou1 = turno_jogador(nome1, mao_jogador1)

        # Turno do jogador 2
        print(f"\nTurno de {nome2}:")
        jogou2 = turno_jogador(nome2, mao_jogador2)

        total1 = soma_mao(mao_jogador1)
        total2 = soma_mao(mao_jogador2)

        print("\nResultados finais:")
        print(f"{nome1}: {mao_jogador1} = {total1}")
        print(f"{nome2}: {mao_jogador2} = {total2}")

        if total1 > 21 and total2 > 21:
            print("Ambos estouraram. Empate!")
        elif total1 > 21:
            print(f"{nome2} ganhou!")
        elif total2 > 21:
            print(f"{nome1} ganhou!")
        elif total1 > total2:
            print(f"{nome1} ganhou!")
        elif total2 > total1:
            print(f"{nome2} ganhou!")
        else:
            print("Empate!")

        while True:
            decisao = input('\nQuer [S]air ou [J]ogar novamente? ').upper()
            if decisao == 'S':
                print("Saindo do jogo...")
                return  # Sai da função jogar() completamente
            elif decisao == 'J':
                print("\nVamos jogar uma nova rodada!\n")
                break  # Sai do loop da decisão e reinicia a rodada
            else:
                print("Opção inválida! Digite S ou J.")

jogar()
