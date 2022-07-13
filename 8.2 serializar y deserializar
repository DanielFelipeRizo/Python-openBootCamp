import pickle

class vehiculo():
    marca = ''
    modelo = ''
    cilindraje = ''

    def __init__(self, marcaM, modeloM, cilindrajeM):
        self.marca = marcaM
        self.modelo = modeloM
        self.cilindraje = cilindrajeM

    def obtenerInfo(self):
        return self.marca, self.modelo, self.cilindraje

#
objVehiculo = vehiculo('mazda', '2020', '1500')

#Serializar o guardar en un archivo instancia de clase vehiculo
guardarObjVehiculo = open('ObjCarro.bin', 'wb')
pickle.dump(objVehiculo, guardarObjVehiculo)
guardarObjVehiculo.close()


#deserializar orchivo ObjCarro.bin
abc = open('ObjCarro.bin', 'rb')
carro = pickle.load(abc)
print(carro.obtenerInfo())
