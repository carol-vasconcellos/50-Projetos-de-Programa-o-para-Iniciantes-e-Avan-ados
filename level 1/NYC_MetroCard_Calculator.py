import time 

def calculadora_metrocard():
    try:
        num_viagens = int(input('Quantas viagens você quer?: '))

        if num_viagens <= 0:
            print("Por favor, digite um número positivo.")
            return

        calculo_total = num_viagens * 2.90
        valor_a_pagar = calculo_total / 1.11

        print(f"Você deve adicionar $ {valor_a_pagar:.2f} para ter exatamente {num_viagens} viagens.")

    except ValueError:
        print("Entrada inválida. Digite apenas números inteiros.")

def viajar():
    
    while True:
        
        calculadora_metrocard()

        print("-" * 30)
        voltar = input('Deseja [C]ontinuar (fazer outro cálculo) ou [S]air? ').upper()
        
        if voltar == 'S':
            print('Volte sempre!!!')
            break
            
        elif voltar == 'C':
            
            print("\nReiniciando...")
            time.sleep(1)
        
        else:
            print('Opção inválida! Encerrando por segurança.')
            break

viajar()