# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 18:05:39 2021

@author: rshni
"""

import sudoku

def main():
    game = sudoku.Sudoku(['530070000',
                    '600195000',
                    '098000060',
                    '800060003',
                    '400803001',
                    '700020006',
                    '060000280',
                    '000419005',
                    '000080079'])
    print(game)
    
    print(game.solve())
    
    print(game)
    
main()