# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore, Qt
import time
import threading
#import QPropertyAnimation

sys.path.insert(0,"/home/art/prgosay/actions/")
import action

statGui = False


class QTheThreadThatConnectToTheServer(threading.Thread):
    def run(self):
        print' '
        print'................Thread DB on................'
        time.sleep(2)
        print 'start ' + time.ctime()
        print' '
        stat = action.estabilishConnection()
        print stat
        print' '
        print 'stop '  + time.ctime()
        time.sleep(2)
        print '...............Thead DB was stoped.............'
        print' '
        return stat
        
	    
def QconnectToServerStart():
    newThread = QTheThreadThatConnectToTheServer()
    newThread.start()
    #return True, '......seans key.....'
    return 'Connect !'

def connectToServerStart():
    print' '
    print'................Thread DB on................'
    time.sleep(0.5)
    print 'start ' + time.ctime()
    print' '
    stat = action.estabilishConnection()
    print stat
    print' '
    print 'stop '  + time.ctime()
    time.sleep(0.5)
    print '...............Thead DB was stoped.............'
    print' '
    return stat


class VLayout(QtGui.QVBoxLayout):
     def __init__(self,parent = None):
        QtGui.QVBoxLayout.__init__(self, parent)
        self.setMargin(0)
        self.setSpacing(0)

class HLayout(QtGui.QHBoxLayout):
     def __init__(self,parent = None):
        QtGui.QHBoxLayout.__init__(self, parent)
        self.setMargin(0)
        self.setSpacing(0)
        
        
class ButtonBackRegistrationWidget(QtGui.QPushButton):
    def __init__(self,parent = None):
        QtGui.QPushButton.__init__(self, parent)
        self.setMaximumSize(40,40)
        self.setMinimumSize(40,40)
        icon = QtGui.QIcon('back_button.png')
        self.setIcon(icon)
        self.setIconSize(QtCore.QSize(30,40))
        self.setStyleSheet('background:#5181b8;')
        
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

class ButtonMenuWidget(QtGui.QPushButton):
    def __init__(self,parent = None):
        QtGui.QPushButton.__init__(self, parent)
        self.setMaximumSize(52,53)
        self.setMinimumSize(52,53)
        icon = QtGui.QIcon('menu.png')
        self.setIcon(icon)
        self.setIconSize(QtCore.QSize(40,40))
        self.setStyleSheet('background:#ffffff; border:none;')
        
    def mousePressEvent(self, event):
        icon = QtGui.QIcon('menu.png')
        self.setIcon(icon)
        self.setIconSize(QtCore.QSize(40,40))
        self.setStyleSheet('background: #ffffff; border:none;')
        self.setFocusPolicy(False)
        print'press 1'

    def mouseReleaseEvent(self, event):
        icon = QtGui.QIcon('menu_hover.png')
        self.setIcon(icon)
        self.setIconSize(QtCore.QSize(40,40))
        self.setStyleSheet('background: #ffffff; border:none;')
    
    def enterEvent(self,event):
        #self.setStyleSheet('background-color: #6e9cd0; color: #ffffff; border: none;')
        icon = QtGui.QIcon('menu_hover.png')
        self.setIcon(icon)
        self.setIconSize(QtCore.QSize(40,45))
        self.setStyleSheet('background: #ffffff; border:none;')
        #print 'enterEvent press'
        
    def leaveEvent(self,event):
        icon = QtGui.QIcon('menu.png')
        self.setIcon(icon)
        self.setIconSize(QtCore.QSize(40,40))
        self.setStyleSheet('background:#ffffff; border:none;')
        #self.setStyleSheet('background-color: #6696cc; color: #ffffff; border: none;')
      
      
      
      
      
      
      
class inputSearchWidget(QtGui.QLineEdit):
    def __init__(self, parent=None):
        QtGui.QLineEdit.__init__(self, parent)  
        self.setMouseTracking(True)
        self.setMaximumSize(220,33)
        self.setMinimumSize(229,33)
        self.setStyleSheet('background-color: #f1f1f3; margin-right: 50px; color: #b4a3b3; border: none; border-radius: 5px;')
        self.setText('Search')
        #self.setFocusPolicy(True)







        

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
                #time.sleep(2)
                cout = cout + 1
                if(cout == 2):break
            print '...........Thread was stoped...............'  


