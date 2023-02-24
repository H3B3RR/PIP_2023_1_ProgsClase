import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile = "Prog_09_CambiaImagen.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.slider_img.setMinimum(0)
        self.slider_img.setMaximum(4)
        self.slider_img.setSingleStep(0)
        self.slider_img.setValue(0)

        self.slider_img.valueChanged.connect(self.cambiaImagen)

        self.listaImgs = []
        self.listaImgs.append(["Numero 1", ":/Numeros/uno.png"])
        self.listaImgs.append(["Numero 2", ":/Numeros/dos.png"])
        self.listaImgs.append(["Numero 3", ":/Numeros/tres.png"])
        self.listaImgs.append(["Numero 4", ":/Numeros/cuatro.png"])
        self.listaImgs.append(["Numero 5", ":/Numeros/cinco.png"])

        self.txt_valorA.setText("Numero 1")

    # Área de los Slots
    def cambiaImagen(self):
        imagen = self.listaImgs[self.slider_img.value()] #imagen -> nombre y la ruta
        self.txt_valorA.setText(imagen[0])
        self.img.setPixmap(QtGui.QPixmap(imagen[1]))



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

