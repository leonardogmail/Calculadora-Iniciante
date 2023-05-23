from somar import adição
from subtração import reduzir
from multiplicação import produto
from dividir import divisão
from potência_de_raiz import exponenciação, raiz_númerica
from texto import boas_vindas, informações
from decisões import obter_decisão, obter_continuação, obter_conclusão

boas_vindas()
informações()

continuação = ""

while continuação != False:
    
    decisão = obter_decisão()

    if decisão == 1:
        total = adição(1)
    elif decisão == 2:
        total = reduzir(2)
    elif decisão == 3:
        total = produto(3)
    elif decisão == 4:
        total = divisão(4)
    elif decisão == 5:
        total = exponenciação(5)
    elif decisão == 6:
        total = raiz_númerica(6)

    continuação = obter_conclusão(obter_continuação)
