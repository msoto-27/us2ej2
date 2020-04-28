from random import randrange

def stringAleatorio(tamaño, char_min = 33, char_max = 126):
    string = ''
    for i in range(tamaño):
        string += chr(randrange(char_min, char_max))
    return string

def crearViajeros(cantidad):
    archivo = open('lista.csv', 'a')
    for i in range(cantidad):
        linea = str(i+1)+','
        if randrange(0,5):
            linea += str(randrange(20000000, 45000000))
        else:
            linea += stringAleatorio(7)
        linea += ','
        for i in range(2):
            if(randrange(0,5)):
                linea += stringAleatorio(randrange(3,7), 97, 122)
            else:
                linea += stringAleatorio(randrange(3,7))
            linea += ','
        if randrange(0, 5):
            linea += str(randrange(0, 10000))
        else:
            linea += stringAleatorio(randrange(3,7))
        archivo.write(linea + '\n')
    archivo.close()

if __name__ == '__main__':
    crearViajeros(20)
