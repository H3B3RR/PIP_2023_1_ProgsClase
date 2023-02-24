import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile = "Prog_12_DatosImagenes.ui"  # Nombre del archivo aquí.
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

        import Modulo_Contactos as contactos
        self.contacts = contactos.cargarContactos()

        self.obtieneDatosContacto(0)

    # Área de los Slots
    def cambiaImagen(self):
        indice = self.slider_img.value()

        imagen = self.listaImgs[indice] #imagen -> nombre y la ruta
        self.txt_valorA.setText(imagen[0])
        self.img.setPixmap(QtGui.QPixmap(imagen[1]))

        self.obtieneDatosContacto(indice)

    def obtieneDatosContacto(self, indice):
        datosContacto  = self.contacts[indice]
        self.txt_nombre.setText(datosContacto[0]) #nombre
        self.txt_carrera.setText(datosContacto[1])  # carrera
        self.txt_edad.setText(datosContacto[2])  # edad



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

