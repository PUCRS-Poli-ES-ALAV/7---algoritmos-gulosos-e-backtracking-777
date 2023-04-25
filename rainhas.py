def calcula_posicoes_atq(pos_rainha):
    posicoes_atq = [[0]*7]*7

    posicoes_atq[3] = [1]*7
    for linha in posicoes_atq:
        linha[3] = 1

    n = 0

    #print(posicoes_atq)
    for linha in posicoes_atq:
        linha[n] = 1
        print(linha)
        n = n + 1
    
    #posicoes_atq[3][3] = 2

    return posicoes_atq

def printa_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(linha)

#printa_tabuleiro(calcula_posicoes_atq([4,4]))

calcula_posicoes_atq([4,4])