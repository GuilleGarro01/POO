import csv
class Viajero:
    __num_viajero= ""
    __dni= ""
    __nombre= ""
    __apellido= ""
    __millas_acum= 0
    
    def __init__ (self,num_viajero="",dni="",nombre="",apellido="",millas_acum=0):
        self.__num_viajero = num_viajero
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__millas_acum = millas_acum
    
    def cantTotMillas(self):
        return(self.__millas_acum)
    def acumularMillas(self,m):
        self.__millas_acum= self.__millas_acum + m
        return (self.__millas_acum)
    def canjearMillas(self,canje):
        if (canje >=self.__millas_acum):
            return print("Puede realizar el canje, sus millas totales son: ",self.__millas_acum)
        else:
            return print("No puede realizar el canje, sigue acumulando para poder canjear ")
    def verifnum(self,numero):
        if self.__num_viajero == numero:
            return True
    def ingreso(lista):
        numviajero = input("Ingrese un numero de viajero: ")
        for i in range(len(lista)):
            if lista[i].verifnum(numviajero) == True:
                print("El valor de i es de ",lista[i])
                return i
            
    # def mostrar(self):
    #     print('El numero de viajero es:{}'.format(self.__num_viajero))
    #     print('El DNI es:{}'.format(self.__dni))
    #     print('El nombre es: {}'.format(self.__nombre))
    #     print('El apellido es:{}'.format(self.__apellido))
    #     print('Las millas acumuladas son: {}'.format(self.__millas_acum))
    
                
            
if __name__ == "__main__":
    lista = []
    unViajero= Viajero()
    archivo = open('Lote de prueba eje 2.csv')
    reader = csv.reader(archivo, delimiter=',')
    num=Viajero.ingreso(lista)

    for linea in reader:
        lista.append(Viajero(linea[0], linea[1],linea[2],linea[3],linea[4])) 
        #for i in range(len(lista)):
        #lista[i].mostrar()
    print ("1. Consultar millas ")
    print ("2. Acumular ")
    print ("3. Canjear ")
    print ("4. Salir ")
           
    opc = int(input("1Ingrese opcion  ")) 
    while opc !=4:
        if opc == 1:
            print ("La cantidad de millas son: {} ".format(lista.cantTotMillas()))
        elif opc == 2:
            millas= int(input("Ingrese cantidad de millas a acumular "))
            unViajero[num].acumularMillas(millas)
        elif opc == 3:
            millasACanjear = int(input("Ingrese la cantidad de millas a canjear "))
            unViajero[num].canjearMillas(millasACanjear)
        elif opc == 4:
            print ("\n Gracias por ingresar ")
        opc = int(input("2Ingrese opcion "))