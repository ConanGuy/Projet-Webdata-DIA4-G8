from rdflib import Graph
import json
import pandas as pd

def main():    
    import gui.MainWindow as gui
    import sys
    from PyQt5 import QtWidgets
        
    app=QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    
    my_window=gui.MainWindow()
    my_window.show()
    app.exec_()

if __name__ == "__main__":
    main()