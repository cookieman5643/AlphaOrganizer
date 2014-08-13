'''
Created Aug. 5, 2014
@author: cookieman
'''

import sys, os
from PyQt4 import QtGui, QtCore

class FileExplorerTmp(QtGui.QWidget):
    
    def __init__(self):
        super(FileExplorerTmp, self).__init__()
        self.setPath()
        self.initUI()
        
    def setPath(self, str = '/home/cookieman/Dropbox/Files_x/Alpha'):
        self.PATH = str
        
#########################

    def initUI(self):
        #Widget's Layout
        self.layout = QtGui.QVBoxLayout()
        self.setLayout(self.layout)
        
        #Add Temp Btn
        self.btn = QtGui.QPushButton("I'm a Button.")
        self.layout.addWidget(self.btn)
        
        #Create Directory Widget
        VERSION = 1
        call = 'listDirectory' + str(VERSION)
        MethodToCall = getattr(self, call)
        MethodToCall()
        
    #Adds the directory Widget
    def listDirectory1(self):
        treeView = QtGui.QTreeView()
        model = QtGui.QStandardItemModel()
        path = self.PATH
        
        #Finish lists
        list = self.getModelList(path) #list of items
        # print(list)
        
        #Finish model Stuff
        headers = ['Home Folder. (header)']
        model.appendColumn(list)
        model.setHorizontalHeaderLabels(headers)
        
        #Finish TreeView Stuff
        treeView.setModel(model)
        treeView.clicked.connect(self.itemClicked)
        
        #Add TreeView to self's layout
        self.layout.addWidget(treeView)
        
    #Holds the Model for treeView (i.e. data)    
    def getModelList(self, path):
        #As of now, recursively fills
        listFiles = []
        listFolders = []
        iconFile = QtGui.QIcon('icon.gif')
        iconFolder = QtGui.QIcon('folderA.png')
        
        #List display name base off file with this tag
        nameFilterTag = self.getFolderNameFilterTag(path)
        #Lists based of file with this tag
        nameFilterTag = self.getFolderNameFilterTag(path) 
        
        for name in os.listdir(path):
            print('Path:',path,". Name: ",name)
            item = QtGui.QStandardItem()
            fullPath = os.path.join(path,name)
            if os.path.isdir(fullPath):
                item.setIcon(iconFolder)
                item.setText(name) #items displays folder's name
                item.setData(fullPath)
                item.appendRows(self.getModelList(fullPath)) #**RECURSIVE**
                print('Recursive fill. Folder: ' + name + " 's Children added.")
                listFolders.append(item)
                print('Add to listFolers.')
            if (os.path.isdir(fullPath) == 0):
                item.setIcon(iconFile)
                text = self.getTagContentsFromPath(nameFilterTag, fullPath)
                if text != '':
                    item.setText(text)
                else:
                    item.setText(name)
                item.setData(fullPath)
                listFiles.append(item)
                print('Add to listFiles.')
            print('Folders: ' , listFolders)
            print('Files: ' , listFiles)
               
        #Note sorting is by Alpha, Capfirst-LowerSecond
        #listFolders.sort()               
        #listFiles.sort()
        #return (listFolders)
        return (listFolders+listFiles)
        
    #When item in list is clicked.
    def itemClicked(self, index):
        print('FlExplr:click on: ',index.model().itemFromIndex(index).text())
        
    
    #Looks at Folder's property, find tag to display in listview.    
    #based of folderprop.txt 
    def getFolderNameFilterTag(self, path):
        default = 'NAME:'
        findTag = 'TAG_NAME:' #specific tag in folder prop for listing
        gotTag = self.getTagContentsFromPath(findTag, path +'/.folderprop.txt')
        if gotTag != '':
            return gotTag
        else: 
            return default
        
    #Given file, searches for 'TAG:' and returns contents
    #Returns empty string if not found
    def getTagContentsFromPath(self, tag, path):
        #TODO: grep it..
        result = ''
        fileName, fileExtension = os.path.splitext(path)
        if fileExtension == '.txt':
            if os.path.exists(path):
                for line in open(path): #reads each line in txt file
                    if tag in line:
                        for c in range(0,len(line)):
                            if line[c] == ':':
                                result = line[c+1:-1]
                                print("Found TAG: ",tag,' in ', path, ". Contents: ", result)
        return result  
        
    