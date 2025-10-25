import random

while True:

    Saudacao = ('OI', 'OLA', 'BOM DIA', 'BOA TARDE')
    Despedida = ('TCHAU', 'ADEUS', 'ATE MAIS', 'SAIR')
    Humor = ('TUDO BEM?', 'COMO ESTA?', 'BELEZA?')
    Nao_Entendeu = (
        "Desculpe, não entendi. Você pode reformular sua pergunta?",
        "Isso é um pouco complexo para mim. Tente algo mais simples.",
        "Hmm, vamos falar sobre outro assunto?"
    )

    resposta = input("Fale algo? Ou deseja sair? ").upper().strip()

    if resposta in Despedida:
        print("👋 Até logo! Foi um prazer conversar com você.")
        break

    elif resposta in Saudacao:
        print("🤖 Oi! Que bom falar com você!")

    elif resposta in Humor:
        print("😀 Estou ótimo, e você?")

    else:
        print(random.choice(Nao_Entendeu))