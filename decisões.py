def obter_decisão():
    while True:
        try:
            decisão = int(input("Você deve digitar apenas números inteiros: "))
            if decisão < 1 or decisão > 6:
                raise ValueError("O número digitado não se encontra nas opções. Tente novamente.")
            break
        except ValueError as e:
            print(e)
    return decisão

def obter_continuação():
    continuar = ""

    while continuar not in ["sim", "não"]:
        try: 
            continuar = str(input("Se quiser continuar digite apenas sim ou não: ").lower())
        except ValueError:
            print("Você deve digitar apenas sim ou não.")
    return continuar

def obter_conclusão(continuar: str) -> str:
    continuar = obter_continuação()
    if continuar == "sim":        
        print("Continuando...")
        return obter_decisão
    elif continuar == "não":
        print("Até logo.")
        return False
