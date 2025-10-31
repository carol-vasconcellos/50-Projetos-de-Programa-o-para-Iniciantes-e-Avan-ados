def cifra_de_cesar(texto_original, chave):

    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    texto_criptografado = ""

    for letra in texto_original.upper():
        
        if letra in alfabeto:

            posicao_atual = alfabeto.find(letra)
            
            nova_posicao = (posicao_atual + chave) % 26
            
            texto_criptografado += alfabeto[nova_posicao]
        
        else:
 
            texto_criptografado += letra
            
    return texto_criptografado

try:
    texto = input("Digite o texto para criptografar: ")
    
    chave = int(input("Digite a chave (número de deslocamento, ex: 3): "))

    resultado = cifra_de_cesar(texto, chave)
    
    print("-" * 30)
    print(f"Texto original: {texto}")
    print(f"Texto cifrado: {resultado}")

except ValueError:
    print("Erro: A chave deve ser um número inteiro.")