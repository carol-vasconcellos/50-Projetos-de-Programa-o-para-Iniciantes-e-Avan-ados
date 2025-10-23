import random
import time 

def jokenpo():
    print("Tente ser um vencedor. Escolha pedra, papel ou tesoura")
    
    # 1. Definição da lista FORA do loop para eficiência
    escolha = ['pedra', 'papel', 'tesoura']
    
    while True:
        # Pede a escolha do jogador
        escolha_player_1 = input("Qual é sua escolha (pedra, papel ou tesoura)? ").lower()
        
        # 2. Validação da escolha antes do efeito sonoro
        if escolha_player_1 not in escolha:
            print("Opção inválida! Escolha entre pedra, papel ou tesoura.")
            continue  # Volta para o início do loop
        
        # Efeito JO... KEN... PÔ!
        print("JO...")
        time.sleep(0.5)
        print("KEN...")
        time.sleep(0.5)
        print("PÔ!!!")
        time.sleep(0.3)

        maquina = random.choice(escolha)
        
        print("-" * 40)
        print(f"Sua escolha: {escolha_player_1.upper()} | Máquina: {maquina.upper()}")
        print("-" * 40)
        
        # Lógica de Vitória/Empate
        if escolha_player_1 == maquina:
            print("Resultado: Deu **EMPATE**!")

        elif (escolha_player_1 == 'pedra' and maquina == "tesoura") or \
             (escolha_player_1 == 'papel' and maquina == "pedra") or \
             (escolha_player_1 == 'tesoura' and maquina == "papel"):
            print("Resultado: Você **GANHOU**!!!")

        else:
            # Se não empatou, nem ganhou, então PERDEU
            print("Resultado: A máquina **GANHOU**!")

        # Loop para perguntar se quer continuar
        while True:
            continuar = input("\nDeseja jogar outra rodada? (s/n): ").lower()
            if continuar == 's':
                break  # Sai do loop de continuidade e volta para o while True principal
            elif continuar == 'n':
                print("Jogo encerrado! Obrigado por jogar.")
                return # Encerra a função e o programa
            else:
                print("Opção inválida! Digite 's' para sim ou 'n' para não.")

# Inicia o jogo
jokenpo()