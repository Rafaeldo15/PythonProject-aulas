#se não adicionar a funçao "float" ou "int" vai reconhecer o numero como um texto, não como numeral
#nesse caso usei float, e não int, pois ele permite numeros quebrados.
n1 = float(input("primeiro numero"))
n2 = float(input("segundo numero"))
resultado = (n1 + n2)
print ("o resultado da sua soma é:", resultado)