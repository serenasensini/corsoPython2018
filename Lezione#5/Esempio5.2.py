import sys
from PyQt4 import QtGui, QtCore # importiamo i moduli necessari


class MainWindow(QtGui.QMainWindow):
      def __init__(self):
              QtGui.QMainWindow.__init__(self)
              self.setWindowTitle('Box example')
              cWidget = QtGui.QWidget(self)
			  #horizontal layout
              hBox = QtGui.QHBoxLayout()
			  #vertical layout
			  #vbox = QtGui.QVBoxLayout()
			  cWidget.setLayout(hBox)
			  #cWidget.setLayout(vbox)
			  self.setCentralWidget(cWidget)
			  
test = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())