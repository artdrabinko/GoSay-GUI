# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore


class ButtonBackRegistrationWidget(QtGui.QPushButton):
    def __init__(self,parent = None):
        QtGui.QPushButton.__init__(self, parent)
        self.setMaximumSize(40,30)
        self.setMinimumSize(40,30)
        icon = QtGui.QIcon('back_button.png')
        self.setIcon(icon)
        self.setIconSize(QtCore.QSize(30,40))
        self.setStyleSheet('background:#5181b8; border:none;')
        
    def mousePressEvent(self, event):
        icons = QtGui.QIcon('button_back_hover.png')
        self.setIcon(icons)
        self.setIconSize(QtCore.QSize(40,40))
        self.setStyleSheet('background:#5181b8;')
        print'press 1'

    def mouseReleaseEvent(self, event):
        icons = QtGui.QIcon('button_back_hover.png')
        self.setIcon(icons)
        self.setIconSize(QtCore.QSize(45,45))
        self.setStyleSheet('background:#5181b8;')
    
    def enterEvent(self,event):
        #self.setStyleSheet('background-color: #6e9cd0; color: #ffffff; border: none;')
        icons = QtGui.QIcon('button_back_hover.png')
        self.setIcon(icons)
        self.setIconSize(QtCore.QSize(45,45))
        self.setStyleSheet('background:#5181b8;')
        #print 'enterEvent press'
        
    def leaveEvent(self,event):
        icon = QtGui.QIcon('back_button.png')
        self.setIcon(icon)
        self.setIconSize(QtCore.QSize(30,40))
        self.setStyleSheet('background:#5181b8;')
        #self.setStyleSheet('background-color: #6696cc; color: #ffffff; border: none;')
        
        
        

class HeaderRegistrationWidget(QtGui.QLabel):
    def __init__(self,parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.setMaximumSize(270,40)
        self.setMinimumSize(270,40)
        LayoutH = QtGui.QHBoxLayout()

        self.setStyleSheet('background: #5181b8; border: none;')
        self.buttonBack = ButtonBackRegistrationWidget()
        self.buttonBack.move(0,0) 
        #self.buttonBack.setStyleSheet('margin-bottom: 20px;')
        self.setLayout(LayoutH)

        
        self.registrationLabel = QtGui.QLabel('Registration:')
        self.registrationLabel.setMaximumSize(240,30)
        self.registrationLabel.setMinimumSize(240,30)
        self.registrationLabel.setStyleSheet('padding-top:1px;border: none;font: Arial; font-size: 18px; background: #5181b8;color: #ffffff;')
        
        
        LayoutH.addWidget(self.buttonBack)
        LayoutH.addWidget(self.registrationLabel)
        
        

    


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


class buttonRegistration(QtGui.QPushButton):
    def __init__(self, parent=None):
        QtGui.QPushButton.__init__(self, parent)  
        self.setMouseTracking(True)
        self.setMaximumSize(250,30)
        self.setMinimumSize(250,30)
        self.setStyleSheet(' color: #ffffff;border:none; ')
        self.setText('Registration')
        
    def mousePressEvent(self, event):
        self.setStyleSheet('background-color: #5f90c8; color: #ffffff; border: none;')
        #self.mai = RegistrationWindow()
        print'press 1'
        #self.mai.show()        
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
        
        
        layoutForWidgetRegestrationWindow = QtGui.QVBoxLayout()
        mainAuthenticationWindowLayout.addLayout(layoutForWidgetRegestrationWindow)
        self.RegistrationHeader = HeaderRegistrationWidget()
        self.RegistrationHeader.setVisible(False)
        #self.RegistrationHeader.setStyleSheet('background:#ffffff;')
        
        self.lab = QtGui.QLabel('           Registration Form:')
        self.lab.setStyleSheet('border:none;')
        self.lab.setVisible(False)
        self.lab.setMinimumSize(200, 420)
        self.lab.setMaximumSize(200, 420)
        
        
        layoutForWidgetRegestrationWindow.addWidget(self.RegistrationHeader)
        layoutForWidgetRegestrationWindow.addWidget(self.lab)
        
        
        #first width second hight
        self.logoWidget = logoWidget()
        self.inputLineForLoginUser = inputLineLogin()
        self.inputLineForPasswordUser = inputLinePassword()
        self.emtyBlockAfterEdit = emtyBlockAfterEdit()
        self.btnLogin = buttonLogin()
        #self.btnRegistration = buttonRegistration()
        self.emptyBlock = emptyBlock()
        #self.btnRegistration = QtGui.QPushButton("Registration")
        
        class buttonRegistration(QtGui.QPushButton):
            def __init__(self, parent=None):
                QtGui.QPushButton.__init__(self, parent)  
                self.setMouseTracking(True)
                self.setMaximumSize(250,30)
                self.setMinimumSize(250,30)
                self.setStyleSheet(' color: #ffffff;border:none; ')
                self.setText('Registration')
                
            def mouseReleaseEvent(self, event):
                self.setStyleSheet('background-color: #6698cf; color: #ffffff; border: none;')
      
            def enterEvent(self,event):
                self.setStyleSheet('background-color: #6e9cd0; color: #ffffff; border: none;')

            def leaveEvent(self,event):
                self.setStyleSheet('background-color: #6696cc; color: #ffffff; border: none;')

            def mousePressEvent(parent, event):
                #self.mai = RegistrationWindow()  
                #self.mai.show()                   
                self.logoWidget.setVisible(False)
            
                print'press 2'
                self.press()
                self.inputLineForLoginUser.setVisible(False)
                self.inputLineForPasswordUser.setVisible(False)
                self.emtyBlockAfterEdit.setVisible(False)
                self.btnLogin.setVisible(False)
                self.emptyBlock.setVisible(False)
                
                self.btnRegistration.setVisible(False)
                self.RegistrationHeader.setVisible(True)
                self.lab.setVisible(True)
                    
        self.btnRegistration = buttonRegistration()
        

        layoutForWidgetAuthenticationWindow.addWidget(self.logoWidget)
        layoutForWidgetAuthenticationWindow.addWidget(self.inputLineForLoginUser)
        layoutForWidgetAuthenticationWindow.addWidget(self.inputLineForPasswordUser)
        layoutForWidgetAuthenticationWindow.addWidget(self.emtyBlockAfterEdit)
        layoutForWidgetAuthenticationWindow.addWidget(self.btnLogin)
        layoutForWidgetAuthenticationWindow.addWidget(self.emptyBlock)
        layoutForWidgetAuthenticationWindow.addWidget(self.btnRegistration)
        
         
                
        self.setLayout(mainAuthenticationWindowLayout)
        self.connect(self.btnRegistration, QtCore.SIGNAL('clicked()'), self.press)
        
    def closeEvent(self, event):
            reply = QtGui.QMessageBox.question(self, 'Message',"Are you sure to quit?", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

            if reply == QtGui.QMessageBox.Yes:
                main.setVisible(True)
                main.close()
            else:
                event.ignore()
        
    def press(self):
        print 'press 3'




#if __name__ == '__gui2.py__':
  
app = QtGui.QApplication(sys.argv)

main = MainAuthenticationWindow()
main.show() 

sys.exit(app.exec_())
