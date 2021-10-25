import sys
from tkinter import filedialog, Tk
from PyQt5 import uic
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtGui import QIcon, QImage, QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
import webbrowser
import imgkit
from analizadorLexico import *
from html2image import Html2Image
global archivo
global herramienta

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
        herramienta = analizadorLexico()
        archivo = self.areaTexto.toPlainText()
        herramienta.scanner(archivo)
        herramienta.ImprimirErrores()

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