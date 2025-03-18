# -*- coding: utf-8 -*-
"""8_Exercicio.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ms9MNcJVCKOm5g7ZJB1SIHV0FyFBPpX1

Write a program to evenly divide pizzas.

Prompt for the number of people, the number of pizzas, and the number of slices per pizza.

Ensure that the number of pieces comes out even.

Display the number of pieces of pizza each person
should get.

If there are leftovers, show the number of leftover pieces.
"""

pessoas = input("Digite o número de pessoas: ")
pizzas = input("Digite o número de pizzas: ")
fatias_pizza = input("Digite o número de pedaços por pizza: ")

pessoas = int(pessoas)
pizzas = int(pizzas)
fatias_pizza = int(fatias_pizza)

fatias_total = pizzas * fatias_pizza
fatias_pessoa = fatias_total // pessoas
fatias_sobra = fatias_total % pessoas

if fatias_total % pessoas != 0:

  print(f'{pessoas} pessoas com {pizzas} pizzas.')
  print(f'Cada pessoa vai ter {fatias_pessoa} fatias de pizza.')
  print(f'Vão sobrar {fatias_sobra} fatias de pizza.')

else:

  print(f'{pessoas} pessoas com {pizzas} pizzas.')
  print(f'Cada pessoa vai ter {fatias_pessoa} fatias de pizza.')