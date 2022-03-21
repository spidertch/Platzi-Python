from __future__ import barry_as_FLUFL


def run():
    # for contador in range(1000):
    #     if contador % 2 != 0:
    #         continue
    #     print(contador)


    # for i in range(0, 10000):
    #     print(i)
    #     if i == 5876:
    #         break


    texto = input("Escribe un texto: ")
    for letra in texto:
        if letra == "o":
            break
        print(letra)



if __name__ == '__main__':
    run()