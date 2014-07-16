'''
Created Jul 8, 2014

@author: cookieman
'''

#RE-write of my first File Explorer

#IMPORTS
import sys, os
from PyQt4 import QtGui, QtCore
from subprocess import call
from ExpandedViewWidget import ExpandedViewWidget


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
        TEST_VERSION = 6
        call = 'list' + str(TEST_VERSION)
        MethodToCall = getattr(self, call)
        MethodToCall() #calls list#()
        
        self.testBash()
        
        
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
        self.explorer = QtGui.QListView()
        self.modelE = QtGui.QStandardItemModel()
        for i in self.getFolders(PATH):
            self.modelE.appendRow(i)
        for i in self.getFiles(PATH):
            self.modelE.appendRow(i)
        #model.(self.getFiles(PATH))
        #model.appendRow(self.getFolders(PATH))
        #explorer.setModel(self.getFiles('/home/cookieman/Dropbox/Files_x/Alpha'))
        self.explorer.setModel(self.modelE)
        self.addWidget(self.explorer)
    
        self.explorer.clicked.connect(self.listClick)
    
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
                #itemChild = QtGui.QStandardItem()
                for nameChild in os.listdir(os.path.join(path,name)):
                    item.setChild(0, QtGui.QStandardItem(nameChild))
                list.append(item)
        return list
    
    def list3(self):
        PATH = '/home/cookieman/Dropbox/Files_x/Alpha'
       
        tree = QtGui.QTreeWidget()
        
        header = QtGui.QTreeWidgetItem(['Name', 'Second'])
        tree.setHeaderItem(header)
        
        root = QtGui.QTreeWidgetItem(tree,['root'])
        
        
        l = []
        iconFile = QtGui.QIcon('icon.gif')
        iconFolder = QtGui.QIcon('folderA.png')
        
        for name in os.listdir(PATH):
            if os.path.isdir(os.path.join(PATH,name)):
                item = QtGui.QTreeWidgetItem(root, [name])
                item.setIcon(0, iconFolder)
            if (os.path.isdir(os.path.join(PATH,name)) == 0):
                item = QtGui.QTreeWidgetItem(root, [name])
                item.setIcon(0, iconFile)
        tree.show()
        #tree.addTopLevelItems(l)
        
        
        #explorer.setModel(model)
        self.addWidget(tree)
    
    @QtCore.pyqtSlot(QtCore.QModelIndex)
    def listClick(self, index):
        print('Test row ', index.row(), ' data: ', index.data())
        PATH = '/home/cookieman/Dropbox/Files_x/Alpha'
        if os.path.isdir(os.path.join(PATH,index.data())):
            self.modelE.append(index.row(), ['str1','str2'])
        
        
    def list4(self):
        evw = ExpandedViewWidget(self.CURRENT_PATH)
        self.addWidget(evw)
        
    def list5(self):
        #This was practice/ sample with tree models and getting sub items
        treeView = QtGui.QTreeView()     
        model = QtGui.QStandardItemModel() 
        itemA = QtGui.QStandardItem('item1')
        itemB = QtGui.QStandardItem('item2')
        list = [itemA, itemB]
        model.appendRow(list)
        itemC = QtGui.QStandardItem('item3')
        itemD = QtGui.QStandardItem('item4')
        list2 = [itemC, itemD]
        #model.insertRow(0,list2)
        itemA.appendRow(list2)
        itemE = QtGui.QStandardItem('item5')
        itemF = QtGui.QStandardItem('item6')
        list3 = [itemE, itemF]
        itemC.appendRow(list3)
        treeView.setModel(model)
        self.addWidget(treeView)
        
    def list6(self):
        treeView = QtGui.QTreeView()
        model = QtGui.QStandardItemModel()
        PATH = '/home/cookieman/Dropbox/Files_x/Alpha'
        
        list = self.getModelList(PATH)
        model.appendColumn(list)
        treeView.setModel(model)
        treeView.clicked.connect(self.activeSelect)
                
        self.addWidget(treeView)
        
    def getModelList(self, path):
        #recursively fills folders until end
        #Goes with list6
        listFiles=[]
        listFolders=[]
        iconFile = QtGui.QIcon('icon.gif')
        iconFolder= QtGui.QIcon('folderA.png')
        
        for name in os.listdir(path):
            item = QtGui.QStandardItem()
            testName = os.path.join(path,name)
            if os.path.isdir(testName):
               item.setIcon(iconFolder)
               item.setText(name)
               item.setData(testName)
               item.appendRow(self.getModelList(testName))
               #item.clicked.connect(self.activeSelect('folder: ' +name))
               listFolders.append(item)
            if (os.path.isdir(testName) == 0):
                item.setIcon(iconFile)
                item.setText(name)
                #item.clicked.connect(self.activeSelect('file: ' + name))
                listFiles.append(item)
                
        listFiles.sort()
        return (listFolders+listFiles)
        
    def activeSelect(self,index):
        print('You have selected',index.model().itemFromIndex(index).text())
        print('Data: ', index.model().itemFromIndex(index).data())
        # print self.model.itemFromIndex(index).text()
    
    def testBash(self):
        print(call(["ls", "-l"]))
        