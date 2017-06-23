
class codigoMorse(object):
    morse = {'a' : '.-'    , 'b' : '-...' ,  'c' : '-.-.' ,  'd' : '-..' ,  'e' : '.' ,   'f' : '..-.' , 'g' : '--.' ,   'h' : '....' ,
             'i' : '..'    , 'j' : '.---' ,  'k' : '-.-' ,   'l' : '.-..' , 'm' : '--' ,  'n' : '-.' ,   'o' : '---' , 'p' : '.--.' ,
             'q' : '--.-'  , 'r' : '.-.' ,   's' : '...' ,   't' : '-' ,    'u' : '..-' , 'v' : '...-' , 'w' : '.--' , 'x' : '-..-' ,
             'y' : '-.--'  , 'z' : '--..' ,  '1' : '.----',  '2' : '..---', '3':'...--',  '4' : '....-', '5' : '.....' , '6' : '-....' ,
             '7' : '--...' , '8' : '---..' , '9' : '----.' , '0' : '-----', ' ' : '___'}

    def agregarLetra(self, letra, codigo):
        self.morse[letra] = codigo

    def eliminarLetra(self, letra):
        del self.morse[letra]


    def traducirTexto(self,texto):
        oracion = ""
        for letra in texto:
            if letra in self.morse[letra]:
                oracion = oracion
            else:
                oracion = oracion + self.morse[letra] + "|"
        return oracion
