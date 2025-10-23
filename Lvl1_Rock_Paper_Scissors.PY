import time

while True:
    jogador = input("Escolha rock, paper ou scissors (ou 'sair'): ").lower()

    if jogador == "sair":
        print("Jogo encerrado!")
        break

    if jogador not in ["rock", "paper", "scissors"]:
        print("Opção inválida! Tente novamente.")
        continue

    print("JO...")
    time.sleep(0.5)
    print("KEN...")
    time.sleep(0.5)
    print("PO...")
    time.sleep(0.3)

    # Computador fixo (pode mudar para variar)
    computador = "rock"
    print(f"Computador escolheu: {computador}")

    if jogador == computador:
        print("Empate!")
    elif jogador == "rock" and computador == "scissors":
        print("Você venceu!")
    elif jogador == "paper" and computador == "rock":
        print("Você venceu!")
    elif jogador == "scissors" and computador == "paper":
        print("Você venceu!")
    else:
        print("Computador venceu!")
