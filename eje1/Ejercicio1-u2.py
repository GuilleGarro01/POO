import csv
class Email:
    __idcuenta = ""
    __dominio = ""
    __tipoDominio = ""
    __contraseña = ""
    
    def __init__(self,id="",dom="",tdom="",contr=""):
        self.__idcuenta = id
        self.__dominio = dom
        self.__tipoDominio = tdom
        self.__contraseña= contr
        
    def retornaEmail(self):
        return f"{self.__idcuenta}@{self.__dominio}.{self.__tipoDominio}"
    def getDominio(self):
        return self.__dominio
    def CrearCuenta(self, direccionDeCorreo):
        partes = direccionDeCorreo.split('@')
        self.__idcuenta = partes[0]
        __DominioYTipo = partes[1].split('.')
        self.__dominio = __DominioYTipo[0]
        self.__tipoDominio = __DominioYTipo[1]
        
if __name__ == "__main__":
    email = Email()
    nombre = input("Ingrese su nombre, por favor ")
    mail = input("Ingrese el email ")
    contraseña = input("Ingrese contraseña actual ")
    email.CrearCuenta(mail)
    print ("Estimado ", nombre, "te enviaremos tus mensajes a la dirección: ", email.retornaEmail())
    comparar = input("Ingrese contraseña antigua ")
    if contraseña == comparar:
        nueva = input("Ingrese contraseña nueva ")
        contraseña = nueva
    else: 
        print ("La contraseñas registrada, no coincide con la ingresada ")
    correo = input("Ingrese correo ")
    email2 = Email()
    email2.CrearCuenta(correo)
    archivo = open('lote1-eje1u2.csv')
    reader = csv.reader(archivo, delimiter=',')
    emails = []
    for fila in reader:
        if '@' in fila[0] and '.' in fila[0]:
            email3 = Email()
            email3.CrearCuenta(fila[0])
            emails.append(email3)
        else:
            print ("La dirección {} es incorrecto".format(fila[0]))
    archivo.close()
    #cant = 0
    with open('lote-eje1u2.csv') as file_object:
        lista= archivo.readline()
        listaN= lista.split(',')
        listaobjetos = list(map(lambda x: Email.CrearCuenta(x), listaN))
        cont = 0
        undominio = input("Ingrese el dominio para saber la cantidad ")
for cuenta in listaobjetos:
                if undominio == cuenta.getidcuenta():
                    cont= cont + 1
            if cont >=1
                print ("El dominio esta repetido " , )
                    
        
                    