perguntas = [
    {
        "pergunta": "Qual é a capital do Japão?",
        "opcoes": ["A) Pequim", "B) Seul", "C) Tóquio", "D) Bangkok"],
        "resposta": "C"
    },
    {
        "pergunta": "Quem é o pintor famoso pela obra 'Mona Lisa'?",
        "opcoes": ["A) Vincent van Gogh", "B) Pablo Picasso", "C) Claude Monet", "D) Leonardo da Vinci"],
        "resposta": "D"
    },
    {
        "pergunta": "Qual é a fórmula química da água?",
        "opcoes": ["A) O2", "B) CO2", "C) H2O", "D) NaCl"],
        "resposta": "C"
    },
    {
        "pergunta": "Qual é o maior órgão do corpo humano em área e peso?",
        "opcoes": ["A) Coração", "B) Cérebro", "C) Fígado", "D) Pele"],
        "resposta": "D"
    },
    {
        "pergunta": "Qual empresa desenvolveu o sistema operacional Android?",
        "opcoes": ["A) Apple", "B) Microsoft", "C) Samsung", "D) Google"],
        "resposta": "D"
    }
]


def fazer_perguntas(perguntas):
    pontuacao = 0

    nome = input("Qual é o seu nome? ")
    print("-" * 30)
    print(f"Bem-vindo(a), {nome}, ao quiz!")
    print("-" * 30)

    for i, item in enumerate(perguntas):
        valor_pontuacao = 10  # cada pergunta vale 10 pontos (você pode mudar isso)

        while True:  # repete até acertar ou desistir
            print(f"\n--- PERGUNTA {i+1} | VALENDO {valor_pontuacao} pontos ---")
            print(item["pergunta"])
            for opcao in item["opcoes"]:
                print(opcao)

            resposta = input("Sua resposta (ou 'S' para parar): ").upper().strip()

            if resposta == 'S':
                print(f"\nVolte sempre, {nome}! Encerrando o quiz...")
                print(f"Sua pontuação final: {pontuacao}")
                return  # encerra a função completamente

            if resposta == item["resposta"]:
                pontuacao += valor_pontuacao
                print(f"\n✅ ACERTOU! Sua pontuação atual: {pontuacao}")
                break  # vai para a próxima pergunta
            else:
                print("\n❌ ERROU! Tente novamente.")

    print(f"\n🎉 PARABÉNS, {nome}! Você concluiu o quiz com {pontuacao} pontos! 🎉")


# Executa o quiz
fazer_perguntas(perguntas)
