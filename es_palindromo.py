palabra = input('Ingrese una palabra: ').lower().replace(" ","")

palabra_invertida = palabra[::-1]

if palabra == palabra_invertida:
    print(f'La palabra {palabra} es un palíndromo.')
else:
    print(f'La palabra {palabra} no es un palíndromo.')