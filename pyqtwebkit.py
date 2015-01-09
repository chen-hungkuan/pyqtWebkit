# -*- coding: utf-8 -*-
"""
Created on Mon Nov 03 10:48:52 2014

@author: pedro
"""

import sys, re
import resources
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtNetwork import QNetworkAccessManager, QNetworkRequest
from formMain import FormMain

def main():
    app = QApplication(sys.argv)
    win = FormMain()
    url, user, pw, t, w, h = '', '', '', 'webkit', '', ''
    args = ' '.join(sys.argv)
    print args
    #取得 url 參數
    g = re.match('.*(-u) ([^-]\S+)', args)
    if not (g is None):
        url = g.group(2)
        print url
    #取得 username 參數
    g = re.match('.*(-n) ([^-]\S+)', args)
    if not (g is None):
        user = g.group(2)
        print user
    #取得 password 參數
    g = re.match('.*(-p) ([^-]\S+)', args)
    if not (g is None):
        pw = g.group(2)
    #取得 width 參數
    g = re.match('.*(-t) ([^-]\S+)', args)
    if not (g is None):
        t = g.group(2).decode('big5')
    #取得 width 參數
    g = re.match('.*(-w) ([^-]\S+)', args)
    if not (g is None):
        w = g.group(2)
    #取得 height 參數
    g = re.match('.*(-h) ([^-]\S+)', args)
    if not (g is None):
        h = g.group(2)

    request = QNetworkRequest(QUrl(url))
    postdata = QByteArray()
    if user != '':
        postdata.append('username=%s' % user)
    if pw != '':
        postdata.append('&password=%s' % pw)
    if url != '':
        #win.webView.load(request)
        #win.webView.load(request, QNetworkAccessManager.PostOperation, postdata)
        win.webPage.mainFrame().load(request, QNetworkAccessManager.PostOperation, postdata)
    win.setWindowTitle(t)
    if (w != '') & (h != ''):
        win.resize(int(w), int(h))
        win.show()
    else:
        win.showMaximized()
    sys.exit(app.exec_())
    
if __name__=='__main__':
    main()