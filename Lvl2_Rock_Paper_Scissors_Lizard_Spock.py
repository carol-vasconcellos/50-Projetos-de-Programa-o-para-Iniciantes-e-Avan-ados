import random
import time

def jokenpo():
    print("Tente ser um vencedor. Escolha pedra, papel, tesoura, lagarto ou spock.")

    regras = {
        'pedra': {'tesoura': 'Pedra esmaga Tesoura', 'lagarto': 'Pedra esmaga Lagarto'},
        'papel': {'pedra': 'Papel cobre Pedra', 'spock': 'Papel refuta Spock'},
        'tesoura': {'papel': 'Tesoura corta Papel', 'lagarto': 'Tesoura decapita Lagarto'},
        'lagarto': {'spock': 'Lagarto envenena Spock', 'papel': 'Lagarto come Papel'},
        'spock': {'tesoura': 'Spock quebra Tesoura', 'pedra': 'Spock vaporiza Pedra'}
    }

    escolhas = list(regras.keys())

    while True:
        player = input("Qual é sua escolha (player1): ").lower()
        if player not in escolhas:
            print("Opção inválida! Escolha entre pedra, papel, tesoura, lagarto ou spock.")
            continue

        print("ROCK...")
        time.sleep(0.5)
        print("PAPER...")
        time.sleep(0.5)
        print("SCISSORS...")
        time.sleep(0.5)
        print("LIZARD...")
        time.sleep(0.5)
        print("SPOCK!!!")
        time.sleep(0.3)

        maquina = random.choice(escolhas)

        print("-" * 40)
        print(f"\nSua escolha: {player} | Máquina: {maquina}")
        print("-" * 40)

        if player == maquina:
            print("Deu empate!")
        elif maquina in regras[player]:
            print(f"{regras[player][maquina]}. Você venceu!")
        else:
            print(f"{regras[maquina][player]}. A máquina venceu!")

        continuar = input("\nDeseja jogar outra rodada? (s/n): ").lower()
        if continuar == 'n':
            print("Jogo encerrado! Obrigado por jogar.")
            break

jokenpo()