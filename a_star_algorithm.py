# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'a_star_algorithm.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from graph import *
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_a_star_algorithm(object):
    def setupUi(self, a_star_algorithm):
        a_star_algorithm.setObjectName("a_star_algorithm")
        a_star_algorithm.resize(498, 110)
        self.verticalLayout = QtWidgets.QVBoxLayout(a_star_algorithm)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(a_star_algorithm)
        self.label.setStyleSheet("font: 14pt \".AppleSystemUIFont\";")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(a_star_algorithm)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems(G.nodes)
        self.horizontalLayout.addWidget(self.comboBox)
        self.label_2 = QtWidgets.QLabel(a_star_algorithm)
        self.label_2.setStyleSheet("font: 14pt \".AppleSystemUIFont\";")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.comboBox_2 = QtWidgets.QComboBox(a_star_algorithm)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItems(G.nodes)
        self.horizontalLayout.addWidget(self.comboBox_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.buttonBox = QtWidgets.QDialogButtonBox(a_star_algorithm)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(a_star_algorithm)
        self.buttonBox.accepted.connect(a_star_algorithm.accept) # type: ignore
        self.buttonBox.rejected.connect(a_star_algorithm.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(a_star_algorithm)


    def retranslateUi(self, a_star_algorithm):
        _translate = QtCore.QCoreApplication.translate
        a_star_algorithm.setWindowTitle(_translate("a_star_algorithm", "Алгоритм А*"))
        self.label.setText(_translate("a_star_algorithm", "Начальная вершина:"))
        self.label_2.setText(_translate("a_star_algorithm", "Целевая вершина:"))


    def show_data(self):
        return (self.comboBox.currentText(), self.comboBox_2.currentText())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    a_star_algorithm = QtWidgets.QDialog()
    ui = Ui_a_star_algorithm()
    ui.setupUi(a_star_algorithm)
    a_star_algorithm.show()
    sys.exit(app.exec_())

def a_star_algorithm_dialog():
    global a_star_algorithm
    a_star_algorithm = QtWidgets.QDialog()
    ui = Ui_a_star_algorithm()
    ui.setupUi(a_star_algorithm)
    a_star_algorithm.show()

    if a_star_algorithm.exec():
        a_star(ui.show_data()[0], ui.show_data()[1])