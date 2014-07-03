'''
Created on Jul 3, 2014

@author: cookieman
'''

import sys
import os
from PyQt4 import QtGui, QtCore, Qt
from random import randint

class FileExplorer(QtGui.QVBoxLayout):
    
    def __init__(self):
        super(FileExplorer, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.button = QtGui.QPushButton()
        self.addWidget(self.button)
        
        self.uiMore()
        self.addFolders()
        
    def uiMore(self):
        model = QtGui.QStandardItemModel()

        for n in range(10):                   
            item = QtGui.QStandardItem('Item %s' % randint(1, 100))
            check = 1 if randint(0, 1) == 1 else 0
            item.setCheckState(check)
            item.setCheckable(True)
            model.appendRow(item)
        
        
        self.view = QtGui.QListView()
        self.view.setModel(model)
        
        self.addWidget(self.view)  
    
    def addFolders(self):
        folders = QtGui.QStandardItemModel()
        folderListKind = []
        for i in os.listdir('/home/cookieman/Dropbox/Files_x'):
            item = QtGui.QStandardItem(str(i))
            folders.appendRow(item)
            folderListKind.append(str(i))
            print(str(i))
        
        
        
        self.folderList = QtGui.QListWidget()
        #self.folderList.setModel(folders)
        folderListKind.sort(key=None, reverse=False)
        self.folderList.insertItems(-1, folderListKind)
        self.addWidget(self.folderList)
        
        
        