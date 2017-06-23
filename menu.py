from clases.profesor import profesor
from clases.alumnos import alumno
from clases.plato import plato
from clases.pedido import pedido
from datetime import date


profesores = []
alumnoss = []
platos = []
pedidos = []

def agregarProfesor():
    unProf=profesor
    unProf.setNyA(input("nombre: "),input("apellido: "))
    unProf.setDescuento(input("descuento: "))
    profesores.append(unProf)

def agregarAlumno():
    unAlum=alumno
    unAlum.setNyA(input("nombre: "),input("apellido: "))
    unAlum.setDivision(input("division: "))
    self.alumno.append(unAlum)

def agregarPlato():
    unPlato=plato
    unPlato.setPlato(input("nombre: "),input("precio: "))
    self.platos.append(unPlato)

def agregarPedido():
    unPedido=pedido
    nombrePersona = input("nombre: ")
    apellidoPersona = input("apellido: ")
    nombrePlatillo = input("plato: ")
    b = 0
    buscandoPersona = 0
    for item in self.profesores:
        if item.getNombre == nombrePersona:
            if item.getApellido == apellidoPersona:
                b = 1
                break
        buscandoPersona = buscandoPersona+1
    if b == 0:
        for item in self.alumno:
            if item.getNombre == nombrePersona:
                if item.getApellido == apellidoPersona:
                    b = 2
                    break
            buscandoPersona = buscandoPersona+1
    buscandoPlato = 0
    existe = 0
    for buscar in self.platos:
        if buscar == nombrePlatillo:
            existe = 1
            break
        buscandoPlato = buscandoPlato+1
    if existe == 1:
        if b == 1:
            unPedido.setPedido(input("fecha: "), self.profesores[buscandoPersona], self.platos[buscandoPlato], time, false)
        elif b == 2:
            unPedido.setPedido(input("fecha: "), self.alumno[buscandoPersona], self.platos[buscandoPlato], time, false)
        else:
            print("no se encuentra la persona")
    else:
        print("no existe el plato")

agregarAlumno()