import re

from Productos import Productos


class analizadorSintactico:

    def obtenerClaves(self, entrada):
        patron = r'"(.*?)"'
        separaUno = entrada.split("Claves = [\n")
        separados = separaUno[1].split("\n]\n")
        separatres = separados[0]
        listaClaves = re.findall(patron,separatres)
        claves = ",".join(listaClaves)
        claves = (claves+"\n")
        return claves
    
    def obtenerRegistros(self, entrada):
        patron = r'{(.*?)}'
        separaUno = entrada.split("Registros = [\n")
        separados = separaUno[1].split("\n]\n")
        separatres = separados[0]
        listaClaves = re.findall(patron,separatres)
        claves = "\n".join(listaClaves)
        claves = (claves+"\n")
        return claves
    
    def obtenerListaRegisto(self, entrada):
        patron = r'{(.*?)}'
        separaUno = entrada.split("Registros = [\n")
        separados = separaUno[1].split("\n]\n")
        separatres = separados[0]
        listaClaves = re.findall(patron,separatres)
        claves = "#".join(listaClaves)
        patronDos = r'"(.*?)"'
        listaProductos = []
        for cla in range(len(listaClaves)):
            separada = listaClaves[cla].split(",")
            codigo = str(separada[0])
            producto = re.findall(patronDos,separada[1])[0]
            compra = separada[2]
            venta = separada[3]
            stock = separada[4]
            producto = Productos(codigo, producto, compra, venta, stock)
            listaProductos.append(producto)
        return listaProductos

        return claves
    
    def obtenerNoRegis(self, entrada):
        patron = r'{(.*?)}'
        separaUno = entrada.split("Registros = [\n")
        separados = separaUno[1].split("\n]\n")
        separatres = separados[0]
        listaClaves = re.findall(patron,separatres)
        claves = str(len(listaClaves))
        return claves
    
    def obtenerImprimir(self, entrada):
        separaUno = entrada.split("imprimir(")
        separaDos = separaUno[1]
        separaTres = separaDos.split(");")
        palabra = separaTres[0]
        patron = r'"(.*?)"'
        palabraImp = re.findall(patron,palabra)
        Imp = "\n".join(palabraImp)
        Imp = (Imp+"\n")
        return Imp
    
    def obtenerImprimirln(self, entrada):
        separaUno = entrada.split("imprimirln(")
        separaDos = separaUno[1]
        separaTres = separaDos.split(");")
        palabra = separaTres[0]
        patron = r'"(.*?)"'
        palabraImp = re.findall(patron,palabra)
        Imp = "\n".join(palabraImp)
        Imp = (Imp+"\n")
        return Imp
    
    def obtenerComentarios(self, entrada):
        separaUno = entrada.split("#")
        separaDos = separaUno[1]
        separaTres = separaDos.split("\n")
        palabra = separaTres[0]
        return palabra

    def obtenerMultilinea(self, entrada):
        separaUno = entrada.split("'''\n")
        separaDos = separaUno[1]
        separaTres = separaDos.split("\n'''")
        palabra = separaTres[0]
        return palabra
