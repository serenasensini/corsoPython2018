import sys
from PyQt4 import QtGui, QtCore # importiamo i moduli necessari


class MainWindow(QtGui.QMainWindow):
      def __init__(self):
              QtGui.QMainWindow.__init__(self)
              self.resize(400, 200)
              self.setWindowTitle(‘Finestra Principale’)
			  #label
			  label = QtGui.QLabel('Testo qualsiasi');
			  self.setCentralWidget(label)
			  
test = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())

