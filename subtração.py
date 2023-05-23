def reduzir(decisão: int) -> int:    
    if decisão == 2:
        lista= []

    while True:
        try:
            resposta = int(input("Digite a quantidade de números que quer substrair: "))
        except ValueError:
            print("Número inválido. Digite novamente.")
            return reduzir(decisão)

        for _ in range(resposta):
            while True:
                try:    
                    número = int(input("Digite um número: "))
                    lista.append(número)
                    break
                except ValueError:
                    print("Número inválido. Digite novamente.")

        subtração = subtrair(lista)

        for posição, elemento in enumerate(lista):
            if posição == len(lista) - 1:
                print(elemento, end="")
            else:
                print(elemento, end=" - ")
        print(f" = {subtração}")
        return reduzir

def subtrair(números):
    resultado = números [0]
    for sequência in números[1:]:
        resultado -= sequência
    return resultado
