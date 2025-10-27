import random

valores_cartas = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

def comprar_carta():

    return random.choice(valores_cartas)

def turno_jogador(mao_jogador, mao_maquina):
    
    while sum(mao_jogador) < 21:
        print("\n--- SEU TURNO ---")
        print(f"Sua mão: {mao_jogador} (Total: {sum(mao_jogador)})")
        print(f"Máquina: [{mao_maquina[0]}, ?]") 

        acao = input("Deseja (P)edir mais uma carta ou (F)icar? ").upper()

        if acao == 'P':
            nova_carta = comprar_carta()
            mao_jogador.append(nova_carta)
            print(f"Você recebeu: {nova_carta}")
            
            # Verifica BUST imediato
            if sum(mao_jogador) > 21:
                print(f"\nBUST! Você estourou com {sum(mao_jogador)}.")
                return 'BUST_JOGADOR'

        elif acao == 'F':
            print(f"Você decidiu Ficar com {sum(mao_jogador)}.")
            break 
        else:
            print("Opção inválida, tente novamente.")
    
    return 'OK'

def turno_maquina(mao_maquina):
    """Lógica do turno da Máquina (Dealer)."""
    print("\n--- TURNO DA MÁQUINA ---")
    print(f"A Máquina revela sua mão: {mao_maquina} (Total: {sum(mao_maquina)})")
    
    # Regra Nível 1: Máquina pede até 17 ou mais
    while sum(mao_maquina) < 17:
        nova_carta = comprar_carta()
        mao_maquina.append(nova_carta)
        print(f"Máquina pede e recebe: {nova_carta}")
        
        if sum(mao_maquina) > 21:
            print(f"\nBUST! A Máquina estourou com {sum(mao_maquina)}.")
            return 'BUST_MAQUINA'

    print(f"Máquina finaliza com: {sum(mao_maquina)}.")
    return 'OK'

def vencedor(mao_jogador, mao_maquina, resultado_j, resultado_m):
    """Compara as pontuações e anuncia o vencedor."""
    
    total_jogador = sum(mao_jogador)
    total_maquina = sum(mao_maquina)

    if resultado_j == 'BUST_JOGADOR':
        print("Você estourou! Máquina vence 😢")
    elif resultado_m == 'BUST_MAQUINA':
        print("Máquina estourou! Você venceu 🎉")

    elif total_jogador > total_maquina:
        print(f"Você venceu com {total_jogador} vs {total_maquina} 🎉")
    elif total_jogador < total_maquina:
        print(f"Máquina venceu com {total_maquina} vs {total_jogador} 😢")
    else:
        print("Empate!")

# --- INÍCIO DO JOGO ---
def baby_blackjack_nivel_1():
    # 1. Iniciar mãos
    mao_jogador = [comprar_carta(), comprar_carta()]
    mao_maquina = [comprar_carta(), comprar_carta()]
    
    resultado_j = turno_jogador(mao_jogador, mao_maquina)
    
    resultado_m = 'OK'
    if resultado_j != 'BUST_JOGADOR':
        resultado_m = turno_maquina(mao_maquina)
        
    vencedor(mao_jogador, mao_maquina, resultado_j, resultado_m)

baby_blackjack_nivel_1()