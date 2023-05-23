def adição(decisão: int) -> int:
    if decisão == 1:       
        lista= []

    while True:
        try:
            resposta = int(input("Digite a quantidade de números que quer somar: "))
        except ValueError:
            print("Número inválido, digite novamente.")
            return adição(decisão)

        for _ in range(resposta):
            while True:
                try:
                    número = int(input("Digite um número: "))
                    lista.append(número)
                    break
                except ValueError:
                    print("Número inválido, digite novamente.")

        somar = sum(lista)

        for posição, elemento in enumerate(lista):
            if posição == len(lista) - 1:
                print(elemento, end="")
            else:
                print(elemento, end=" + ")
                
        print(f" = {somar}")
        return somar
