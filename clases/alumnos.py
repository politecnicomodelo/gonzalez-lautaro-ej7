from persona import persona

class alumno(persona):
    division = 0

    def setDivision(self,di):
        self.division = di

    def getDivision(self):
        return self.division