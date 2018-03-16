import sys
from PyQt4 import QtGui, QtCore # importiamo i moduli necessari


class MainWindow(QtGui.QMainWindow):
      def __init__(self):
              QtGui.QMainWindow.__init__(self)
              self.setWindowTitle('Box example')
              cWidget = QtGui.QWidget(self)
			  #aggiunta griglia
			  grid = QtGui.QGridLayout(cWidget) 
			  cWidget.setLayout(grid)
			  self.setCentralWidget(cWidget)
			  
test = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())

