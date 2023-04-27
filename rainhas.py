def calcula_posicoes_atq(pos_rainha):
    posicoes_atq = [
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0]]

    posicoes_atq[3] = [1, 1, 1, 1, 1, 1, 1]

    for linha in posicoes_atq:
        linha[3] = 1

    n = 0
    for linha in posicoes_atq:

        if(n+pos_rainha[0]-3 < 7):
            linha[n+pos_rainha[0]-3] = 1
            
        # diagonal /
        #if(6-n-pos_rainha[1] > 0):
            #linha[6-n-pos_rainha[1]] = 1

        n = n + 1

    posicoes_atq[pos_rainha[0]][pos_rainha[1]] = 2
    printa_tabuleiro(posicoes_atq)

def printa_tabuleiro(tabuleiro):
    print()
    for linha in tabuleiro:
        print(linha)

#printa_tabuleiro(calcula_posicoes_atq())

calcula_posicoes_atq([3,3])