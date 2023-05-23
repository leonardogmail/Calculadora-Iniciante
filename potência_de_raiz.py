def exponenciação(decisão: str) -> str:
    if decisão == 5:
        while True:
            try:
                número_1 = int(input("Digite um número: "))
                break
            except ValueError:
                print("Número inválido.")

        while True:
            try:        
                número_2 = int(input("Digite um número: "))
                if número_2 < 0:
                    raise ValueError("Não é possível calcular com expoente negativo.")
                break
            except ValueError as e:
                print(e)

        resultado_potência = número_1 ** número_2
        print(f"A potência de {número_1} elevado a {número_2}. É {resultado_potência}.")
        return resultado_potência

def raiz_númerica(decisão: str) -> str:
    if decisão == 6:
        while True:
            try:
                número_1 = int(input("Digite o número que deseja calcular: "))
                if número_1 < 0:
                    raise ValueError("Não é possível calcular número negativo em raiz nas condições normais.")
                break
            except ValueError as e:
                print(e)

        while True:
            try:
                número_2 = int(input("Digite o índice da raiz: "))
                if número_2 == 0:
                    raise ValueError("Não é possível resolver raiz com zero.")
                break
            except ValueError as e:
                print(e)

        resultado_raiz = pow(número_1, 1/número_2)
        print(f"A raiz {número_2} de {número_1} é {resultado_raiz:.2f}.")
        return resultado_raiz
