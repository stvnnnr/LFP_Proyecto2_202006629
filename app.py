import sys
from tkinter import filedialog, Tk
from PyQt5 import uic
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtGui import QIcon, QImage, QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
import webbrowser
import imgkit
from html2image import Html2Image
global archivo

class principal(QMainWindow):
    
    def __init__(self):
        global archivo
        super().__init__()
        uic.loadUi("gui_app.ui", self)
        self.consola.setWordWrap(True)
        self.botonCargar.clicked.connect(self.cargaArchivo)
        self.botonSalir.clicked.connect(self.salirr)

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
            print("Tu archivo ha sido cargado exitosamente.")
            self.areaTexto.setPlainText(archivo)
            self.consola.setText(archivo)
            return archivo

    def salirr(self):
        sys.exit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = principal()
    GUI.show()
    sys.exit(app.exec_())