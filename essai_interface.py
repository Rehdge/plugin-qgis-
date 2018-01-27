# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 13:44:36 2018

@author: regis
"""
import csv
import sys, os
from functools import partial
from PyQt4 import QtCore, QtGui

 
#############################################################################
class Fenetre(QtGui.QWidget):
 
    # =======================================================================
    def __init__(self, parent=None):
        super(Fenetre, self).__init__(parent)
        self.resize(700, 300)
        Tableau = []
        f = open("donnees_test_ter.csv")
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
 
        # crée le QTableView
        self.tablevue = QtGui.QTableView(self)
        # connecte le QTableView au modèle de données
        self.tablevue.setModel(self.model)
        # ajuste la largeur des colonnes à leur contenu
        self.tablevue.resizeColumnsToContents()
        # exécutera la méthode donnée à chaque clic sur le QTableView
        #self.tablevue.clicked.connect(self.clic_tablevue)
 
        # positionne le QTableView dans la fenêtre
        posit = QtGui.QGridLayout()
        posit.addWidget(self.tablevue, 0, 0)
        self.setLayout(posit)
 
    # =======================================================================
    '''def clic_tablevue(self, index):
        """exécuté à chaque clic sur le QTableView
        """
        if index.column() == 1:
            # => on a cliqué sur la colonne des dates (indice 1)
 
            # récup du contenu (str) de la case cliquée
            date = index.data() 
            # crée un QDate avec la date de la case cliquée 
            qdate = QtCore.QDate()
            qdate.setDate(int(date[:4]), int(date[4:6]), int(date[6:])) 
 
            # crée le calendrier
            self.cal = QtGui.QCalendarWidget()
            self.cal.setGridVisible(True)
            # prépare la sortie du calendrier (on passe index en plus!)
            self.cal.clicked.connect(partial(self.clic_cal, index))
            # initialise le calendrier avec la date de la case cliquée
            self.cal.setSelectedDate(qdate) 
            # affiche la fenêtre du calendrier
            self.cal.show()
 
    # =======================================================================
    def clic_cal(self, index, qdate):
        """exécuté à chaque clic sur une date du calendrier
        """
        # récupère la date sélectionnée sous forme de chaine
        date2 = "%4d%02d%02d" % (qdate.year(), qdate.month(), qdate.day())
        # modifie la donnée grâce au modèle
        self.tablevue.model().setData(index, date2)
        # et ferme la fenêtre du calendrier
        self.cal.close()
 
    # =======================================================================
    def keyPressEvent(self, event):
        if self.tablevue.hasFocus():
            if event.key() == QtCore.Qt.Key_X and (event.modifiers() & QtCore.Qt.AltModifier):
                # récupére la liste data après modification
                imax, jmax = self.tablevue.model().rowCount(), self.tablevue.model().columnCount()
                data2 = []
                for i in range(0, imax):
                    data2.append([]) # nouvelle ligne
                    for j in range(0, jmax):
                        item = self.tablevue.model().item(i,j)
                        elem = item.data(QtCore.Qt.DisplayRole)
                        data2[-1].append(elem)
                print(data2)
                event.accept()
            else:
                event.ignore()
        else:
            event.ignore()'''
 
#############################################################################
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    fen = Fenetre()
    fen.setAttribute(QtCore.Qt.WA_DeleteOnClose)
    fen.show()
    sys.exit(app.exec_())