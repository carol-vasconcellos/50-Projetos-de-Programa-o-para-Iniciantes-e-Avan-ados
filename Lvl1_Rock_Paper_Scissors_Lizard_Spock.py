import time

while True:
    jogador = input("Escolha rock, paper, scissors, lizard ou spock (ou 'sair'): ").lower()
    
    if jogador == "sair":
        print("Jogo encerrado!")
        break
    
    if jogador not in ["rock", "paper", "scissors", "lizard", "spock"]:
        print("Opção inválida! Tente novamente.")
        continue

    print("rock...")
    time.sleep(0.5)
    print("paper...")
    time.sleep(0.5)
    print("scissors...")
    time.sleep(0.5)
    print("lizard...")
    time.sleep(0.5)
    print("spock...")
    time.sleep(0.3)
    
    # Computador sempre escolhe "scissors"
    computador = "scissors"
    print(f"Computador escolheu: {computador}")
    
    if jogador == computador:
        print("Empate!")
    elif jogador == "rock" and (computador == "scissors" or computador == "lizard"):
        print("Você venceu!")
    elif jogador == "paper" and (computador == "rock" or computador == "spock"):
        print("Você venceu!")
    elif jogador == "scissors" and (computador == "paper" or computador == "lizard"):
        print("Você venceu!")
    elif jogador == "lizard" and (computador == "paper" or computador == "spock"):
        print("Você venceu!")
    elif jogador == "spock" and (computador == "rock" or computador == "scissors"):
        print("Você venceu!")
    else:
        print("Computador venceu!")
