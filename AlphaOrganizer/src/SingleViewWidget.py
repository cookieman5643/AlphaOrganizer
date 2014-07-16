'''
Created Jul 14, 2014

@Author: cookieman
'''


#This Widget Object will show icon and name

#IMPORTS
import sys, os
from PyQt4 import QtGui
#from PyQt4 import QtGui, QtCore
from subprocess import call


#CLASS DEFINITION   
class SingleViewWidget(QtGui.QAbstractItemView):
    
    def __init__(self, path):
        super(SingleViewWidget, self).__init__()
        self.PATH = path    #Initialized Path
        self.NAME = self.getName()
        self.initUI()       #Create UI
        
    def initUI(self):
        #Add icon
        self.icon = QtGui.QIcon('folderA.png')
        #self.setIcon(self.icon)
        
        #Add Name
        #self.setText(self.NAME)
        
        
    def buttonPushed(self):
        print('Button Pushed Single View')
        
    def getName(self):
        search = "'['TITLE:"
        result = self.PATH  #call(["grep -F", search, self.PATH])
        
        return result