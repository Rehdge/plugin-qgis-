# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 17:30:27 2018

@author: regis
"""
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtXml import QDomDocument
from qgis.core import *
from qgis.gui import QgsMessageBar
import resources

import os
import sys
import os.path
import string
import math
import re
import inspect
import csv 

mplAvailable=True
try:
    import numpy as np
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    from matplotlib.mlab import griddata
    from shapely.geometry import MultiLineString, MultiPolygon
except:
    mplAvailable=False

from ui_Deplacement import Ui_DeplacementDialogBase





class Deplacement:

    def __init__(self, iface):
        self._iface = iface

    def initGui(self):
        if not mplAvailable:
            QMessageBox.warning(self._iface.mainWindow(), "Deplacement erreur")
            return

        self.action = QAction(QIcon(":/plugins/Deplacement/icon.png"), \
        "Deplacement", self._iface.mainWindow())
        self.action.setWhatsThis("Generer un schema permettant la visualisation de déplacements")
        QObject.connect(self.action, SIGNAL("triggered()"), self.run)
        self._iface.addToolBarIcon(self.action)
        self._iface.vectorMenu().addAction(self.action)

    def unload(self):
        try:
            self._iface.removePluginMenu("&Contour", self.action)
            self._iface.vectorMenu().removeAction(self.action)
            self._iface.removeToolBarIcon(self.action)
        except:
            pass

    def run(self):
        try:
            dlg = DeplacementDialog(self._iface)
            dlg.exec_()
        except DeplacementError:
            QMessageBox.warning(self._iface.mainWindow(), "Deplacement erreur",
                unicode(sys.exc_info()[1]))
                
                
                
                
class DeplacementError(Exception):
    pass

class DeplacementGenerationError(Exception):
    pass


class DeplacementDialog(QDialog,Ui_DeplacementDialogBase):
    
    def __init__(self, iface):
        QDialog.__init__(self)
        self._iface = iface
        
        self.setupUi(self)
        
        self.lineEdit_chemin_fichier.clear()
        self.lineEdit_nom_couche.clear()
        
        # connecte le QTableView au modèle de données
        self.tablevue.setModel(self.model)
        # ajuste la largeur des colonnes à leur contenu
        self.tablevue.resizeColumnsToContents()
        
        self.toolButton_charger_fichier.clicked.connect(self.select_output_file)
        
        
    def select_output_file(self):
        filename = QFileDialog.getSaveFileName(self,"Open file","/home/regis/Bureau/PROJET PPMD/DEVELOPPEMENT","Fichiers (*.txt *.csv)")
        
        name_file_1 = filename.split('/')[-1]
        name_file = name_file_1.split('.')[0]
        
        self.lineEdit_chemin_fichier.setText(filename)
        self.lineEdit_nom_couche.setText(name_file)
        
        Tableau = []
        f = filename #open("donnees_test_ter.csv")
        csv_f = csv.reader(f)
        for row in csv_f:
            Tableau.append(row)
        self.data = Tableau
 
        # crée le modèle de données
        self.model = QtGui.QStandardItemModel()
 
        # peuple le modèle
        for i, row in enumerate(self.data):
            for j, col in enumerate(row):
                item = QtGui.QStandardItem()
                item.setData(col, QtCore.Qt.DisplayRole)
                self.model.setItem(i, j, item)
 
        # met les titres des colonnes
        headers = Tableau[0]
        for j, header in enumerate(headers):
            titrecol = QtGui.QStandardItem(header)
            self.model.setHorizontalHeaderItem(j, titrecol)
   
        
        
        
    
        
        
        
       






