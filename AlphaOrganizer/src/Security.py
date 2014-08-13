'''
Created Aug 10, 2014
@author: cookieman
'''

#Imports
import sys, os
from subprocess import call
from PyQt4 import QtGui, QtCore


class Security(QtGui.QWidget):
    PATH = '/home/cookieman/Dropbox/Files_x/Alpha'
    PASSWORD_FILENAME = '.g_alpha'
    CRYPT_WORD = ''
    VERIFY_WORD= ''
    
    def __init__(self, path = '/home/cookieman/Dropbox/Files_x/Alpha'):
        super(Security, self).__init__()
        print("Security: init")
        self.PATH = path        
      
    #Called by main application, check password_filename, encryption
    #decrypt if needed
    #Verify Password Match.    
    def initChecks(self):
        b = self.isPasswordSet()
        print("b: ", str(b))
        
        PW_EXISTS_ENCRYPTED = 2
        PW_EXISTS_UNENCRYPTED = 1
        PW_DOESNOTEXIST = 0
        
        if(b==PW_EXISTS_ENCRYPTED):
            self.decryptDialog()
            self.decryptFile(os.path.join(self.PATH,self.PASSWORD_FILENAME), self.CRYPT_WORD)
            self.verifyDialog()
            value = self.verifyPassword(self.VERIFY_WORD)
            if(value): 
                return 1
            else: 
                return 0
        elif(b==PW_EXISTS_UNENCRYPTED):
            self.verifyDialog()
            value = self.verifyPassword(self.VERIFY_WORD)
            if(value):
                return 1
            else:
                return 0
        elif(b==PW_DOESNOTEXIST):
            print("Need to Setup initial password")
        else:
            print("Confusing...")
            return 0
        
           
    #Return 0 or 1 - checks password_file @ path if exists
    def isPasswordSet(self):
        print("Security: isPasswordSet.")
        strpath = os.path.join(self.PATH,self.PASSWORD_FILENAME)                   
        if (os.path.exists(strpath+".cpt")):
            isSet = 2 #file exists, encrypted
        elif (os.path.exists(strpath)):
            isSet = 1 #file exists, unencrypted
        else:
            isSet = 0
        return isSet
    
    #Creates dialog, gets user's decypt word
    def decryptDialog(self):
        print("Security: decryptDialog.")
        self.dialogDecrypt = QtGui.QDialog()
        self.dialogDecrypt.resize(300,100)
        
        label = QtGui.QLabel("Enter Decryption Password:")
        field = QtGui.QLineEdit()
        field.setMaxLength(25)
        
        button = QtGui.QPushButton("Decrypt.")
        def setDecryptWord():
            text = field.text()
            print("decryptDialog: Field text: ", text)
            self.CRYPT_WORD = text
            self.dialogDecrypt.close()
        button.clicked.connect(setDecryptWord)
            
        layout = QtGui.QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(field)
        layout.addWidget(button)
        
        self.dialogDecrypt.setLayout(layout)
        self.dialogDecrypt.exec()
    
    #Create dialog, gets user's verification password.
    def verifyDialog(self):
        print("Security: verifyDialog.")          
        self.dialogVerify = QtGui.QDialog()
        self.dialogVerify.resize(300,100)
        
        label = QtGui.QLabel("Enter Verification Password:")
        field = QtGui.QLineEdit()
        field.setMaxLength(25)
        
        button = QtGui.QPushButton("Verify.")
        def setVerifyWord():
            text = field.text()
            print("verifyDialog: Field text: ", text)
            self.VERIFY_WORD = text
            self.dialogVerify.close()
        button.clicked.connect(setVerifyWord)
            
        layout = QtGui.QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(field)
        layout.addWidget(button)
        
        self.dialogVerify.setLayout(layout)
        self.dialogVerify.exec()
    
    #Given file and keyword, decrypt          
    def decryptFile(self, filenamePath, decryptWord):
        #TODO: return 0, 1
        print("Security: decryptFile.")
        print("Decrypting: ", filenamePath, " with: " , decryptWord)
        call(["ccrypt","-d",filenamePath, "-K", decryptWord])
        
    #Given file and keyword, encrypt
    def encryptFile(self, filenamePath, encryptWord):
        print("Security: encryptFile.")
        print("Encrypting: ", filenamePath, " with: " , encryptWord)
        call(["ccrypt","-e",filenamePath, "-K", encryptWord])
        
    #Checks given str matches password in password file
    def verifyPassword(self, password):
        print("Security: verifyPassword")
        passwordfromfile = open(os.path.join(self.PATH,self.PASSWORD_FILENAME),mode = 'r').read()
        if(passwordfromfile == password): 
            print("Password verified!")
            return 1
        else: 
            return 0
    
    #Encrypts file named with same decrypt word.    
    def reEncryptPasswordFile(self):
        if(self.CRYPT_WORD != ''):
            self.encryptFile(os.path.join(self.PATH,self.PASSWORD_FILENAME),self.CRYPT_WORD)


