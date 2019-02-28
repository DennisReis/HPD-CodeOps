#!/usr/bin/env python3
oJogo = {'cima-E': ' ', 'cima-M': ' ', 'cima-D': ' ',
         'meio-E': ' ', 'meio-M': ' ', 'meio-D': ' ',
         'baixo-E': ' ', 'baixo-M': ' ', 'baixo-D': ' '}

def printBoard(board):
    print(board['cima-E'] + '|' + board['cima-M'] + '|' + board['cima-D'])
    print('-+-+-')
    print(board['meio-E'] + '|' + board['meio-M'] + '|' + board['meio-D'])
    print('-+-+-')
    print(board['baixo-E'] + '|' + board['baixo-M'] + '|' + board['baixo-D'])

vez = 'X'

for i in range(9):
    printBoard(oJogo)
    print('Eh a vez do ' + vez + '. Qual eh a posicao desejada?')
    move = input()
    oJogo[move] = vez
    if vez == 'X':
        vez = 'O'
    else:
        vez = 'X'

printBoard(oJogo)
