# -*- coding: utf-8 -*-
"""9_Exercicio.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1OqsAuzd4UEb_aAZ6H8rip4vjzfrYDNz3

Calculate gallons of paint needed to paint the ceiling of a
room.

Prompt for the length and width, and assume one
gallon covers 350 square feet.

Display the number of gallons
needed to paint the ceiling as a whole number.
"""

import math

comprimento = input("Digite o comprimento: ")
largura = input("Digite a largura: ")

comprimento = float(comprimento)
largura = float(largura)

galao = 350
area = comprimento * largura
galoes_teto = area / galao

galoes_teto = math.ceil(galoes_teto)

if galoes_teto == 1:
  print(f'Será necessário 1 galão de tinta')

else:
  print(f'Serão necessários {galoes_teto} galões de tinta.')