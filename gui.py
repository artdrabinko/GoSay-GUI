# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore 
import time
import threading
#import QPropertyAnimation

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
        self.setStyleSheet('background: #5181b8; border: none;')
        
        LayoutH = QtGui.QHBoxLayout()
        self.setLayout(LayoutH)
        
        #self.buttonBack.setStyleSheet('margin-bottom: 20px;')
        self.buttonBack = ButtonBackRegistrationWidget() 
        self.registrationLabel = QtGui.QLabel('Registration:')
        self.registrationLabel.setMaximumSize(240,30)
        self.registrationLabel.setMinimumSize(240,30)
        self.registrationLabel.setStyleSheet('padding-top:1px;border: none;font: Arial; font-size: 18px; background: #5181b8;color: #ffffff;')
        
        
        LayoutH.addWidget(self.buttonBack)
        LayoutH.addWidget(self.registrationLabel)
        
        

class ThreadDB(threading.Thread):
        def run(self):
            cout = 0
            print'............Thread was active................'
            while(True):
                print time.ctime()
                time.sleep(2)
                cout = cout + 1
                if(cout == 2):break
            print '...........Thread was stoped...............'  


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
        self.setEchoMode(QtGui.QLineEdit.Password)
        
    def focusOutEvent(self,event):
        self.setStyleSheet('background-color: #5181b8; color: #a8c0dc; margin : 0px;border: none; border-bottom: 1px solid #7ca0ca;')
        self.setEchoMode(QtGui.QLineEdit.Normal)
        self.setText('Password                                    Forgot?')
        

        
    def focusInEvent(self,event):
        self.clear()
        self.setStyleSheet('background-color: #5181b8; color: #a8c0dc; margin : 0px; border: none; border-bottom: 1.6px solid #edf2f8;')
   
     
class emtyBlockAfterEdit(QtGui.QLabel):
    def __init__(self, parent=None):
        QtGui.QLabel.__init__(self, parent) 
        self.setMinimumSize(100,0)
        self.setMaximumSize(100,0)

  
class buttonLogin0(QtGui.QLabel):
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


class ButtonRegistrationWidget(QtGui.QPushButton):
    def __init__(self, parent=None):
        QtGui.QPushButton.__init__(self, parent)  
        self.setMouseTracking(True)
        self.setMaximumSize(250,30)
        self.setMinimumSize(250,30)
        self.setStyleSheet(' color: #ffffff;border:none; ')
        self.setText('Registration')
        
    def mousePressEvent(self, event):
        self.setStyleSheet('background-color: #5f90c8; color: #ffffff; border: none;')
        
    def mouseReleaseEvent(self, event):
        self.setStyleSheet('background-color: #6698cf; color: #ffffff; border: none;')
        #print 'mouseReleaseEvent press'

    def enterEvent(self,event):
        self.setStyleSheet('background-color: #6e9cd0; color: #ffffff; border: none;')
        #print 'enterEvent press'
        
    def leaveEvent(self,event):
        self.setStyleSheet(' color: #ffffff; border: none;')
        #print 'leaveEvent press'










#.....................Build Application........................................

