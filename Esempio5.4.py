import sys
from PyQt4 import QtGui, QtCore # importiamo i moduli necessari


class MainWindow(QtGui.QMainWindow):
      def __init__(self):
              QtGui.QMainWindow.__init__(self)
              self.setWindowTitle(‘Finestra Principale’)
			  cWidget = QtGui.QWidget(self)
			  #horizontal layout
              hBox = QtGui.QHBoxLayout()
			  #pulsante
			  button1 = QtGui.QPushButton('Chiudi finestra');
              button1.setFont(QtGui.QFont("Arial", 15, QtGui.QFont.Italic));
			  #segnale per il pulsante 1
			  self.connect(button1, QtCore.SIGNAL('clicked()'), QtCore.SLOT('close()'));
			  hBox.addWidget(randomLabel)
			  self.setCentralWidget(button)
			  
test = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())

