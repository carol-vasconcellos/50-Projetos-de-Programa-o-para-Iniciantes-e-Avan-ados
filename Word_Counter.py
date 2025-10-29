def contar_palavras():
    print("\n--- BEM-VINDO AO CONTADOR DE PALAVRAS ---")

    while True:
        texto = input('Escreva um texto ou escreva [sair] para parar. ')

        if texto.lower() == 'sair':
            print("Contador encerrado. Até mais!")
            break

        texto_limpo = texto.strip()

        if not texto_limpo:
            print("O texto está vazio. Total de palavras: 0")
            continue

        lista_palavras = texto.split()

        total_palavras = len(lista_palavras)
        
        total_caracteres = len(texto_limpo)

        print("-" * 35)
        print(f"Total de Palavras Contadas: {total_palavras}")
        print(f"Total de Caracteres (incluindo espaços): {total_caracteres}")
        print("-" * 35)

contar_palavras()