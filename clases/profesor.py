from persona import persona

class profesor(persona):
    descuento = 0

    def getDescuento(self):
        return self.descuento

    def setDescuento(self,d):
        self.descuento = d
