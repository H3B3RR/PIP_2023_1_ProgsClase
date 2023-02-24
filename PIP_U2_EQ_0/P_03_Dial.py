import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "Prog_03_Dial.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.dial.setMinimum(-10)
        self.dial.setMaximum(10)
        self.dial.setSingleStep(1)
        self.dial.setValue(0)

        self.dial.valueChanged.connect(self.cambiaValor)
        self.txt_valor.setText("0")

    # Área de los Slots
    def cambiaValor(self):
        self.txt_valor.setText(str(self.dial.value()))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

