'''
Created Jul 8, 2014

@author: cookieman
'''

#RE-write of my first File Explorer

#IMPORTS
import sys, os
from PyQt4 import QtGui, QtCore

#CLASS DEFINITION
class FileExplorer2(QtGui.QVBoxLayout):
    
    def __init__(self):
        super(FileExplorer2, self).__init__()
        self.setPath()
        self.initUI()
        
    #Temporary working with this set of directories
    def setPath(self):
        self.CURRENT_PATH = '/home/cookieman/Dropbox/Files_x/Alpha'
    
    #Make the Initial UI - Try using a QTreeView
    def initUI(self):
        #Add a simple button just to find object
        self.button = QtGui.QPushButton("Push Me.")
        self.button.setToolTip("Button, FE2")
        self.addWidget(self.button)
        
        
        #Call different types of File Explorer Layouts
        TEST_VERSION = 2
        call = 'list' + str(TEST_VERSION)
        MethodToCall = getattr(self, call)
        MethodToCall() #calls list#()
        
        
    def list1(self):
        #SAMPLE CODE
        model = QtGui.QFileSystemModel()
        #model.setRootPath('/home/cookieman/Dropbox/Files_x/Alpha')
        model.setRootPath('/home/cookieman/Dropbox/Files_x/Alpha')
        self.tree = QtGui.QTreeView()
        self.tree.setModel(model)
        
        self.addWidget(self.tree) #add widget to layout
        
    def list2(self):
        PATH = '/home/cookieman/Dropbox/Files_x/Alpha'
        explorer = QtGui.QListView()
        model = QtGui.QStandardItemModel()
        for i in self.getFolders(PATH):
            model.appendRow(i)
        for i in self.getFiles(PATH):
            model.appendRow(i)
        #model.(self.getFiles(PATH))
        #model.appendRow(self.getFolders(PATH))
        #explorer.setModel(self.getFiles('/home/cookieman/Dropbox/Files_x/Alpha'))
        explorer.setModel(model)
        self.addWidget(explorer)
    
        
    ''' Returns a QStandardItemModel
            icons set to Files
            Text set to Files names
    '''
    def getFiles(self, path):
        #model = QtGui.QStandardItemModel()
        list =[]
        icon = QtGui.QIcon('icon.gif')
        for name in os.listdir(path):
            if (os.path.isdir(os.path.join(path,name)) == 0):
                item = QtGui.QStandardItem(name)
                item.setIcon(icon)
                #model.appendRow(item)
                list.append(item)
        return list #using list to combine two models
    
    #Returns folders w/ image
    def getFolders(self, path):
        #model = QtGui.QStandardItemModel()
        list=[]
        icon = QtGui.QIcon('folderA.png')
        for name in os.listdir(path):
            if os.path.isdir(os.path.join(path,name)):
                item = QtGui.QStandardItem(name)
                item.setIcon(icon)
                #model.appendRow(item)
                list.append(item)
        return list
    