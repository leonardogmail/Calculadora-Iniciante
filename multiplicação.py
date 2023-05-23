def produto(decisão: int) -> int:
    if decisão == 3:
        lista = []

    while True:
        try:
            resposta = int(input("Digite a quantidade de números que quer multiplicar: "))
        except ValueError:
            print("Número inválido, digite novamente.")
            return produto(decisão)

        for _ in range(resposta):
            while True:
                try:    
                    número = int(input("Digite um número: ")) 
                    lista.append(número)
                    break
                except ValueError:
                    print("Número inválido, digite novamente.")

        multiplicação = multiplicar(lista)

        for posição, elemento in enumerate(lista):
            if posição == len(lista) - 1:
                print(elemento, end="")
            else:
                print(elemento, end=" x ")       
        print(f" = {multiplicação}")
        return produto

def multiplicar(número):
    resultado = número[0]
    for sequência in número[1:]:
        resultado *= sequência
    return resultado