class logoLabelWidget(QtGui.QLabel):
    def __init__(self, parent=None):
        QtGui.QLabel.__init__(self, parent)
        self.setMaximumSize(165,70)
        self.setMinimumSize(165,70)
        self.setText("GoSay")
        self.setStyleSheet('background-color: #5181b8; color : #edf2f8; font: bold  Arial; font-size: 46px;')


class logoWidget(QtGui.QLabel):
    def __init__(self, parent=None):
        QtGui.QLabel.__init__(self, parent)
        self.setMaximumSize(290,120)
        self.setMinimumSize(250,120)
        self.setStyleSheet('background-color: #5181b8;')
        logoLayout = HLayout()
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
        self.setContentsMargins(0,0,0,0)
        #first width second hight
        #290 460
        #410 460
        self.setMaximumSize(300,460)
        self.setMinimumSize(290,460)
        self.setStyleSheet('background-color: #5181b8; border-style: solid; border-color: #363333; border-width: 1px')
        
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
                self.setMaximumSize(290,40)
                self.setMinimumSize(290,40)
                LayoutH = QtGui.QHBoxLayout()
                LayoutH.setMargin(0)
                self.setStyleSheet('background: #5181b8;')
                self.buttonBack = ButtonBackRegistration()
                #self.buttonBack.setStyleSheet('margin-bottom: 20px;')
                self.setLayout(LayoutH)
        
                
                self.registrationLabel = QtGui.QLabel('Registration:')
                self.registrationLabel.setMaximumSize(240,40)
                self.registrationLabel.setMinimumSize(240,40)
                self.registrationLabel.setStyleSheet('padding-top:1px;font: Arial; font-size: 18px; background: #5181b8;color: #ffffff;')
                
                
                LayoutH.addWidget(self.buttonBack)
                LayoutH.addWidget(self.registrationLabel)
                
                
                
                
                
                
                
        
        mainAuthenticationWindowLayout = HLayout()
        self.setLayout(mainAuthenticationWindowLayout)
        
        

        layoutForWidgetAuthenticationWindow = VLayout()
        mainAuthenticationWindowLayout.addLayout(layoutForWidgetAuthenticationWindow)
        
        
        
        layoutForWidgetRegestrationWindow = VLayout()
        mainAuthenticationWindowLayout.addLayout(layoutForWidgetRegestrationWindow)
        
        
        
        
        #...................Start content Registration Form.............................
        
        self.RegistrationHeader = HeaderRegistration()
        self.RegistrationHeader.setContentsMargins(0,0,0,0)
        self.RegistrationHeader.setStyleSheet('border:1px solid;')
        #self.RegistrationHeader.setStyleSheet('background:#ffffff;')
        
        self.emptyLabel0 = QtGui.QLabel('      Registration Form')
        self.emptyLabel0.setStyleSheet(' text-align:right;')        
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
        
        MainUserWindow = HLayout()
        mainAuthenticationWindowLayout.addLayout(MainUserWindow)
        
        
        leftLayoutMainuserWindow = VLayout()
        MainUserWindow.addLayout(leftLayoutMainuserWindow)
        
        rightLayoutMainuserWindow = VLayout()
        MainUserWindow.addLayout(rightLayoutMainuserWindow)
        
        
        self.leftWidget = logoLabelWidget()
        self.leftWidget.setMinimumSize(260,460)
        self.leftWidget.setMaximumSize(290,900)
        self.leftWidget.setStyleSheet('border:1px solid; background: #ffffff; border: none;')
        self.leftWidget.setMargin(0)
        self.leftWidget.setVisible(False)
        
        self.rightWidget = logoLabelWidget()
        self.rightWidget.setMinimumSize(400,460)
        self.rightWidget.setMaximumSize(520,900)
        self.rightWidget.setStyleSheet('background: #ffffff; border: none;border-left: 1px solid #cacfd2;')
        self.rightWidget.setMargin(0)
        self.rightWidget.setVisible(False)
        
        
        
        
        #...................Start content self.leftWidget.............................
        leftWidgetlayout = VLayout()
        
        self.leftWidget.setLayout(leftWidgetlayout)
        self.leftWidget.setMargin(0)
        self.leftWidget.setContentsMargins(0,0,0,0)
        
        
        self.leftHeader = QtGui.QWidget()
        layoutForWidgetsLeftHeader = HLayout()

        self.leftHeader.setLayout(layoutForWidgetsLeftHeader)
        self.leftHeader.setMinimumSize(260,55)
        self.leftHeader.setMaximumSize(290,55)
        self.leftHeader.setStyleSheet('border: none; border-bottom: 1px solid #cacfd2;')
        
        self.buttonMenu = ButtonMenuWidget()
        self.inputSearch = inputSearchWidget()
        layoutForWidgetsLeftHeader.addWidget(self.buttonMenu)
        layoutForWidgetsLeftHeader.addWidget(self.inputSearch)
        
        
        
        
        self.leftArea = QtGui.QScrollArea()
        self.leftArea.setWidgetResizable(True)
        self.leftArea.setMinimumSize(260,404)
        self.leftArea.setMaximumSize(290,500)
        self.leftArea.setStyleSheet('border: none;')
        self.leftArea.setContentsMargins(0,0,0,0)
        
        self.boxwid = QtGui.QWidget()
        self.leftArea.setWidget(self.boxwid)
        self.layoutForleftArea = VLayout()        
        self.boxwid.setLayout(self.layoutForleftArea)
        
        
        self.Friend = QtGui.QLabel('   Friend\n   You: Hi!')
        self.Friend.setMinimumSize(260,62)
        self.Friend.setMaximumSize(290,62)
        self.Friend.setStyleSheet('background: #419fd9; color: #ffffff; border: none;')
        
        self.Friend1 = QtGui.QLabel('   Friend\n   You: Hi!')
        self.Friend1.setMinimumSize(260,62)
        self.Friend1.setMaximumSize(290,62)
        self.Friend1.setStyleSheet('background: #f1f1f1; color: #857f7b; border: none; border-bottom: 1px solid #cacfd2')
        
        self.Friend2 = QtGui.QLabel('   Friend\n   You: Hi!')
        self.Friend2.setMinimumSize(260,62)
        self.Friend2.setMaximumSize(290,62)
        self.Friend2.setStyleSheet('background: #f1f1f1; color: #857f7b; border: none; border-bottom: 1px solid #cacfd2')
        
        self.Friend3 = QtGui.QLabel('   Friend\n   You: Hi!')
        self.Friend3.setMinimumSize(260,62)
        self.Friend3.setMaximumSize(290,62)
        self.Friend3.setStyleSheet('background: #f1f1f1; color: #857f7b; border: none; border-bottom: 1px solid #cacfd2')
        
        self.Friend4 = QtGui.QLabel('   Friend\n   You: Hi!')
        self.Friend4.setMinimumSize(260,62)
        self.Friend4.setMaximumSize(290,62)
        self.Friend4.setStyleSheet('background: #ffffff; color: #857f7b; border: none; border-bottom: 1px solid #cacfd2')
        
        self.Friend5 = QtGui.QLabel('   Friend\n   You: Hi!')
        self.Friend5.setMinimumSize(260,62)
        self.Friend5.setMaximumSize(290,62)
        self.Friend5.setStyleSheet('background: #f1f1f1; color: #857f7b; border: none; border-bottom: 1px solid #cacfd2')
        
        self.Friend6 = QtGui.QLabel('   Friend\n   You: Hi!')
        self.Friend6.setMinimumSize(260,62)
        self.Friend6.setMaximumSize(290,62)
        self.Friend6.setStyleSheet('background: #f1f1f1; color: #857f7b; border: none; border-bottom: 1px solid #cacfd2')
        


        
        
        self.layoutForleftArea.addWidget(self.Friend)
        self.layoutForleftArea.addWidget(self.Friend1)
        self.layoutForleftArea.addWidget(self.Friend2)
        self.layoutForleftArea.addWidget(self.Friend3)
        self.layoutForleftArea.addWidget(self.Friend4)
        self.layoutForleftArea.addWidget(self.Friend5)
        self.layoutForleftArea.addWidget(self.Friend6)
        
        
        leftWidgetlayout.addWidget(self.leftHeader)
        leftWidgetlayout.addWidget(self.leftArea)
        #leftWidgetlayout.setAlignment(Qt.)
        
        
        #...................End content self.leftWidget.............................
        
        
        
        
        
        
        
        
        leftLayoutMainuserWindow.addWidget(self.leftWidget)
        rightLayoutMainuserWindow.addWidget(self.rightWidget)
        
        
        
    def lisenS(self):
        print '.........time'
        #time.sleep(3)
        self.rightWidget.setStyleSheet('border:3px solid;')
        self.setMinimumSize(630,460)
        self.setMaximumSize(700,800)
        #stat = action.estabilishConnection()
        print 'llll'
        self.resize(600,500)
        print '.........time'
        
        
        #...................End content Main User Form.............................





        #...................Start content Main User Form.............................
        
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
        self.resize(290,460)
        print 'press ...........end pressRegistrationAction...........'
        
 
    def pressBackAction(self):
        print 'press ...........start pressBackAction........'
        self.logoWidget.setVisible(True)
        self.inputLineForLoginUser.setVisible(True)
        self.inputLineForPasswordUser.setVisible(True)
        self.emtyBlockAfterEdit.setVisible(True)
        self.btnLogin.setVisible(True)
        self.emptyBlock.setVisible(True)
        self.btnRegistration.setVisible(True)
        
        
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
        r = MainAuthenticationWindow(self)
        t1 = threading.Thread(target= r.lisenS(), args=())
        t1.start()
        statGui = action.estabilishConnection()
    
        # init threads
        
        
        self.Friend13 = QtGui.QLabel('   Friend\n   You: Hi!')
        self.Friend13.setMinimumSize(260,62)
        self.Friend13.setMaximumSize(290,62)
        self.Friend13.setStyleSheet('background: #f1f1f1; color: #857f7b; border: none; border-bottom: 1px solid #cacfd2')
        
        self.Friend23 = QtGui.QLabel('   Friend\n   You: Hi!')
        self.Friend23.setMinimumSize(260,62)
        self.Friend23.setMaximumSize(290,62)
        self.Friend23.setStyleSheet('background: #f1f1f1; color: #857f7b; border: none; border-bottom: 1px solid #cacfd2')
        
        self.Friend33 = QtGui.QLabel('   Friend\n   You: Hi!')
        self.Friend33.setMinimumSize(260,62)
        self.Friend33.setMaximumSize(290,62)
        self.Friend33.setStyleSheet('background: #f1f1f1; color: #857f7b; border: none; border-bottom: 1px solid #cacfd2')
        
        self.Friend43 = QtGui.QLabel('   Friend\n   You: Hi!')
        self.Friend43.setMinimumSize(260,62)
        self.Friend43.setMaximumSize(290,62)
        self.Friend43.setStyleSheet('background: #ffffff; color: #857f7b; border: none; border-bottom: 1px solid #cacfd2')
        
        self.Friend53 = QtGui.QLabel('   Friend\n   You: Hi!')
        self.Friend53.setMinimumSize(260,62)
        self.Friend53.setMaximumSize(290,62)
        self.Friend53.setStyleSheet('background: #f1f1f1; color: #857f7b; border: none; border-bottom: 1px solid #cacfd2')
        
        self.Friend63 = QtGui.QLabel('   Friend\n   You: Hi!')
        self.Friend63.setMinimumSize(260,62)
        self.Friend63.setMaximumSize(290,62)
        self.Friend63.setStyleSheet('background: #f1f1f1; color: #857f7b; border: none; border-bottom: 1px solid #cacfd2')
        
        
        self.layoutForleftArea.addWidget(self.Friend13)
        self.layoutForleftArea.addWidget(self.Friend23)
        self.layoutForleftArea.addWidget(self.Friend33)
        self.layoutForleftArea.addWidget(self.Friend43)
        self.layoutForleftArea.addWidget(self.Friend53)
        self.layoutForleftArea.addWidget(self.Friend63)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #self.setMinimumSize(290,460)
        #self.setMaximumSize(600,460)
        #self.resize(600,460)
        if(statGui):
            print 'True login'
            self.setMinimumSize(500,460)
            self.setMaximumSize(810,900)
            self.resize(920,460)
           

            self.logoWidget.setVisible(False)
            self.inputLineForLoginUser.setVisible(False)
            self.inputLineForPasswordUser.setVisible(False)
            self.emtyBlockAfterEdit.setVisible(False)
            self.btnLogin.setVisible(False)
            self.emptyBlock.setVisible(False)
            self.btnRegistration.setVisible(False)
            
            
            self.leftWidget.setVisible(statGui)
            self.leftWidget.setText(str(statGui))
        
            self.rightWidget.setVisible(True)
            #self.leftWidget.setVisible(False)
        #t1.join()
        else:
            print 'False login'
            self.logoWidget.setVisible(False)
        
        
        
        
        
        
        
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

