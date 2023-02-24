import sys
from PyQt5 import uic, QtWidgets, QtGui, QtCore
qtCreatorFile = "Prog_10_Timer.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_iniciar.clicked.connect(self.iniciar)
        self.btn_iniciar_timer.clicked.connect(self.iniciar_timer)

        #Timer
        self.segundoPlano  = QtCore.QTimer() #objeto de tipo timer
        self.segundoPlano.timeout.connect(self.contador)


    # Área de los Slots
    def iniciar(self):
        n = int(self.txt_n.text())
        import time as t
        for i in range(n, 0, -1):
            print(i)
            self.lb_contador.setText(str(i))
            t.sleep(1) #1 segundo



    def iniciar_timer(self):
        self.val = int(self.txt_n_timer.text())
        self.segundoPlano.start(1000) ##ms

    def contador(self):
        self.lb_contador_timer.setText(str(self.val))
        self.val-=1
        if self.val<0:
            self.segundoPlano.stop()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

