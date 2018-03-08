import sys
from PyQt4 import QtGui, QtCore # importiamo i moduli necessari


class MainWindow(QtGui.QMainWindow):
      def __init__(self):
              QtGui.QMainWindow.__init__(self)
              self.setWindowTitle('Menu di prova')
			  #pulsante esci
              quit = QtGui.QAction(null, "Quit", self)
              quit.setShortcut("Ctrl+Q")
              self.connect(quit, QtCore.SIGNAL('clicked()'), QtCore.SLOT('close()'))
			  #separatore tra i bottoni
              sep = QtGui.QAction(self)
              sep.setSeparator(True)
			  #pulsante informazioni
              info = QtGui.QAction(null, "Information", self)
              info.setShortcut("Ctrl+I")
              self.connect(info, QtCore.SIGNAL('clicked()'), self.mySlot)
			  #mostro toolbar
              self.statusBar().show()
			  #creo menu
              menu = self.menuBar()
              home = menu.addMenu('&Home')
              home.addAction(quit)
              home.addAction(sep)
              home.addAction(info)
			  
test = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())

