def media(n, v):
    return sum(v) / n

def variancia(n, v, m):
    return sum((x - m) ** 2 for x in v) / n


def main():
    numeros = []
    print("Digite 10 números:")
    for i in range(10):
        num = float(input(f"Número {i + 1}: "))
        numeros.append(num)

    
    m = media(len(numeros), numeros)
    print(f"Média: {m:.2f}")

    
    var = variancia(len(numeros), numeros, m)
    print(f"Variância: {var:.2f}")
