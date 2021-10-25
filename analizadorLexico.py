from Token import Token

global tiposToken
global listaTokens

class analizadorLexico:
    global tiposToken
    lexema = ""
    listaTokens = []
    fila = 1
    columna = 1
    estado = 0
    comprobadorErrores = False

    #Formato de token con valores -1 para un mejor manejo de fallas
    tiposToken = Token("lexemaInicial", -1, -1, -1)


    def scanner(self, texto):
        global title
        union = ''
        usando = ''
        tamanio = len(texto)
        self.lexema = ''
        self.listaTokens = []
        self.fila = 1
        self.columna = 1
        self.estado = 0
        self.comprobadorErrores = True

        for i in range(tamanio):
            actual = texto[i]
            if self.estado == 0:
                if actual.isalpha():
                    self.estado = 1
                    self.columna += 1
                    self.lexema += actual
                    continue
                elif actual == '"':
                    self.estado = 3
                    self.columna +=1
                    self.lexema += actual
                    continue
                elif actual.isdigit():
                    self.estado = 5
                    self.columna +=1
                    self.lexema += actual
                    continue
                elif actual == "#":
                    self.estado = 6
                    self.columna +=1
                    self.lexema +=actual
                    continue
                elif actual == "'":
                    self.estado = 7
                    self.columna +=1
                    self.lexema += actual
                    continue
                elif actual == "\n":
                    self.estado = 0
                    self.columna = 1
                    self.fila +=1
                    continue
                elif actual == " ":
                    self.estado = 0
                    self.columna +=1
                    continue
                elif actual == "=":
                    self.estado = 0
                    self.columna +=1
                    self.lexema = actual
                    self.agregarToken(tiposToken.signoIgual)
                    continue
                elif actual == "[":
                    self.estado = 0
                    self.columna +=1
                    self.lexema = actual
                    self.agregarToken(tiposToken.corcheteIz)
                    continue
                elif actual == "]":
                    self.estado = 0
                    self.columna += 1
                    self.lexema = actual
                    self.agregarToken(tiposToken.corcheteD)
                    continue
                elif actual == ",":
                    self.columna += 1
                    self.lexema = actual
                    self.agregarToken(tiposToken.puntoComa)
                    self.estado = 0
                    continue
                elif actual == "{":
                    self.estado = 0
                    self.columna += 1
                    self.lexema = actual
                    self.agregarToken(tiposToken.llaveIz)
                    continue
                elif actual == "}":
                    self.estado = 0
                    self.columna += 1
                    self.lexema = actual
                    self.agregarToken(tiposToken.llaveD)
                    continue
                elif actual == ";":
                    self.estado = 0
                    self.columna += 1
                    self.lexema = actual
                    self.agregarToken(tiposToken.puntoComa)
                    continue
                elif actual == "(":
                    self.estado = 0
                    self.columna +=1
                    self.lexema = actual
                    self.agregarToken(tiposToken.parentesisIz)
                    continue
                elif actual == ")":
                    self.estado = 0
                    self.columna += 1
                    self.lexema = actual
                    self.agregarToken(tiposToken.parentesisD)
                    continue
                else:
                    self.columna +=1
                    self.lexema += actual
                    self.estado = 0
                    self.agregarToken(tiposToken.error)

            elif self.estado == 1:
                if actual.isalpha():
                    self.estado = 1
                    self.columna +=1
                    self.lexema += actual
                    continue
                elif actual == " ":
                    if self.palabraRes(self.lexema):
                        self.agregarToken(tiposToken.palabraReservada)
                        self.estado=0
                        continue
                elif actual == "(":
                    if self.palabraRes(self.lexema):
                        self.agregarToken(tiposToken.palabraReservada)
                    self.lexema = actual
                    self.columna += 1
                    self.agregarToken(tiposToken.parentesisIz)
                    continue
                else:
                    self.lexema += actual
                    self.columna +=1
                    self.agregarToken(tiposToken.error)
                    self.estado = 0

            elif self.estado == 3:
                if actual != '"':
                    self.estado = 3
                    self.columna +=1
                    self.lexema += actual
                    continue
                elif actual == '"':
                    self.columna +=1
                    self.lexema += actual
                    self.agregarToken(tiposToken.cadena)
                    self.estado = 0
                    continue
                else:
                    self.columna +=1
                    self.lexema += actual
                    self.estado = 0
                    self.agregarToken(tiposToken.error)

            elif self.estado == 5:
                if actual.isdigit():
                    self.estado = 5
                    self.columna +=1
                    self.lexema +=actual
                    continue
                elif actual == '.':
                    self.estado = 5
                    self.columna += 1
                    self.lexema +=actual
                    continue
                elif actual == ",":
                    self.columna +=1
                    self.agregarToken(tiposToken.numero)
                    self.lexema = actual
                    self.agregarToken(tiposToken.coma)
                    self.estado = 0
                    continue
                elif actual == "}":
                    self.columna +=1
                    self.agregarToken(tiposToken.numero)
                    self.lexema = actual
                    self.agregarToken(tiposToken.llaveIz)
                    self.estado = 0
                    continue
                elif actual == ")":
                    self.columna +=1
                    self.agregarToken(tiposToken.numero)
                    self.lexema = actual
                    self.agregarToken(tiposToken.parentesisD)
                    self.estado = 0
                    continue
                else:
                    self.lexema = actual
                    self.columna +=1
                    self.agregarToken(tiposToken.error)
                    continue

            elif self.estado == 6:
                if actual != '\n':
                    self.estado = 6
                    self.columna +=1
                    self.lexema += actual
                    continue
                elif actual == '\n':
                    self.columna +=1
                    self.lexema += actual
                    self.agregarToken(tiposToken.coment)
                    self.estado = 0
                    continue
                else:
                    self.columna +=1
                    self.lexema += actual
                    self.estado = 0
                    self.agregarToken(tiposToken.error)

            elif self.estado == 7:
                if actual == "'":
                    self.estado = 7
                    self.columna +=1
                    self.lexema += actual
                    if self.lexema == "'''":
                        self.estado = 8
                    continue
                else:
                    self.columna +=1
                    self.lexema += actual
                    self.estado = 0
                    self.agregarToken(tiposToken.error)

            elif self.estado == 8:
                if actual == "'":
                    union += actual
                    self.columna +=1
                    self.lexema += actual
                    self.estado = 8
                    if union == "'''":
                        self.agregarToken(tiposToken.multiComent)
                        union = ''
                    continue
                elif actual == "\n":
                    self.columna = 1
                    self.fila +=1
                    self.columna = 1
                    self.lexema += actual
                    continue
                elif actual.isalpha():
                    self.columna +=1
                    self.lexema += actual
                    self.estado = 8
                    continue
                elif actual.isdigit():
                    self.columna += 1
                    self.lexema += actual
                    self.estado = 8
                    continue
                elif actual == " ":
                    self.columna +=1
                    self.lexema += actual
                    self.estado = 8
                    continue
                else:
                    self.columna +=1
                    self.lexema += actual
                    self.estado = 0
                    self.agregarToken(tiposToken.error)


    def agregarToken(self, tipo):
        self.listaTokens.append(Token(self.lexema, tipo, self.fila, self.columna))
        self.lexema = ""
        self.estado = 0
        self.columna = 1


    def palabraRes(self, texto=''):
        texto = texto.lower()
        valor = False
        reservadas = ["claves", "registros", "imprimir", "imprimirln", "conteo", "promedio", "contarsi","datos","sumar", "max","min","exportarreporte"]
        if texto in reservadas:
            valor = True
        return valor


    # def Imprimir(self):
    #     global tiposToken
    #     for x in self.listaTokens:
    #         if x.tipo != tiposToken.error:
    #             print(x.getLexema(), "-->", x.getTipo(), '-->', x.getFila(), '-->', x.getColumna())
    
    def ImprimirErrores(self):
        global tiposToken
        for x in self.listaTokens:
            if x.tipo == tiposToken.error:
                print(x.getLexema(), "-->", x.getFila(), '-->', x.getColumna(), '-->Error Lexico')


    def generarRepoTokens(self):
        file = open("Reporte Tokens.html", "w")
        head = f"""
                <!DOCTYPE html>
                <html lang="en">
                <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <link rel="stylesheet" href="reporte.css" type="text/css" />
                <title>Document</title>
                </head>
                <body>
                <h1><span class="yellow">Reporte de: </span><span class="blue">&lt;</span>Tokens<span class="blue">&gt;</span></h1>
                <h3>Tokens</h3>
                <table class="container">
                 <thead>
                 <tr>
                 <th>
                 <h1>LEXEMA</h1>
                 </th>
                 <th>
                 <h1>TOKEN</h1>
                 </th>
                 <th>
                 <h1>FILA</h1>
                 </th>
                 <th>
                 <h1>COLUMNA</h1>
                 </th>
                 </tr>
                 </thead>
                 <tbody>
                """
        file.write(head)
        for x in self.listaTokens:
            if x.tipo != tiposToken.error:
                linea = f"""
                <tr>
                <td>{x.getLexema()}</td>
                <td>{x.getTipo()}</td>
                <td>{x.getFila()}</td>
                <td>{x.getColumna()}</td>
                </tr>
                """
                file.write(linea)
        end1 = f"""
        </tbody>
        </table>
        """
        file.write(end1)
        endd = f"""
        </body>
        </html>
        """
        file.write(endd)
        file.close()


    def generarRepoErrores(self):
        file = open("Reporte Errores.html", "w")
        head = f"""
                <!DOCTYPE html>
                <html lang="en">
                <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <link rel="stylesheet" href="reporte.css" type="text/css" />
                <title>Document</title>
                </head>
                <body>
                <h1><span class="yellow">Reporte de: </span><span class="blue">&lt;</span>Errores Lexicos<span class="blue">&gt;</span></h1>
                <h3>Tokens</h3>
                <table class="container">
                 <thead>
                 <tr>
                 <th>
                 <h1>LEXEMA</h1>
                 </th>
                 <th>
                 <h1>TOKEN</h1>
                 </th>
                 <th>
                 <h1>FILA</h1>
                 </th>
                 <th>
                 <h1>COLUMNA</h1>
                 </th>
                 </tr>
                 </thead>
                 <tbody>
                """
        file.write(head)
        for x in self.listaTokens:
            if x.tipo == tiposToken.error:
                linea = f"""
                <tr>
                <td>{x.getLexema()}</td>
                <td>{x.getTipo()}</td>
                <td>{x.getFila()}</td>
                <td>{x.getColumna()}</td>
                </tr>
                """
                file.write(linea)
        end1 = f"""
        </tbody>
        </table>
        """
        file.write(end1)
        endd = f"""
        </body>
        </html>
        """
        file.write(endd)
        file.close()