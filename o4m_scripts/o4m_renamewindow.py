from PySide2 import QtWidgets, QtCore, QtGui
from maya.api.OpenMaya import MGlobal

mayaApp = QtWidgets.QApplication.instance()
mainWindow = 0

for qw in mayaApp.topLevelWidgets():
    
    if(qw.objectName() == "MayaWindow"):
        
        mainWindow = qw

class Window(QtWidgets.QWidget):
    
    def __init__(self):
        
        super().__init__(mainWindow)

        #Window properties
        self.resize(550, 100)
        self.winLayout = QtWidgets.QVBoxLayout(self)
        self.setWindowTitle("Organise4M - Rename")
        self.setWindowFlags(QtCore.Qt.Window)
        self.modes = ["All", "Prefix", "Prefix Edit", "Suffix", "Suffix Edit"]
        
        #Font properties
        self.font = QtGui.QFont()
        self.font.setFamily("Noto Sans")
        self.font.setPointSize(12)
        self.setFont(self.font)
        
        #Object name box
        self.nameLayout = QtWidgets.QHBoxLayout(self)
        self.nameLabel = QtWidgets.QLabel("Name: ", self)
        self.nameBox = QtWidgets.QLineEdit(self)
        self.nameLayout.addWidget(self.nameLabel)
        self.nameLayout.addWidget(self.nameBox)
        self.winLayout.addLayout(self.nameLayout)
        
        #Object options grid
        self.optionsLayout = QtWidgets.QGridLayout()
        
        #Mode option
        self.modeLayout = QtWidgets.QHBoxLayout(self)
        self.modeLabel = QtWidgets.QLabel("Mode: ", self)
        self.modeBox = QtWidgets.QComboBox(self)
        self.modeBox.addItems(self.modes)
        self.modeLayout.addWidget(self.modeLabel)
        self.modeLayout.addWidget(self.modeBox)
        self.modeLayout.addStretch()
        
        #Padding option
        self.padLayout = QtWidgets.QHBoxLayout(self)
        self.padLabel = QtWidgets.QLabel("Padding: ", self)
        self.padBox = QtWidgets.QSpinBox(self)
        self.padBox.setMaximum(8)
        self.padBox.setMinimum(0)
        self.padBox.setMinimumWidth(100)
        self.padLayout.addWidget(self.padLabel)
        self.padLayout.addWidget(self.padBox)
        self.padLayout.addStretch()

        #Add options to option layout
        self.optionsLayout.addLayout(self.modeLayout, 0, 0)
        self.optionsLayout.addLayout(self.padLayout, 0, 1)
        self.winLayout.addLayout(self.optionsLayout)
        
        #Buttons
        self.btnLayout = QtWidgets.QHBoxLayout(self)
        self.cancelBtn = QtWidgets.QPushButton("Cancel", self)
        self.cancelBtn.clicked.connect(self.close)
        self.exeBtn = QtWidgets.QPushButton("Rename", self)
        self.exeBtn.clicked.connect(self.rename)
        self.btnLayout.addWidget(self.cancelBtn)
        self.btnLayout.addWidget(self.exeBtn)
        self.winLayout.addLayout(self.btnLayout)

        self.winLayout.addStretch()
    
    def rename(self, *args, **kwargs):
        
        mode = ""

        match self.modeBox.currentText():
            
            case "Prefix":
                mode = "-p"
            case "Prefix Edit":
                mode = "-pe"
            case "Suffix":
                mode = "-s"
            case "Suffix Edit":
                mode = "-se"

        cmdStr = "o4m_rename " + mode + " \"" + self.nameBox.text() + "\" " + str(self.padBox.value())
        MGlobal.displayInfo(cmdStr)
        MGlobal.executeCommandOnIdle(cmdStr)
    
if mainWindow != 0:
    
    window = Window()
    window.show()