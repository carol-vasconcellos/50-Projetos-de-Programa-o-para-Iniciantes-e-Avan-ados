from math import pi

while True:
    print("\n1. Quadrado/Retângulo")
    print("2. Círculo")
    print("3. Triângulo")
    print("0. Sair")

    resposta = input('\nQual forma geométrica você quer calcular a área ou sair da aplicação? ')

    if resposta == '0':
        print('Até mais!!!')
        break

    elif resposta == '1':
        try:
            largura = float(input('Qual a largura?: '))
            altura = float(input('Qual a altura?: '))
            area = largura * altura
            print(f'A área do Quadrado/Retângulo é: {area}')
        except ValueError:
            print("\nERRO: Por favor, insira apenas valores numéricos para as dimensões.")

    elif resposta == '2':
        try:
            raio = float(input('Qual a raio?: '))
            area = pi * raio**2
            print(f'A área do Círculo é: {area:.2f}')
        except ValueError:
            print("\nERRO: Por favor, insira apenas valores numéricos para as dimensões.")

    elif resposta == '3':
        try: 
            base = float(input('Qual a base?: '))
            altura = float(input('Qual a altura?: '))
            area = (base * altura) / 2
            print(f'A área do Triângulo é: {area}')
        except ValueError:
            print("\nERRO: Por favor, insira apenas valores numéricos para as dimensões.")

    else: 
        print('\nOpção inválida!')