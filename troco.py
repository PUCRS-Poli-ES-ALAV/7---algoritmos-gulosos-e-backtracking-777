import math

def calcula_troco(lista_moedas, valor):
    tupla_moedas = []

    for moeda in lista_moedas:
        if(valor == 0):
            break

        num_moedas = math.floor(valor / moeda)

        tupla_moedas.append([moeda, num_moedas])
        valor = valor % moeda

    return tupla_moedas




print(calcula_troco([100, 25, 10, 5, 1], 289))