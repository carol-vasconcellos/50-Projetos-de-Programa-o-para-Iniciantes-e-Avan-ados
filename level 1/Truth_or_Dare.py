import random

lista_verdades = [
    "Qual foi a mentira mais 'cabeluda' que você já contou para evitar uma bronca?",
    "Quem, de todas as pessoas que você já conheceu, te deu a pior primeira impressão?",
    "Qual é o seu maior medo bobo (irracional)?",
    "Qual é a última coisa 'vergonhosa' que você pesquisou no seu celular?",
    "Você já colou em alguma prova na escola ou faculdade? Se sim, em qual?",
    "Qual foi o momento mais constrangedor que você já passou em público?"
]

lista_desafios = [
    "Faça a dancinha mais ridícula do TikTok que você conseguir lembrar.",
    "Ligue para um amigo e conte uma piada sem graça, sem rir.",
    "Cheire o seu próprio sapato ou tênis e descreva o cheiro com três adjetivos.",
    "Imite um cachorro latindo ou um gato miando por 30 segundos, sem parar.",
    "Coma uma colher de mostarda, ketchup, ou qualquer outro condimento que não combine com nada.",
    "Tire uma selfie fazendo a sua pior careta e use-a como foto de perfil por 5 minutos."
]

while True:

    try:
        n_jogadores = int(input("🎲 Bem-vindos! Quantos jogadores irão jogar? (2 - 4): "))

        if n_jogadores < 2 or n_jogadores > 4:
            print("❌ Número inválido! Escolha entre 2 e 4 jogadores.\n")
            continue
        else:
            break

    except ValueError:
        print("⚠️ Digite um número válido!\n")

jogadores = []
for i in range(n_jogadores):
    nome = input(f"Digite o nome do jogador {i+1}: ").capitalize()
    jogadores.append(nome)

print("\n✅ Jogadores confirmados:")
for j in jogadores:
    print(f" - {j}")

print("\nVamos começar o jogo!\n")

while True:
    jogador_atual = random.choice(jogadores)
    print(f"\n👉 É a vez de {jogador_atual}!")

    escolha = input("Você escolhe VERDADE ou DESAFIO? (V/D ou SAIR): ").upper()

    if escolha == "SAIR":
        print("\nJogo encerrado. Obrigado por jogar! 👋")
        break

    elif escolha == "V":
        print("\n💬 VERDADE:")
        print(random.choice(lista_verdades))

    elif escolha == "D":
        print("\n🔥 DESAFIO:")
        print(random.choice(lista_desafios))

    else:
        print("❌ Opção inválida! Escolha 'V' para Verdade ou 'D' para Desafio.")