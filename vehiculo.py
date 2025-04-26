class Vehiculo:
    def __init__ (self, modelo, marca):
        self.marca = marca
        self.modelo = modelo

    def descripcion (self):
        return f"{self.marca} {self.modelo}"

class Automovil (Vehiculo):
    def __init__ (self, marca, modelo, puertas):
        super ().__init__ (marca, modelo)
        self.puertas = puertas

    def mostrar_detalles (self):
        base = super ().descripcion ()
        return f"{base} con {self.puertas} puertas"

v = Vehiculo ("Generic", "MoselECS")
print (v.descripcion())

a = Automovil ("Toyota", "Corolla", 4)
print (a.mostrar_detalles())