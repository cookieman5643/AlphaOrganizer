'''
Created Jul 14, 2014

@Author: cookieman
'''


#This Widget Object will list all the folders and files give a path

#IMPORTS
import sys, os
from PyQt4 import QtGui
#from PyQt4 import QtGui, QtCore
from SingleViewWidget import SingleViewWidget


#CLASS DEFINITION   
class ExpandedViewWidget(QtGui.QWidget):
    
    def __init__(self, path):
        super(ExpandedViewWidget, self).__init__()
        self.PATH = path    #Initialized Path
        print('path: ',path)
        print('selfpath',self.PATH)
        
        self.initUI()       #Create UI
        
    def initUI(self):
        #Self's List Widget
        self.vBox = QtGui.QVBoxLayout()
        self.setLayout(self.vBox)
        
        #Simple Button for kicks
        button= QtGui.QPushButton() 
        button.clicked.connect(self.buttonPushed)
        self.vBox.addWidget(button)
        
        #Make ListView
        self.listView = QtGui.QListView()
        listFile =[]
        listFolder =[]
        #Fill ListView
        for obj in os.listdir(self.PATH):
            print('object in dir: ',obj)
            objName = os.path.join(self.PATH,obj)
            if os.path.isdir(objName) == 0:
                item = SingleViewWidget(objName)
                listFile.append(item)
            if os.path.isdir(objName):
                item = SingleViewWidget(objName)
                listFolder.append(item)
        
        listmerge = listFolder + listFile
        
        print(listFolder)
        
        model = QtGui.QStandardItemModel()
        #model.insertRows(0, 0, listmerge)
        self.listView.setModel(model)
        #Add ListView
        self.vBox.addWidget(self.listView)
        
    def buttonPushed(self):
        print('Button Pushed')