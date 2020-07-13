import sys
from PyQt5 import QtCore
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap, QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi

class Window(QMainWindow):
	def __init__(self):
		super(Window, self).__init__()
		loadUi('interface/mainwindow.ui', self)
		self.setWindowIcon(QIcon('red.png'))
		self.HelloWorldBT.clicked.connect(self.helloWindow)
		self.show()

	def helloWindow(self):
		self.tela = hello()

class hello(QMainWindow):
	def __init__(self):
		super(hello, self).__init__()
		loadUi('interface/hello.ui', self)
		self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Window = Window()
    Window.show()
    sys.exit(app.exec_())
    