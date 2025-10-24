import random

frases = ["Uma grande aventura o aguarda", "Confie em sua intuição", "Seus números da sorte são: 14, 28, 33, 40", "Você será abençoado essa semana!"]

def fortune_cookie():
    print("Tire seu biscoito da sorte!")
    return random.choice(frases)

frase = fortune_cookie()

print(frase)

# random.choice(frases) → escolhe uma frase aleatória da lista.

# random.randint() -> gera números inteiros aleatórios, e por isso não funcionava com uma lista.