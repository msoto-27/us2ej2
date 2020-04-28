import csv

import re

from viajero import ViajeroFrecuente

  
def opcion0():
    pass

def opcion1():
    print('Usted cuenta con ', lista_viajeros[nv].cantidadTotaldeMillas(), 'millas')

def opcion2():
    millas = int(input("Ingrese la cantidad de mllas a sumar: "))
    lista_viajeros[nv].acumularMillas(millas)

def opcion3():
    millas = int(input('Ingrese la cantidad de millas a descontar: '))
    lista_viajeros[nv].canjearMillas(millas)

switcher = {
    0: opcion0,
    1: opcion1,
    2: opcion2,
    3: opcion3
}


def switch(argument):
    func = switcher.get(argument, lambda: print("Opción no válida"))
    func()

def cargarLista(lista):
    archivo = open('lista.csv')
    reader = csv.reader(archivo, delimiter = ',')
    i = 1
    for fila in reader:
        #print(str(fila))
        fila_completa = str(fila)
        if re.match(r"\['[0-9]{1,9}', '[0-9]{1,9}', '[A-Z, a-z]{1,10}', '[A-Z, a-z]{1,10}', '[0-9]{1,9}'\]", fila_completa):
            lista.append(ViajeroFrecuente(i, fila[1], fila[2], fila[3], int(fila[4])))
            print(i, fila[1], fila[2], fila[3], fila[4])
            i += 1
            
    archivo.close()
    
        
if __name__ == '__main__':
    lista_viajeros = []
    cargarLista(lista_viajeros)
    nv = int(input('Ingrese su numero de viajero: '))
    while nv <= 0 or nv > len(lista_viajeros):
        nv = int(input('Numero no valido. Intente nuevamente: '))
    nv -= 1
    bandera = False
    while not bandera:
        print("""
              0 Salir
              1 Consultar cantidad de millas
              2 Acumular millas
              3 Canjear millas""")
        opcion = int(input("Ingrese una opción: "))
        switch(opcion)
        bandera = int(opcion)==0 
    
    