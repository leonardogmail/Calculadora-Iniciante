def divisão(decisão: int) -> int:
    if decisão == 4:
        while True:
            try:
                operador_1 = int(input("Digite um número: "))
                break
            except ValueError:
                print("Número inválido.")
      
        while True:
            try:
                operador_2 = int(input("Digite um número: "))
                if operador_2 == 0:
                    raise ValueError("Não é possível dividir por zero.")
                break
            except ValueError as e:
                print(e)

        divisão = operador_1 / operador_2    
        print(f"A divisão entre {operador_1} / {operador_2} = {divisão:.2f}")
        return divisão
