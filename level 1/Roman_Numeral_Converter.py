def converter_numero_para_romano(numero):
    
    mapa_romano = {
        1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
        100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
        10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
    }

    valor_traduzido = ""

    for valor, simbolo in mapa_romano.items():
        
        while numero >= valor:
            valor_traduzido += simbolo
            numero -= valor

    return valor_traduzido

try:
    numero_entrada = int(input("Digite um numero para traduzir romano: "))

    numero_traduzido = converter_numero_para_romano(numero_entrada)

    print(f"Numero inserido é: {numero_entrada}, traduzido para romano é: {numero_traduzido}")

except ValueError:
    print("Entrada inválida. Digite apenas números inteiros.")