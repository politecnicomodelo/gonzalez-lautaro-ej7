class persona(object):
    nombre = ""
    apellido = ""

    def setNyA(self,n,a):
        self.nombre = n
        self.apellido = a

    def getNombre(self):
        return self.nombre

    def getApellido(self):
        return self.apellido

    def getDescuento(self):
        return 0