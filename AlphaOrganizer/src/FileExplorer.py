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
        self.setPath()
        self.initUI()
        
    def initUI(self):
        self.button = QtGui.QPushButton()
        self.addWidget(self.button)
        
        self.listLocal()
        #self.uiMore()
        #self.addFoldersFiles()
    
    #Get Path
    def setPath(self):
        self.CURRENT_PATH = '/home/cookieman/Dropbox/Files_x/Alpha' + '/files'
    
    #Get all the Directories in a given path *NOT FULL
    def getFolders(self, path):
        list = []
        for name in os.listdir(path):
            #s = os.path.join(path,name) possibly return full path
            if os.path.isdir(os.path.join(path,name)):
                list.append(name)
        return list
    
    #Get all the Files in a path, not Full paths
    def getFiles(self, path):
        list =[]
        for name in os.listdir(path):
            if (os.path.isdir(os.path.join(path,name)) == 0):
                list.append(name)
        return list
    
    #Current Directory Folders and Files
    def listLocal(self):
        self.explorerContainer = QtGui.QListWidget()
        self.explorerContainer.insertItems(0, self.getFolders(self.CURRENT_PATH))
        self.explorerContainer.insertItems(0, self.getFiles(self.CURRENT_PATH))
        self.addWidget(self.explorerContainer)
    
    #Start with the initial path
    def addFoldersFiles(self):
        #Create objects to hold info
        self.foldersList = []
        self.filesList = []
        self.testList =[]
        self.explorerContainer = QtGui.QListWidget()
        
        
                
        for name in os.listdir(self.CURRENT_PATH):
            if os.path.isdir(os.path.join(self.CURRENT_PATH, name)):
                self.testList.append(name)
        
        print(self.testList)
        
        #Add the folders and files
        self.explorerContainer.insertItems(0, self.foldersList)
        self.explorerContainer.insertItems(-1, self.filesList)
        self.explorerContainer.insertItems(-1, self.testList)
        
        #Set view to this ListWidget
        self.addWidget(self.explorerContainer)
        
        
        
        '''
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
        '''
        
    #Walks through all subdirectories and files
    def listAllFilesAndFolers(self):
        self.foldersList = []
        self.filesList = []
        
        #Fill objects with into
        for root, dirs, files in os.walk(self.CURRENT_PATH, topdown=False):
            for name in files:
                self.filesList.append(name)
                #print(name)
                print(os.path.join(root,name)) #print full filename
            for name in dirs:
                self.foldersList.append(name)
        
    #Extra Code
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
        