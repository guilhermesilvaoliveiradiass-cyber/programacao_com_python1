import re
codigo = input('digite um codigo: ')
if re.fullmatch(r"\d{4}",codigo):
    print("Código válido")
else:
    print('Código inválido')