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
            return 'Palabra Reservada'
        elif self.tipo == self.signoIgual:
            return 'Signo Igual'
        elif self.tipo == self.cadena:
            return "Cadena de Texto"
        elif self.tipo == self.puntoComa:
            return "Punto Y Coma"
        elif self.tipo == self.numero:
            return "Número"
        elif self.tipo == self.llaveIz:
            return "Llave Izquierda"
        elif self.tipo == self.llaveD:
            return "Llave Derecha"
        elif self.tipo == self.corcheteIz:
            return "Corchete Izquierdo"
        elif self.tipo == self.corcheteD:
            return "Corchete Derecho"
        elif self.tipo == self.parentesisIz:
            return "Parentesis Izquierdo"
        elif self.tipo == self.parentesisD:
            return "Parentesis Derecho"
        elif self.tipo == self.coma:
            return "Coma"
        elif self.tipo == self.coment:
            return "Comentario"
        elif self.tipo == self.multiComent:
            return "Comentario Multilinea"
        elif self.tipo == self.error:
            return "Error"
