# -*- coding: utf-8 -*-
"""7_Exercicio.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1URW1uJk5IPJU5JKPhsswe6WA_DeCE6lD

Create a program that calculates the area of a room.

Prompt the user for the length and width of the room in feet.

Then display the area in both square feet and square meters.
"""

#The formula for this conversion is:

# m ** 2 = (f ** 2) * 0.09290304

comprimento = input("Digite o comprimento do quarto: ")
largura = input("Digite a largura do quarto: ")

comprimento = float(comprimento)
largura = float(largura)

area_pes = comprimento * largura
area_metros = area_pes * 0.09290304

area_metros_arredondada = round(area_metros, 3)

print(f'Você digitou dimensões de {comprimento} pés por {largura} pés.')
print(f'A área é:')
print(f'{area_pes} pés quadrados.')
print(f'{area_metros_arredondada} metros quadrados.')