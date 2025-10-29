import random

def advinhe_o_numero():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    palpite = 0

    print("\n--- INICIANDO NOVO JOGO ---")
    print("Tente adivinhar o número entre 1 e 100!")

    while palpite != numero_secreto:
        try:
            palpite = int(input("Seu palpite: "))
            tentativas += 1

            if palpite < numero_secreto:
                print("Dica: É MAIOR! Tente novamente.")
            elif palpite > numero_secreto:
                print("Dica: É MENOR! Tente novamente.")

        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")
            
    print(f"\n🎉 PARABÉNS! Você acertou o número {numero_secreto}!")
    print(f"Você precisou de {tentativas} tentativas.")


def rodar_jogo():
    """Função principal que gerencia o loop de repetição."""
    while True:
       
        advinhe_o_numero() 
        
        decisao = input('\nDeseja [S]air ou [N]ão (jogar de novo)? ').upper()

        if decisao == 'S':
            print('Até mais!!!')
            break
        elif decisao == 'N':
            print("-" * 30)
            continue
        else:
            print("Opção inválida. Jogo será encerrado.")
            break

rodar_jogo()