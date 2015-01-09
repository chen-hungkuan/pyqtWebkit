# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formMainUI.ui'
#
# Created: Tue Nov 18 11:52:55 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_formMain(object):
    def setupUi(self, formMain):
        formMain.setObjectName(_fromUtf8("formMain"))
        formMain.resize(800, 640)
        self.verticalLayout = QtGui.QVBoxLayout(formMain)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.webView = QtWebKit.QWebView(formMain)
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.verticalLayout.addWidget(self.webView)

        self.retranslateUi(formMain)
        QtCore.QMetaObject.connectSlotsByName(formMain)

    def retranslateUi(self, formMain):
        formMain.setWindowTitle(_translate("formMain", "webkit", None))

from PyQt4 import QtWebKit