class MainAuthenticationWindow(QtGui.QWidget):
    
    def __init__(self,parent = None):
        QtGui.QWidget.__init__(self, parent)
        
        self.setWindowTitle('Authentication Window')
        self.setWindowIcon(QtGui.QIcon('connect.png'))
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        #first width second hight
        #290 460
        #410 460
        self.setMaximumSize(300,460)
        self.setMinimumSize(290,460)
        self.setStyleSheet('background-color: #5181b8; margin : 0px; padding: 0px;border-style: solid; border-color: #363333; border-width: 1px')
        
        class buttonLogin(buttonLogin0):
            def mousePressEvent(parent, event):
                print 'lolol'
                self.pressLoginAction()
        
        class ButtonRegistration(ButtonRegistrationWidget):
            def mousePressEvent(parent, event):
                print 'line 233'
                self.pressRegistrationAction()
        
        class ButtonBackRegistration(ButtonBackRegistrationWidget):  
            def mousePressEvent(parent, event):
                print'line 238'
                self.pressBackAction()
        
        
   
        class HeaderRegistration(HeaderRegistrationWidget):
            def __init__(self,parent = None):
                QtGui.QWidget.__init__(self, parent)
                self.setMaximumSize(270,40)
                self.setMinimumSize(270,40)
                LayoutH = QtGui.QHBoxLayout()
        
                self.setStyleSheet('background: #5181b8; border: none;')
                self.buttonBack = ButtonBackRegistration()
                #self.buttonBack.setStyleSheet('margin-bottom: 20px;')
                self.setLayout(LayoutH)
        
                
                self.registrationLabel = QtGui.QLabel('Registration:')
                self.registrationLabel.setMaximumSize(240,30)
                self.registrationLabel.setMinimumSize(240,30)
                self.registrationLabel.setStyleSheet('padding-top:1px;border: none;font: Arial; font-size: 18px; background: #5181b8;color: #ffffff;')
                
                
                LayoutH.addWidget(self.buttonBack)
                LayoutH.addWidget(self.registrationLabel)
                
                
                
                
                
                
                
        
        mainAuthenticationWindowLayout = QtGui.QHBoxLayout()
        self.setLayout(mainAuthenticationWindowLayout)
        
        

        layoutForWidgetAuthenticationWindow = QtGui.QVBoxLayout()
        mainAuthenticationWindowLayout.addLayout(layoutForWidgetAuthenticationWindow)
        
        
        
        layoutForWidgetRegestrationWindow = QtGui.QVBoxLayout()
        mainAuthenticationWindowLayout.addLayout(layoutForWidgetRegestrationWindow)
        
        
        
        
        #...................Start content Registration Form.............................
        
        self.RegistrationHeader = HeaderRegistration()
        #self.RegistrationHeader.setStyleSheet('background:#ffffff;')
        
        self.emptyLabel0 = QtGui.QLabel('      Registration Form')
        self.emptyLabel0.setStyleSheet('border:none; text-align:right;')        
        self.emptyLabel0.setMinimumSize(200, 420)
        self.emptyLabel0.setMaximumSize(200, 420)
        
        self.RegistrationHeader.setVisible(False)
        self.emptyLabel0.setVisible(False)
        
        layoutForWidgetRegestrationWindow.addWidget(self.RegistrationHeader)
        layoutForWidgetRegestrationWindow.addWidget(self.emptyLabel0)
        
        
        #...................End content Registration Form.............................
        
        
        
        
        
        
        
        
        #...................Start content authentification.............................
        
        #first width second hight
        self.logoWidget = logoWidget()
        
        self.inputLineForLoginUser = inputLineLogin()
        self.inputLineForPasswordUser = inputLinePassword()
        self.emtyBlockAfterEdit = emtyBlockAfterEdit()
        
        self.btnLogin = buttonLogin()
        self.emptyBlock = emptyBlock()
        
        self.btnRegistration = ButtonRegistration()
        

        layoutForWidgetAuthenticationWindow.addWidget(self.logoWidget)
        layoutForWidgetAuthenticationWindow.addWidget(self.inputLineForLoginUser)
        layoutForWidgetAuthenticationWindow.addWidget(self.inputLineForPasswordUser)
        layoutForWidgetAuthenticationWindow.addWidget(self.emtyBlockAfterEdit)
        layoutForWidgetAuthenticationWindow.addWidget(self.btnLogin)
        layoutForWidgetAuthenticationWindow.addWidget(self.emptyBlock)
        layoutForWidgetAuthenticationWindow.addWidget(self.btnRegistration)
        
        #...................End content authentification.............................
        
        
        
        
        
        
        
        
        #...................Start content Main User Form.............................
        
        MainUserWindow = QtGui.QHBoxLayout()
        mainAuthenticationWindowLayout.addLayout(MainUserWindow)
        
        
        leftLayoutMainuserWindow = QtGui.QVBoxLayout()
        MainUserWindow.addLayout(leftLayoutMainuserWindow)
        
        rightLayoutMainuserWindow = QtGui.QVBoxLayout()
        MainUserWindow.addLayout(rightLayoutMainuserWindow)
        
        
        self.leftWidget = logoLabelWidget()
        self.leftWidget.setMaximumSize(200,200)
        self.leftWidget.setMinimumSize(200,200)
        self.leftWidget.setStyleSheet('border:1px solid;')
        
        self.rightWidget = logoLabelWidget()
        self.rightWidget.setMaximumSize(200,200)
        self.rightWidget.setMinimumSize(200,200)
        self.rightWidget.setStyleSheet('border: 1px solid;')
        
        
        leftLayoutMainuserWindow.addWidget(self.leftWidget)
        rightLayoutMainuserWindow.addWidget(self.rightWidget)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #...................End content Main User Form.............................

        
       
    def closeEvent(self, event):
            reply = QtGui.QMessageBox.question(self, 'Message',"Are you sure to quit?", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

            if reply == QtGui.QMessageBox.Yes:
                main.setVisible(True)
                main.close()
            else:
                event.ignore()
                
                
    def pressRegistrationAction(self):
        print 'press ...........start pressRegistrationAction........'
        self.logoWidget.setVisible(False)
        self.inputLineForLoginUser.setVisible(False)
        self.inputLineForPasswordUser.setVisible(False)
        self.emtyBlockAfterEdit.setVisible(False)
        self.btnLogin.setVisible(False)
        self.emptyBlock.setVisible(False)
        self.btnRegistration.setVisible(False)
        
        
        self.RegistrationHeader.setVisible(True)
        self.emptyLabel0.setVisible(True)
        newThread = ThreadDB()
        newThread.start()
        self.setMinimumSize(290,460)
        self.setMaximumSize(600,460)
        self.resize(600,460)
        print 'press ...........end pressRegistrationAction...........'
        
 
    def pressBackAction(self):
        print 'press ...........start pressBackAction........'
        self.logoWidget.setVisible(True)
        self.inputLineForLoginUser.setVisible(True)
        self.inputLineForPasswordUser.setVisible(True)
        self.emtyBlockAfterEdit.setVisible(True)
        self.btnLogin.setVisible(True)
        self.emptyBlock.setVisible(True)
        self.btnRegistration.setVisible(False)
        
        
        self.RegistrationHeader.setVisible(False)
        self.emptyLabel0.setVisible(False)   
        newThread = ThreadDB()
        newThread.start()
        
        self.setMinimumSize(290,460)
        self.setMaximumSize(290,460)
        self.resize(290,460)
       # workPlace.show()
        print 'press ...........end pressBackAction...........'
        
        
    def pressLoginAction(self):
        print 'pressLoginAction'
        #self.setMinimumSize(290,460)
        #self.setMaximumSize(600,460)
        #self.resize(600,460)
        self.setMinimumSize(290,460)
        self.setMaximumSize(900,900)
        self.resize(900,700)
        
        self.logoWidget.setVisible(False)
        self.inputLineForLoginUser.setVisible(False)
        self.inputLineForPasswordUser.setVisible(False)
        self.emtyBlockAfterEdit.setVisible(False)
        self.btnLogin.setVisible(False)
        self.emptyBlock.setVisible(False)
        self.btnRegistration.setVisible(False)
        
        
        
        
        
        
        
        
    def press(self):
        print 'press 373'
        
#class workWindow(MainAuthenticationWindow):   
   # def __init__(self,parent):
       # self.setMinimumSize(400,400)
       # self.setWindowTitle('Main window')
       # qr = self.frameGeometry()
       # cp = QtGui.QDesktopWidget().availableGeometry().center()
       # qr.moveCenter(cp)
       # self.move(qr.topLeft())
       # self.setWindowIcon(QtGui.QIcon('gosay.png'))







#if __name__ == '__gui2.py__':
  
app = QtGui.QApplication(sys.argv)

main = MainAuthenticationWindow()

#workPlace = workWindow(main)

main.show() 

sys.exit(app.exec_())     
