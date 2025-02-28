import random 

a = "S"

while a=="S":
    tupla=(random.randint(1,6),random.randint(1,6))
    print (f"Os valores sorteados foram {tupla}")
    while True:
        a=input('Gostaria de girar novamente : ?').strip().upper()
        if a in ("S,N"):
            break
        print("Opção inválida, tente novamente")    
