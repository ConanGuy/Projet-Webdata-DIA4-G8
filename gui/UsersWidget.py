from PyQt5.QtWidgets import *
from consts import *
import plotly.express as px
import pandas as pd
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

class SearchWidget(QWidget):
    
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QHBoxLayout(self)
        
        self.userSearch = QtWidgets.QLineEdit(self)
        
        self.btnSearch = QtWidgets.QPushButton("Search", self)
        self.btnSearch.clicked.connect(self.search)
        
        self.layout.addWidget(self.userSearch)
        self.layout.addWidget(self.btnSearch)
        
        self.setLayout(self.layout)
        
        self.setFixedHeight(self.userSearch.height()*2)
        
    def search(self):
        self.btnSearch.setDisabled(True)
        users = self.parent().get_table(self.userSearch.text())
        self.parent().show_table(users)
        self.btnSearch.setDisabled(False)
        
class UsersWidget(QWidget):
    
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        
        
        self.table = QTableWidget(self)
        self.table.setHorizontalHeaderLabels(["ID", "Pseudo", "Prénom", "Nom", "Age"])
        self.show_table(self.get_table(""))
        
        self.search = SearchWidget(self)
        
        self.layout.addWidget(self.search)
        self.layout.addWidget(self.table)
        
        self.setLayout(self.layout)

    def get_table(self, username):      
        knows_query = """
        SELECT DISTINCT ?username ?identifier ?first_name ?last_name ?age
        WHERE  {
            { 
                ?x :username ?username .
                ?x :identifier ?identifier .
                ?x :first_name ?first_name .
                ?x :last_name ?last_name .
                ?x :age ?age .
                FILTER regex(?username, """+'"'+username+'"'+""", "i") 
            } 
        }"""

        users = []

        qres = G_USERNAME.query(knows_query)
        for row in qres:            
            users.append([str(row.identifier),str(row.username),str(row.first_name),str(row.last_name),str(row.age)])
            
        return users
    
    def show_table(self, users):   
        if len(users) == 0:
            return
  
        #Row count
        self.table.setRowCount(len(users)) 
  
        #Column count
        self.table.setColumnCount(len(users[0]))  
  
        for ix, row in enumerate(users):
            for iy, item in enumerate(row):
                self.table.setItem(ix,iy, QTableWidgetItem(item))