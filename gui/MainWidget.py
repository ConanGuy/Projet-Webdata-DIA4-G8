from PyQt5.QtWidgets import *

from gui.LinePerCityWidget import LinePerCityWidget
from gui.UsersWidget import UsersWidget
from gui.TempWidget import TempWidget

class MainWidget(QWidget):
    
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        
        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(False)

        self.tabs.addTab(UsersWidget(self), "Utilisateurs")
        self.tabs.addTab(LinePerCityWidget(self), "Lignes par ville")
        self.tabs.addTab(TempWidget(self), "Temperatures")

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)