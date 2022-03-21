bolivares = input("Inserte bolivares: ")
bolivares = float(bolivares)
valor_dolar = input("Inserte precio del dolar: ")
valor_dolar = float(valor_dolar)
dolares = bolivares / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
print("Tienes $" + dolares + "dolares")
