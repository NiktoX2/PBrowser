from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1200, 720)
        self.verticalLayout = QtWidgets.QVBoxLayout(mainWindow)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.body = QtWidgets.QWidget(mainWindow)
        self.body.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-radius: 12px;")
        self.body.setObjectName("body")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.body)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.main = QtWidgets.QWidget(self.body)
        self.main.setMaximumSize(QtCore.QSize(16777215, 80))
        self.main.setStyleSheet("border-radius: 0px;")
        self.main.setObjectName("main")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.main)
        self.verticalLayout_3.setContentsMargins(9, -1, -1, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget = QtWidgets.QWidget(self.main)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 23))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.nameApp = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.nameApp.setFont(font)
        self.nameApp.setStyleSheet("color: rgb(255, 255, 255);")
        self.nameApp.setObjectName("nameApp")
        self.horizontalLayout_2.addWidget(self.nameApp)
        self.maxMin = QtWidgets.QPushButton(self.widget)
        self.maxMin.setMinimumSize(QtCore.QSize(0, 20))
        self.maxMin.setMaximumSize(QtCore.QSize(20, 16777215))
        self.maxMin.setStyleSheet("background-color: rgb(91, 91, 91);\n"
"border-radius: 10px;")
        self.maxMin.setText("")
        self.maxMin.setObjectName("maxMin")
        self.horizontalLayout_2.addWidget(self.maxMin)
        self.closse = QtWidgets.QPushButton(self.widget)
        self.closse.setMinimumSize(QtCore.QSize(0, 20))
        self.closse.setMaximumSize(QtCore.QSize(20, 16777215))
        self.closse.setStyleSheet("background-color: rgb(170, 0, 0);\n"
"border-radius: 10px;")
        self.closse.setText("")
        self.closse.setObjectName("closse")
        self.horizontalLayout_2.addWidget(self.closse)
        self.verticalLayout_3.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.main)
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Button_1 = QtWidgets.QPushButton(self.widget_2)
        self.Button_1.setMinimumSize(QtCore.QSize(20, 20))
        self.Button_1.setMaximumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.Button_1.setFont(font)
        self.Button_1.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.Button_1.setObjectName("Button_1")
        self.horizontalLayout.addWidget(self.Button_1)
        self.Button_2 = QtWidgets.QPushButton(self.widget_2)
        self.Button_2.setMinimumSize(QtCore.QSize(20, 20))
        self.Button_2.setMaximumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.Button_2.setFont(font)
        self.Button_2.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.Button_2.setObjectName("Button_2")
        self.horizontalLayout.addWidget(self.Button_2)
        self.Button_3 = QtWidgets.QPushButton(self.widget_2)
        self.Button_3.setMinimumSize(QtCore.QSize(20, 20))
        self.Button_3.setMaximumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.Button_3.setFont(font)
        self.Button_3.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.Button_3.setObjectName("Button_3")
        self.horizontalLayout.addWidget(self.Button_3)
        self.www = QtWidgets.QLineEdit(self.widget_2)
        self.www.setMinimumSize(QtCore.QSize(0, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.www.setFont(font)
        self.www.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"color: rgb(255, 255, 255);")
        self.www.setObjectName("www")
        self.horizontalLayout.addWidget(self.www)
        self.verticalLayout_3.addWidget(self.widget_2)
        self.verticalLayout_2.addWidget(self.main)
        self.web = QtWebEngineWidgets.QWebEngineView(self.body)
        self.web.setObjectName("web")
        self.web.page().setBackgroundColor(QtGui.QColor("#000"))
        self.verticalLayout_2.addWidget(self.web)
        self.verticalLayout.addWidget(self.body)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Browser"))
        self.nameApp.setText(_translate("mainWindow", "LSBrowser"))
        self.Button_1.setText(_translate("mainWindow", "🡄"))
        self.Button_2.setText(_translate("mainWindow", "🡆"))
        self.Button_3.setText(_translate("mainWindow", "⭯"))
