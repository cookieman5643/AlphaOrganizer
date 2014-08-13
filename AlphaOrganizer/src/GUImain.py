'''
Created on Jul 2, 2014

@author: cookieman
'''


import sys
from PyQt4 import QtGui, QtCore
#from FileExplorer import FileExplorer
#from FileExplorer2 import FileExplorer2
from FileExplorer3 import FileExplorerTmp
from Security import Security

######################### - Class Definition
class GUImain(QtGui.QWidget):
    def __init__(self):
         super(GUImain, self).__init__()
         ### - Sets up UI, Layout, etc.
         
         
         self.security = Security()
         if(self.security.initChecks()):
            self.initUI()
        
        
    def initUI(self):
        #Set-up Window
        self.uiWindow()
        
        #Set-up Frames
        self.uiInterface()
        
        #Show App
        self.uiShow()


    ##### - Window Layout Set-up
    def uiWindow(self):
        ### - Tool tip Properties
        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
        self.setToolTip('This is the main GUI.')
        
        ### - Sizing
        self.resize(1200,800)
        self.move(50,100)
        
        ### - Window Properties
        self.setWindowTitle("Alpha..")
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        
    ##### - Interface Layout, Set-up and Management
    def uiInterface(self):
        #Choose Layout Style
        USE_LAYOUT = 1        
        LAYOUT_FULL = 1
        LAYOUT_TEST = 2
        
        if(USE_LAYOUT == LAYOUT_FULL):
            ''' Make Items:
                 - Widget: menuBar
                 - Layout: bodyLayout
                 - Widget: statusBar    '''
            self.menuBar = QtGui.QMenuBar()
            self.uiBody()
            self.statusBar = QtGui.QStatusBar()
            
            #MAIN LAYOUT HOLDER
            self.mainLayout = QtGui.QVBoxLayout()
            self.mainLayout.setMargin(0) #rids ugly border
            
            #Add Widgets into layout
            self.mainLayout.addWidget(self.menuBar)
            self.mainLayout.addLayout(self.bodyLayout,1)
            self.mainLayout.addWidget(self.statusBar)
            
            #Set Applications Layout to Interface
            self.setLayout(self.mainLayout)
            self.uiStatusBarMsg("Application Layout Set")
            
        if(USE_LAYOUT == LAYOUT_TEST):
            pass
            
    ##### - Body Component of the UI
    def uiBody(self):
        #Make Main Body Layout: bodyLayout
        self.bodyLayout = QtGui.QHBoxLayout()
        
        #Make Frames:
        self.uiLeft() # creates: leftFrame
        self.uiCenter() # creates: centerFrame
        self.uiRight() # creates: rightFrame
        
        #Add Frames to Body
        self.bodyLayout.addWidget(self.leftFrame)
        self.bodyLayout.addWidget(self.centerFrame)
        self.bodyLayout.addWidget(self.rightFrame)
        
        pass     
        
    ##### - Set up Left Body UI
    def uiLeft(self):
        self.leftFrame = QtGui.QFrame()
        self.leftFrame.setMaximumWidth(400)
        self.leftFrame.setMinimumWidth(100)
        self.leftFrame.setToolTip('This Left Frame.')
        
        self.leftLayout = QtGui.QVBoxLayout()
        self.leftFrame.setLayout(self.leftLayout)
        
        self.fileExplorer = FileExplorerTmp()
        self.leftLayout.addWidget(self.fileExplorer)
        
    ##### - Set up Center Body UI
    def uiCenter(self):
        self.centerFrame = QtGui.QFrame()
        self.centerFrame.setMinimumWidth(500)
        self.centerFrame.setMaximumWidth(1000)
        self.centerFrame.setToolTip("This Center Frame.")
        
        self.centerLayout = QtGui.QVBoxLayout()
        self.centerFrame.setLayout(self.centerLayout)
        
        btn = QtGui.QPushButton("CenterFrame")
        self.centerLayout.addWidget(btn)
        
        
        
    ##### - Set up Right Body UI
    def uiRight(self):
        self.rightFrame = QtGui.QFrame()
        self.rightFrame.setMaximumWidth(500)
        self.rightFrame.setMinimumWidth(50)
        self.rightFrame.setToolTip('This Right Frame.')
        
        
    ##### - Set UI status bar
    def uiStatusBarMsg(self, msg):
        self.statusBar.showMessage(msg)

    ##### - Show window
    def uiShow(self):
        self.show()
        
        
    ##### - before window closes
    def closeEvent(self, event):
        print("Application Close.")
        self.security.reEncryptPasswordFile()
        print("Password File Re-encrypted.")
        event.accept()


######################### - Main Call
def main():
    app = QtGui.QApplication(sys.argv)
    layout = GUImain()
    sys.exit(app.exec_())
    


if __name__ == '__main__':
    main()
    