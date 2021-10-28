import sys
from tkinter import filedialog, Tk
from PyQt5 import uic
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtGui import QIcon, QImage, QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
import webbrowser
import imgkit
from analizadorLexico import *
from analizadorLexico import *
from html2image import Html2Image
from analizadorSintactico import analizadorSintactico
from Productos import Productos
global archivo
global herramienta
global herramientaDos

class principal(QMainWindow):
    
    def __init__(self):
        global archivo
        super().__init__()
        uic.loadUi("gui_app.ui", self)
        self.consola.setWordWrap(True)
        self.botonCargar.clicked.connect(self.cargaArchivo)
        self.botonSalir.clicked.connect(self.salirr)
        self.botonAnalizar.clicked.connect(self.analizar)
        self.botonGenerar.clicked.connect(self.generarReporte)

    def cargaArchivo(self):
        global archivo
        Tk().withdraw()
        file = filedialog.askopenfile(
            title = "Selecciona un archivo, porfavor.",
            initialdir = "./",
            filetypes = (
                ("Únicamente .lfp", "*.lfp"),
                ("todos los archivos",  "*.*")
            )
        )
        if file is None:
            print("No has seleccioado ningun archivo.")
            return None
        else:
            archivo = file.read()
            file.close()
            msgBox = QMessageBox()
            msgBox.setText("Tu archivo ha sido cargado exitosamente.")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.setInformativeText(":)")
            #self.consola.setText(archivo)
            msgBox.exec_()
            self.areaTexto.setPlainText(archivo)
            return archivo

    def analizar(self):
        global archivo
        global herramienta
        global herramientaDos
        herramienta = analizadorLexico()
        herramientaDos = analizadorSintactico()
        archivo = self.areaTexto.toPlainText()
        herramienta.scanner(archivo)
        #herramienta.ImprimirErrores()

        claves = herramientaDos.obtenerClaves(archivo)
        imprimir = herramientaDos.obtenerImprimir(archivo)
        imprimirln = herramientaDos.obtenerImprimirln(archivo)
        registros = herramientaDos.obtenerRegistros(archivo)
        comentario = herramientaDos.obtenerComentarios(archivo)
        conteo = herramientaDos.obtenerNoRegis(archivo)
        multiComent = herramientaDos.obtenerMultilinea(archivo)
        listaRegistros = []
        listaRegistros = herramientaDos.obtenerListaRegisto(archivo)
        promedioStock = herramientaDos.promedioStock(archivo)
        promedioCompra = herramientaDos.promedioCompra(archivo)
        promedioVenta = herramientaDos.promedioVenta(archivo)
        contar = herramientaDos.contarsi(archivo)
        maxi = herramientaDos.obtenerMaximo(archivo)
        mini = herramientaDos.obtenerMinimo(archivo)

        variableImpri = (comentario+multiComent+imprimir+imprimirln)
        if "conteo();" in archivo:
            variableImpri = (variableImpri +conteo)
        if 'promedio("stock");' in archivo:
            variableImpri = (variableImpri +promedioStock)
        if 'promedio("precio_compra");' in archivo:
            variableImpri = (variableImpri +promedioCompra)
        if 'promedio("precio_venta");' in archivo:
            variableImpri = (variableImpri +promedioVenta)
        if "contarsi" in archivo:
            variableImpri = (variableImpri +contar)
        if 'datos();' in archivo:
            variableImpri = (variableImpri + claves + registros)
        if "max(" in archivo:
            variableImpri = (variableImpri +"\n"+maxi)
        if "min(" in archivo:
            variableImpri = (variableImpri +"\n"+mini)
        
        #-------------------------------------------------
        if 'exportarReporte' in archivo:
            repo = herramientaDos.generarRepo(archivo)
            
        self.consola.setText(variableImpri)
        
        msgBox = QMessageBox()
        msgBox.setText("Tu archivo ha sido analizado con exito.")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.setInformativeText(":D")
        msgBox.exec_()


    def generarReporte(self):
        global herramienta
        tipo = self.comboRepos.currentText()
        if tipo == "Reporte de Tokens":
            msgBox = QMessageBox()
            msgBox.setText("Tu reporte de Tokens ha sido generado.")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.setInformativeText(":D")
            msgBox.exec_()
            herramienta.generarRepoTokens()
        elif tipo == "Reporte de Errores":
            msgBox = QMessageBox()
            msgBox.setText("Tu reporte de Erores ha sido generado.")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.setInformativeText(":/")
            msgBox.exec_()
            herramienta.generarRepoErrores()
        elif tipo == "Árbol de derivación":
            print("jeje")
        else:
            msgBox = QMessageBox()
            msgBox.setText("No seleccionaste Ninguna Opción.")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.setInformativeText(":(")
            msgBox.exec_()

    def salirr(self):
        sys.exit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = principal()
    GUI.show()
    sys.exit(app.exec_())