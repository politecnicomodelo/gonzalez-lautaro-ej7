from clases.pruebaMorse import codigoMorse
escrito = ""
codigo = codigoMorse()
opcion = 0
opcion = input("1: texto a morse, 2: morse a texto ")
escrito = input("ingrese el texto: ")
if (opcion == "1"):
    escrito = codigo.traducirTexto(escrito)
elif(opcion == "2"):
    escrito = codigo.traducirMorse(escrito)
print(escrito)