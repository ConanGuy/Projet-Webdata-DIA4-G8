from PyQt5.QtWidgets import *
from consts import *
import consts
import plotly.express as px
import pandas as pd
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets
        
class TempWidget(QWidget):
    
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        
        
        self.table = QTableWidget(self)
        self.table.setHorizontalHeaderLabels(["Ville", "Temperature"])
        self.show_table(self.get_table())
        
        self.btnrefresh = QPushButton("Refresh", self)
        self.btnrefresh.clicked.connect(self.refresh)
        
        self.layout.addWidget(self.btnrefresh)
        self.layout.addWidget(self.table)
        
        self.setLayout(self.layout)
        
    def refresh(self): 
        import load_live as ll
        
        ll.load_live()
        
        import pickle
        consts.G_TEMP = pickle.load(open('rdf_obj/temperatures.pkl', 'rb'))
        
        table = self.get_table()
        self.show_table(table)

    def get_table(self):     
        knows_query = """
        SELECT DISTINCT ?ville ?temp
        WHERE  {
            ?x :ville ?ville .
            ?x :temp ?temp .
        }"""

        users = []

        qres = consts.G_TEMP.query(knows_query)
        for row in qres:            
            users.append([str(row.ville),str(row.temp)])
            
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