##### SLIGHTLY EXTRA #####
    def setPasswordFileName(self,str):
        self.PASSWORD_FILENAME = str
        
    def getPasswordFileName(self):
        return self.PASSWORD_FILENAME
##########################        
        
          
def main():
    app = QtGui.QApplication(sys.argv)
    sec = Security()
    sys.exit(app.exec_())
    
if __name__== '__main__':
    main()
    
'''
    ##init
     boolPassSet = self.isSetPassword()
        if(boolPassSet):  self.verifyPassword()
        else: dialog = SetPassword()
        #v = SetPassword()
        #vv = VerifyPassword()
    ##
    
    ###Class set pW
    class SetPassword(QtGui.QDialog):
    
    def __init__(self):
        super(SetPassword, self).__init__()
        
        boolPassSet = self.isSetPassword()
        
        self.initUI()
        
    def isSetPassword(self):
        isSet = 0
        return isSet
        
    def initUI(self):
        self.initialPassword()
        
        self.resize(300,100)
        self.show()
        
    def initialPassword(self):
        label = QtGui.QLabel("Set Password: ")
        layout = QtGui.QVBoxLayout()
        field = QtGui.QLineEdit()
        field.setMaxLength(20)
        button = QtGui.QPushButton("Set.")
        
        layout.addWidget(label)
        layout.addWidget(field)
        layout.addWidget(button)
        
        self.setLayout(layout)
        
        def setClicked():
            self.INIT = field.text()
            print("Initial: ", self.INIT)
            #TODO: if text not null, yada yada
            self.confirmPassword()
            self.close()
        button.clicked.connect(setClicked)
        
        
    def confirmPassword(self):
        self.dialog = QtGui.QDialog()
        
        
        label2 = QtGui.QLabel("Confirm Password: ")
        layout2 = QtGui.QVBoxLayout()
        field2 = QtGui.QLineEdit()
        field2.setMaxLength(20)
        button2 = QtGui.QPushButton("Confirm.")
        
        layout2.addWidget(label2)
        layout2.addWidget(field2)
        layout2.addWidget(button2)
        
        #self.setLayout(layout2)
        self.dialog.setLayout(layout2)
        self.dialog.show()
        
        
        def confirmClicked():
            #TODO: Check if confirm matches.
            self.CONFIRM = field2.text()
            print("Confirm: ", self.CONFIRM)
            self.writeToFile()
            self.dialog.close()
        button2.clicked.connect(confirmClicked)
        
    def writeToFile(self):
        #Get Bash to write password to file.
        print()
    ###
           
    ####Class Verify Password
    
        
class VerifyPassword(QtGui.QWidget):
    def __init__(self, path = '/home/cookieman/Dropbox/Files_x/Alpha'): 
        super(VerifyPassword, self).__init__()
        print('VerifyPasswordClass, init')
        self.PATH = path
        self.initUI()
        self.show()
        
    def initUI(self):
        self.dialogDecrypt = QtGui.QDialog()
        
        label = QtGui.QLabel("Enter Decryption Password:")
        field = QtGui.QLineEdit()
        field.setMaxLength(25)
        button = QtGui.QPushButton("Decrypt.")
        #button.clicked.connect(self.decryptFile)
        layout = QtGui.QVBoxLayout()
        
        layout.addWidget(label)
        layout.addWidget(field)
        layout.addWidget(button)
        
        self.dialogDecrypt.setLayout(layout)
        
        self.decryptPassword()
        
        self.resize(300,100)
        self.show()
        
    def decryptPassword(self):
        print("001 - dec")
        
        
        
        def decryptFile():
            print("ehllo")
    ####
            
'''