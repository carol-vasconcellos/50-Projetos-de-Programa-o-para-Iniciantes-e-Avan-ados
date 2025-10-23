import random

def lancar_dados():
    print("Lançando dados!!!")
    return random.randint(1, 6)
    
lance = lancar_dados()

print(f"O resultado é: {lance}")