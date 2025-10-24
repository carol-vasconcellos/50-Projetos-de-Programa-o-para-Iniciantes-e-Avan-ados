def millionaire():
    perguntas = [
        {"p": "Qual é o nome do animal conhecido como 'Rei da Selva'?", "o": ["A) Tigre", "B) Leão", "C) Elefante", "D) Urso"], "r": "B"},
        {"p": "Qual planeta é famoso por seus anéis visíveis?", "o": ["A) Marte", "B) Vênus", "C) Saturno", "D) Júpiter"], "r": "C"},
        {"p": "Quem foi o primeiro presidente da República do Brasil?", "o": ["A) Getúlio Vargas", "B) Dom Pedro II", "C) Marechal Deodoro da Fonseca", "D) Juscelino Kubitschek"], "r": "C"},
        {"p": "Qual o processo químico que as plantas usam para converter luz em energia?", "o": ["A) Respiração", "B) Fotossíntese", "C) Osmose", "D) Evaporação"], "r": "B"},
        {"p": "Qual é o único número primo que é par?", "o": ["A) 1", "B) 4", "C) 2", "D) 0"], "r": "C"},
        {"p": "Qual país tem mais pirâmides?", "o": ["A) Egito", "B) Sudão", "C) México", "D) Peru"], "r": "B"},
        {"p": "Em qual ano o homem pisou na Lua pela primeira vez?", "o": ["A) 1965", "B) 1969", "C) 1972", "D) 1959"], "r": "B"},
        {"p": "Qual é a capital do Japão?", "o": ["A) Kyoto", "B) Osaka", "C) Tóquio", "D) Hiroshima"], "r": "C"}
    ]

    premios = [1000, 5000, 10000, 50000, 100000, 250000, 500000, 1000000]
    patamares_seguros = [10000, 100000] # Patamares garantidos
    
    ultimo_seguro = 0
    premio_acumulado = 0 # Variável para rastrear o valor da última pergunta ACERTADA

    for i, item in enumerate(perguntas):
        valor_pergunta = premios[i]
        
        print(f"\n--- PERGUNTA {i+1} | VALENDO R$ {valor_pergunta:,.2f} | ACUMULADO R$ {premio_acumulado:,.2f} ---")
        print(item["p"])
        for opcao in item["o"]:
            print(opcao)

        resposta = input("Sua resposta (ou 'P' para parar): ").upper()
        
        # Lógica de Parada
        if resposta == 'P':
            print(f"\nVocê parou! Você levou R$ {premio_acumulado:,.2f} para casa. Parabéns!")
            return

        # Lógica de Acerto
        if resposta == item["r"]:
            premio_acumulado = valor_pergunta 
            print(f"\n**ACERTOU!** Você acumulou R$ {premio_acumulado:,.2f}.")
            
            # Atualiza o patamar seguro
            if premio_acumulado in patamares_seguros:
                ultimo_seguro = premio_acumulado
                print(f"**Este valor é um Patamar de Segurança!**")

        # Lógica de Erro
        else:
            print("\n**ERROU!** O jogo acabou.")
            print(f"Sua resposta estava errada. Você sai com o prêmio garantido de R$ {ultimo_seguro:,.2f}.")
            return

    # Se sair do loop sem errar ou parar, ele acertou a última pergunta (1 milhão)
    print(f"\nPARABÉNS!!! VOCÊ ACERTOU TODAS AS PERGUNTAS E GANHOU R$ {premio_acumulado:,.2f}!")
    
millionaire()