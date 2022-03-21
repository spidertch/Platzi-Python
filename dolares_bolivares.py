dolares = input("Inserte dolares: ")
dolares = float(dolares)
valor_dolar = input("Inserte precio del dolar: ")
valor_dolar = float(valor_dolar)
bolivares = dolares * valor_dolar
bolivares = round(bolivares, 2)
bolivares = str(bolivares)
print("Tienes $" + bolivares + "bolivares")