class Token():
    lexemaValido = ''
    tipo = 0
    fila = 0
    columna = 0
    palabraReservada = 1
    signoIgual = 2
    cadena = 3
    puntoComa = 4
    numero = 5
    llaveIz = 6
    llaveD = 7
    corcheteIz = 8
    corcheteD = 9
    parentesisIz = 10
    parentesisD = 11
    coma = 12
    coment = 13
    multiComent = 14
    error = 15

    def __init__(self, lexema, tipo, fila, columna):
        self.lexemaValido = lexema
        self.tipo = tipo
        self.fila = fila
        self.columna = columna

    def getLexema(self):
        return self.lexemaValido

    def getFila(self):
        return self.fila

    def getColumna(self):
        return self.columna

    def getTipo(self):
        if self.tipo == self.palabraReservada:
            return 'palabraReservada'
        elif self.tipo == self.signoIgual:
            return 'signoIgual'
        elif self.tipo == self.cadena:
            return "cadena"
        elif self.tipo == self.puntoComa:
            return "puntoComa"
        elif self.tipo == self.numero:
            return "numero"
        elif self.tipo == self.llaveIz:
            return "llaveIz"
        elif self.tipo == self.llaveD:
            return "llaveD"
        elif self.tipo == self.corcheteIz:
            return "corcheteIz"
        elif self.tipo == self.corcheteD:
            return "corcheteD"
        elif self.tipo == self.parentesisIz:
            return "parentesisIz"
        elif self.tipo == self.parentesisD:
            return "parentesisD"
        elif self.tipo == self.coma:
            return "coma"
        elif self.tipo == self.coment:
            return "coment"
        elif self.tipo == self.multiComent:
            return "multiComent"
        elif self.tipo == self.error:
            return "error"
