# -*- coding: utf-8 -*-
"""
Created on Wed Nov 05 11:09:57 2014

@author: pedro
"""
import sys, os
import resources
from formMainUI import Ui_formMain
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtNetwork import *
from PyQt4.QtWebKit import *


class WebPage(QWebPage):
    def javaScriptConsoleMessage(self, msg, line, source):
        print '%s line %d: %s' % (source, line, msg)

class PyAgent(QObject):
    def __init__(self):
        QObject.__init__(self)
        self.socket = QUdpSocket()
    
    @pyqtSlot(str)
    def sendMessage(self, pMsg):
        self.socket.writeDatagram(pMsg, QHostAddress.LocalHost, 12000)
        
    @pyqtSlot(str, str)
    def shellExecute(self, pCmd, pParm):
        os.popen('%s %s'%(pCmd, pParm))
        
    @pyqtSlot(str)
    def printPage(self, pUrl):
        self.web = QWebView()
        self.web.setUrl(QUrl(pUrl))
        self.web.loadFinished.connect(self.printPage_ready)
        """
        dialog = QPrintDialog(printer)
        if (dialog.exec_() == QDialog.Accepted):
            web.page().mainFrame().print_(printer)
        """
        
    def printPage_ready(self):
        printer = QPrinter()
        printer.setPageMargins(5,5,5,5,QPrinter.Millimeter)
        preview = QPrintPreviewDialog(printer)
        preview.paintRequested.connect(self.web.page().mainFrame().print_)
        preview.exec_()
                    
    def _pyVersion(self):
        return sys.version

class FormMain(QWidget, Ui_formMain):
    def __init__(self):
        QWidget.__init__(self)
        self.agent = PyAgent()
        
        self.setupUi(self)
        self.setWindowIcon(QIcon(':/images/ico/WebKit.png'))        
        
        self.webPage = WebPage()
        self.webView.setPage(self.webPage)        
        #self.webPage.settings().setAttribute(QWebSettings.PluginsEnabled, True)
        self.webPage.networkAccessManager().sslErrors.connect(self.onSslErrors)
        self.webPage.networkAccessManager().finished.connect(self.onfinished)
        self.webPage.setForwardUnsupportedContent(True)
        self.webPage.unsupportedContent.connect(self.download)

        self.dlmanager = QNetworkAccessManager()
        self.dlmanager.finished.connect(self.dlmanagerOnfinished)
        

    def onSslErrors(self, reply, errors):
        reply.ignoreSslErrors()
        print 'handleSslErrors'
        
    def onfinished(self):
        self.webPage.mainFrame().addToJavaScriptWindowObject('pyAgent', self.agent)        

    def download(self, reply):        
        self.request = reply.request()
        u = reply.url()
        h = u.host()
        if h!='':# 如果 href 連結為網址, 另用一個 manage dowload
            self.request.setUrl(u)
            self.reply = self.dlmanager.get(self.request)            
        else:# 如果 href 連結中為資料, 那就直接存檔
            f = self.webPage.currentFrame()
            e = f.findFirstElement('*:focus')
            path = e.attribute('download')
            self.replySaveFile(reply, path)
        

    def dlmanagerOnfinished(self):            
        path = os.path.expanduser(
            os.path.join('~',
                         unicode(self.reply.url().path()).split('/')[-1]))                                 
        self.replySaveFile(self.reply, path)
           
            
    def replySaveFile(self, reply, path):
        destination = unicode(QFileDialog.getSaveFileName(self, 'save', path))
        
        if destination:
            f = open(destination, 'wb')
            f.write(reply.readAll())
            f.flush()
            f.close()
        

