#!/usr/bin/env python3
oJogo = {'cima-E': ' ', 'cima-M': 'O', 'cima-D': 'X',
         'meio-E': ' ', 'meio-M': ' ', 'meio-D': 'X ',
         'baixo-E': ' ', 'baixo-M': 'O', 'baixo-D': 'X '}

def printBoard(board):
    print(board['cima-E'] + '|' + board['cima-M'] + '|' + board['cima-D'])
    print('-+-+-')
    print(board['meio-E'] + '|' + board['meio-M'] + '|' + board['meio-D'])
    print('-+-+-')
    print(board['baixo-E'] + '|' + board['baixo-M'] + '|' + board['baixo-D'])

printBoard(oJogo)
