# -*- coding: utf-8 -*-
"""2_Exercicio.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16I57sBn8sQ0olGPO4m2i2Ubs-QpuhJfB

Create a program that prompts for an input string and displays an output that shows the input string and the number of
characters the string contains.
"""

string = input("Digite uma string: ")

tamanho_str = len(string)

print(f'{string} tem {tamanho_str} caracteres')