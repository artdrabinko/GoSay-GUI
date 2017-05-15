# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore


class logoLabelWidget(QtGui.QLabel):
    def __init__(self, parent=None):
        QtGui.QLabel.__init__(self, parent)
        self.setMaximumSize(140,70)
        self.setMinimumSize(140,70)
        self.setText("GoSay")
        self.setStyleSheet('background-color: #5181b8; border: none; color : #edf2f8; font: bold  Arial; font-size: 46px;')
        

class logoWidget(QtGui.QLabel):
    def __init__(self, parent=None):
        QtGui.QLabel.__init__(self, parent)
        self.setMaximumSize(250,120)
        self.setMinimumSize(250,120)
        self.setStyleSheet('background-color: #5181b8;border: none;')
        logoLayout = QtGui.QHBoxLayout()
        self.setLayout(logoLayout)
        self.logoLabel = logoLabelWidget()
        logoLayout.addWidget(self.logoLabel) 
    

class inputLineLogin(QtGui.QLineEdit):
    def __init__(self, parent=None):
        QtGui.QLineEdit.__init__(self, parent)  
        self.setMouseTracking(True)
        self.setMaximumSize(250,30)
        self.setMinimumSize(250,30)
        self.setStyleSheet('background-color: #5181b8; color: #a8c0dc; margin : 0px; border: none; border-bottom: 1px solid #7ca0ca;')
        self.setText('Login or phone')
        
    def mousePressEvent(self, event):
        #self.clear()
        print 'mouse press'
        
    def focusOutEvent(self,event):
        self.setStyleSheet('background-color: #5181b8; color: #a8c0dc; margin : 0px;border: none; border-bottom: 1px solid #7ca0ca;')
        self.setText('Login or phone')

        
    def focusInEvent(self,event):
        self.clear()
        self.setStyleSheet('background-color: #5181b8; color: #a8c0dc; margin : 0px; border: none; border-bottom: 1.6px  solid #edf2f8;')
        

class inputLinePassword(QtGui.QLineEdit):
    def __init__(self, parent=None):
        QtGui.QLineEdit.__init__(self, parent)  
        self.setMouseTracking(True)
        self.setMaximumSize(250,40)
        self.setMinimumSize(250,40)
        self.setStyleSheet('background-color: #5181b8; color: #a8c0dc; border: none; border-bottom: 1px solid #7ca0ca;')
        self.setText('Password                                    Forgot?')
        
    def mousePressEvent(self, event):
        #self.clear()
        print 'mouse press'
        
    def focusOutEvent(self,event):
        self.setStyleSheet('background-color: #5181b8; color: #a8c0dc; margin : 0px;border: none; border-bottom: 1px solid #7ca0ca;')
        self.setText('Password                                    Forgot?')

        
    def focusInEvent(self,event):
        self.clear()
        self.setStyleSheet('background-color: #5181b8; color: #a8c0dc; margin : 0px; border: none; border-bottom: 1.6px solid #edf2f8;')
        
class emtyBlockAfterEdit(QtGui.QLabel):
    def __init__(self, parent=None):
        QtGui.QLabel.__init__(self, parent) 
        self.setMinimumSize(100,0)
        self.setMaximumSize(100,0)
        

  
class buttonLogin(QtGui.QLabel):
    def __init__(self, parent=None):
        QtGui.QLabel.__init__(self, parent)  
        self.setMouseTracking(True)
        self.setMaximumSize(250,38)
        self.setMinimumSize(250,38)
        self.setStyleSheet('background-color: #6696cc; color: #ffffff; border: none;')
        self.setText('                              Login')
        
    def mousePressEvent(self, event):
        self.setStyleSheet('background-color: #5f90c8; color: #ffffff; border: none;')
        #print 'mousePressEvent press'
        
    def mouseReleaseEvent(self, event):
        self.setStyleSheet('background-color: #6698cf; color: #ffffff; border: none;')
        #print 'mouseReleaseEvent press'

    def enterEvent(self,event):
        self.setStyleSheet('background-color: #6e9cd0; color: #ffffff; border: none;')
        #print 'enterEvent press'
        
    def leaveEvent(self,event):
        self.setStyleSheet('background-color: #6696cc; color: #ffffff; border: none;')
        #print 'leaveEvent press'

class emptyBlock(QtGui.QLabel):
    def __init__(self, parent=None):
        QtGui.QLabel.__init__(self, parent)  
        self.setMouseTracking(True)
        self.setMaximumSize(250,85)
        self.setMinimumSize(250,85)
        self.setStyleSheet('border: solid;')

class buttonRegistration(QtGui.QLabel):
    def __init__(self, parent=None):
        QtGui.QLabel.__init__(self, parent)  
        self.setMouseTracking(True)
        self.setMaximumSize(250,30)
        self.setMinimumSize(250,30)
        self.setStyleSheet(' color: #ffffff;border:none; ')
        self.setText('                        Registration')
        
    def mousePressEvent(self, event):
        self.setStyleSheet('background-color: #5f90c8; color: #ffffff; border: none;')
        #print 'mousePressEvent press'
        
    def mouseReleaseEvent(self, event):
        self.setStyleSheet('background-color: #6698cf; color: #ffffff; border: none;')
        #print 'mouseReleaseEvent press'

    def enterEvent(self,event):
        self.setStyleSheet('background-color: #6e9cd0; color: #ffffff; border: none;')
        #print 'enterEvent press'
        
    def leaveEvent(self,event):
        self.setStyleSheet('background-color: #6696cc; color: #ffffff; border: none;')
        #print 'leaveEvent press'





class MainAuthenticationWindow(QtGui.QWidget):
    
    def __init__(self,parent = None):
        QtGui.QWidget.__init__(self, parent)
        
        self.setWindowTitle('Authentication Window')
        self.setWindowIcon(QtGui.QIcon('connect.png'))
        #first width second hight
        #290 460
        #410 460
        self.setMaximumSize(300,460)
        self.setMinimumSize(290,460)
        self.setStyleSheet('background-color: #5181b8; margin : 0px; padding: 0px;border-style: solid; border-color: #363333; border-width: 1px')
        
        
        mainAuthenticationWindowLayout = QtGui.QHBoxLayout()
        layoutForWidgetAuthenticationWindow = QtGui.QVBoxLayout()
        
        mainAuthenticationWindowLayout.addLayout(layoutForWidgetAuthenticationWindow)
        
        
        #first width second hight
        self.logoWidget = logoWidget()
        self.inputLineForLoginUser = inputLineLogin()
        self.inputLineForPasswordUser = inputLinePassword()
        self.emtyBlockAfterEdit = emtyBlockAfterEdit()
        self.btnLogin = buttonLogin()
        self.btnRegistration = buttonRegistration()
        self.emptyBlock = emptyBlock()
        

        layoutForWidgetAuthenticationWindow.addWidget(self.logoWidget)
        layoutForWidgetAuthenticationWindow.addWidget(self.inputLineForLoginUser)
        layoutForWidgetAuthenticationWindow.addWidget(self.inputLineForPasswordUser)
        layoutForWidgetAuthenticationWindow.addWidget(self.emtyBlockAfterEdit)
        layoutForWidgetAuthenticationWindow.addWidget(self.btnLogin)
        layoutForWidgetAuthenticationWindow.addWidget(self.emptyBlock)
        layoutForWidgetAuthenticationWindow.addWidget(self.btnRegistration)
        
        
        
        self.setLayout(mainAuthenticationWindowLayout)


app = QtGui.QApplication(sys.argv)

main = MainAuthenticationWindow()
main.show() 

sys.exit(app.exec_())     

