import sys
from PyQt5 import QtCore, QtWebEngineWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

class Ui_MainWindows(object):
    def SetupUi(self, Ui_MainWindows):
        MainWindow.setWindowTitle("HTML5测试")
        MainWindow.resize(800,600)
        #加载外部的web页
        self.browser = QtWebEngineWidgets.QWebEngineView(MainWindow)
        self.browser.setGeometry(QtCore.QRect(0,0,800,600))
        self.browser.load(QtCore.QUrl("http://chrome.360.cn/test/html5/"))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow =QMainWindow()
    ui = Ui_MainWindows()
    ui.SetupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

