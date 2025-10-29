while True:
    fator_km_para_milhas = 0.621371 

    tipo = input("Converter de [M]ilhas para Quilômetros ou [K]m para Milhas ou deseja [S]air? ").upper()

    if tipo == 'M':
        milhas = float(input("Digite a distância em milhas: "))
        quilometros = milhas * 1.60934
        print(f"{milhas} milhas = {quilometros:.2f} quilômetros.")
        
    elif tipo == 'K':
        quilometros = float(input("Digite a distância em quilômetros: "))
        milhas = quilometros * 0.621371
        print(f"{quilometros} quilômetros = {milhas:.2f} milhas.")

    elif tipo == 'S':
        print("Saindo do conversor ....")
        break

    else:
        print("Opção inválida.")
