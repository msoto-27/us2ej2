class ViajeroFrecuente:
    __num_viajero = ''
    __dni = ''
    __nombre = ''
    __apellido = ''
    __millas_acumuladas = ''
    def __init__(self, num_viajero, dni, nombre, apellido, millas_acumuladas):
        self.__num_viajero = num_viajero
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__millas_acumuladas = millas_acumuladas
    def cantidadTotaldeMillas(self):
        return self.__millas_acumuladas
    def acumularMillas(self, millas):
        self.__millas_acumuladas += millas
        print(millas, 'han sido acumuladas')
    def canjearMillas(self, millas):
        if(self.__millas_acumuladas >= millas):
            self.__millas_acumuladas -= millas
            print(millas, 'han sido canjeadas')
        else:
            print('Error en la operacion. No cuenta con la cantidad de millas suficiente')