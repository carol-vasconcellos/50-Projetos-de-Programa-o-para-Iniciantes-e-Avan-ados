def texto_para_morse(texto_usuario):

    texto_para_morse = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-',
    ' ': '/'
}
    
    texto_traduzido = []

    for i in texto_usuario.upper(): # Converte tudo para maiúsculo
        if i in texto_para_morse:
            texto_traduzido.append(texto_para_morse[i])

    return ' '.join(texto_traduzido)
        
texto_entrada = input('insira um texto para ser traduzido para o código morse: ')

morse = texto_para_morse(texto_entrada)

print(f"Seu texto: '{texto_entrada}' em código morse é: '{morse}'")