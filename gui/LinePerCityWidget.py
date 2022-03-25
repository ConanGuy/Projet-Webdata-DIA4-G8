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
        
        self.citySearch = QtWidgets.QLineEdit(self)
        self.citySearch.setText('massy')
        
        self.btnSearch = QtWidgets.QPushButton("Search", self)
        self.btnSearch.clicked.connect(self.search)
        
        self.layout.addWidget(self.citySearch)
        self.layout.addWidget(self.btnSearch)
        
        self.setLayout(self.layout)
        
        self.setFixedHeight(self.citySearch.height()*2)
        
    def search(self):
        self.btnSearch.setDisabled(True)
        fig = self.parent().get_fig(self.citySearch.text())
        self.parent().show_graph(fig)
        self.btnSearch.setDisabled(False)
        
class LinePerCityWidget(QWidget):
    
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        
        
        self.browser = QtWebEngineWidgets.QWebEngineView(self)
        self.show_graph(self.get_fig("massy"))
        
        self.search = SearchWidget(self)
        
        self.layout.addWidget(self.search)
        self.layout.addWidget(self.browser)
        
        self.setLayout(self.layout)

    def get_fig(self, ville):      
        knows_query = """
        SELECT DISTINCT ?origine ?destination
        WHERE  {
            { 
                ?x :origine ?origine .
                ?x :destination ?destination .
                FILTER regex(?origine, """+'"'+ville+'"'+""", "i") 
            } 
        }"""

        columns=['trip', 'lat', 'lon', 'city']
        df = pd.DataFrame(columns=columns)

        columns2=['trip', 'lat', 'lon', 'city']
        stations = []
        df2 = pd.DataFrame(columns=columns2)

        qres = G_TGVMAX.query(knows_query)
        for row in qres:            
            q1 = """
            SELECT DISTINCT ?lat ?lon ?name
            WHERE  {
                { 
                    ?x :latitude ?lat .
                    ?x :longitude ?lon .
                    ?x :nom_gare ?name .
                    FILTER regex(?name, """+'"'+row.origine+'"'+""", "i") 
                } UNION {
                    ?x :latitude ?lat .
                    ?x :longitude ?lon .
                    ?x :nom_gare ?name .
                    FILTER regex(?name, """+'"'+row.destination+'"'+""", "i") 
                }
            }"""
            
            qres2 = G_GARES.query(q1)
            if len(qres2) < 2: continue 
            for row2 in qres2:
                data = [str(row.origine)+" - "+str(row.destination), float(str(row2.lat)), float(str(row2.lon)), str(row2.name)]
                
                if str(row2.name) not in stations:
                    stations.append(str(row2.name))
                    df2 = pd.concat([df2,pd.DataFrame([data], columns=columns2)])
                    
                df = pd.concat([df, pd.DataFrame([data], columns=columns)])
            
        fig = px.line_mapbox(df, lat="lat", lon="lon", color="trip")
        fig.update_layout(mapbox_style="carto-positron", mapbox_zoom=4, mapbox_center_lat = 41,
            margin={"r":0,"t":0,"l":0,"b":0})
        fig.update_layout(showlegend=False)

        df2["color"] = 1
        fig2 = px.scatter_mapbox(df2, lat="lat", lon="lon", color="city", size="color", size_max=10)

        for d in fig2.data:
            fig.add_trace(d)
        return fig
    def show_graph(self, fig):   
        self.browser.setHtml(fig.to_html(include_plotlyjs='cdn'))
        