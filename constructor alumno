class alumno:
    nombreAlumno = ''
    notaAlumno = ''

    def __init__(self, nombreParam='', notaParam=''):

        self.nombreAlumno = nombreParam
        self.notaAlumno = notaParam
        if (notaParam > 5):
            print('la nota maxima es 5.0')
            exit()

    def mostarDatosAlumno(self):

        return self.nombreAlumno, self.notaAlumno

    def saberAprobo(self):
        if (self.notaAlumno >= 3.0):
            return 'el estudiante ', self.nombreAlumno, 'aprobo con ', self.notaAlumno
        else:
            return 'el estudiante ', self.nombreAlumno, 'reprobo con ', self.notaAlumno


a = alumno('Juan', 4.8)

print(a.nombreAlumno, a.notaAlumno)

print(a.mostarDatosAlumno())

print(a.saberAprobo())
