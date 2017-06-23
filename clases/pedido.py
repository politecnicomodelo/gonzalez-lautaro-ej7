from datetime import date
from datetime import time
from clases.persona import persona
from clases.profesor import profesor
from clases.plato import plato

class pedido(object):
    fechaCreacion = date
    cliente = persona
    platoPedido = plato
    horaEntre = time
    Estado = False

    def setPedido(self,f,c,p,h,e):
        self.fechaCreacion = f
        self.cliente = c
        self.platoPedido = p
        self.horaEntre = h
        self.Estado = e

    def getFecha(self):
        return self.fechaCreacion

    def getCliente(self):
        return self.cliente

    def getPlato(self):
        return self.platoPedido

    def getHora(self):
        return self.horaEntre

    def getEstado(self):
        return self.Estado

    def calcularPrecio(self):
        return (((100-profesor.getDescuento())*plato.getPrecio())/100)