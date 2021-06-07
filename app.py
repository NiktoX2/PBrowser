from PyQt5 import QtCore, QtWidgets
from ui import Ui_mainWindow


class mainWindow(QtWidgets.QWidget, Ui_mainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.setupUi(self)
        self.setMinimumSize(220, 200)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.closse.clicked.connect(self.closeApp)
        self.maxMin.clicked.connect(self.waxMinWindow)
        self.www.returnPressed.connect(self.load)
        self.web.load(QtCore.QUrl("https://google.com"))
        self.web.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.dragPos = QtCore.QPoint()
        self.waxMin = True

    def waxMinWindow(self):
        if self.waxMin is True:
            self.showMaximized()
            self.waxMin = False
        else:
            self.showNormal()
            self.waxMin = True

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

    def load(self):
        url = QtCore.QUrl.fromUserInput(self.www.text())
        if url.isValid():
            self.web.load(url)

    def closeApp(self):
        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    main = mainWindow()
    main.show()
    app.exec_()

# self.web = QtWebEngineWidgets.QWebEngineView(self.body)
# self.web.setObjectName("web")
# self.web.page().setBackgroundColor(QtGui.QColor("#000"))
