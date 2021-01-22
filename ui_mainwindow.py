# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tasksTable = QTableWidget(self.centralwidget)
        self.tasksTable.setObjectName(u"tasksTable")
        self.tasksTable.setGeometry(QRect(685, 0, 591, 491))
        self.tasksTable.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tasksTable.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tasksTable.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tasksTable.setColumnCount(0)
        self.tasksTable.horizontalHeader().setCascadingSectionResizes(True)
        self.tasksTable.horizontalHeader().setMinimumSectionSize(45)
        self.taskHeader = QLabel(self.centralwidget)
        self.taskHeader.setObjectName(u"taskHeader")
        self.taskHeader.setGeometry(QRect(10, 10, 161, 41))
        font = QFont()
        font.setPointSize(18)
        self.taskHeader.setFont(font)
        self.subjectLabel = QLabel(self.centralwidget)
        self.subjectLabel.setObjectName(u"subjectLabel")
        self.subjectLabel.setGeometry(QRect(10, 70, 111, 31))
        font1 = QFont()
        font1.setPointSize(12)
        self.subjectLabel.setFont(font1)
        self.taskLabel = QLabel(self.centralwidget)
        self.taskLabel.setObjectName(u"taskLabel")
        self.taskLabel.setGeometry(QRect(10, 120, 111, 31))
        self.taskLabel.setFont(font1)
        self.timeLabel = QLabel(self.centralwidget)
        self.timeLabel.setObjectName(u"timeLabel")
        self.timeLabel.setGeometry(QRect(10, 170, 271, 31))
        self.timeLabel.setFont(font1)
        self.subjectBox = QLineEdit(self.centralwidget)
        self.subjectBox.setObjectName(u"subjectBox")
        self.subjectBox.setGeometry(QRect(320, 60, 211, 41))
        self.taskBox = QLineEdit(self.centralwidget)
        self.taskBox.setObjectName(u"taskBox")
        self.taskBox.setGeometry(QRect(320, 110, 211, 41))
        self.timeBox = QLineEdit(self.centralwidget)
        self.timeBox.setObjectName(u"timeBox")
        self.timeBox.setGeometry(QRect(320, 160, 211, 41))
        self.addTaskButton = QPushButton(self.centralwidget)
        self.addTaskButton.setObjectName(u"addTaskButton")
        self.addTaskButton.setGeometry(QRect(410, 220, 121, 41))
        self.addTaskButton.setFont(font1)
        self.productivityHeader = QLabel(self.centralwidget)
        self.productivityHeader.setObjectName(u"productivityHeader")
        self.productivityHeader.setGeometry(QRect(10, 300, 321, 41))
        self.productivityHeader.setFont(font)
        self.chooseTaskLabel = QLabel(self.centralwidget)
        self.chooseTaskLabel.setObjectName(u"chooseTaskLabel")
        self.chooseTaskLabel.setGeometry(QRect(10, 360, 131, 31))
        self.chooseTaskLabel.setFont(font1)
        self.chooseButton = QPushButton(self.centralwidget)
        self.chooseButton.setObjectName(u"chooseButton")
        self.chooseButton.setGeometry(QRect(150, 350, 131, 41))
        font2 = QFont()
        font2.setPointSize(10)
        self.chooseButton.setFont(font2)
        self.productivityLabel = QLabel(self.centralwidget)
        self.productivityLabel.setObjectName(u"productivityLabel")
        self.productivityLabel.setGeometry(QRect(10, 410, 181, 31))
        self.productivityLabel.setFont(font1)
        self.productivityChoose = QComboBox(self.centralwidget)
        self.productivityChoose.setObjectName(u"productivityChoose")
        self.productivityChoose.setGeometry(QRect(200, 400, 161, 41))
        self.workLabel = QLabel(self.centralwidget)
        self.workLabel.setObjectName(u"workLabel")
        self.workLabel.setGeometry(QRect(40, 450, 581, 31))
        self.workLabel.setFont(font2)
        self.breakLabel = QLabel(self.centralwidget)
        self.breakLabel.setObjectName(u"breakLabel")
        self.breakLabel.setGeometry(QRect(40, 490, 561, 31))
        self.breakLabel.setFont(font2)
        self.cyclesLabel = QLabel(self.centralwidget)
        self.cyclesLabel.setObjectName(u"cyclesLabel")
        self.cyclesLabel.setGeometry(QRect(40, 530, 581, 31))
        self.cyclesLabel.setFont(font2)
        self.completeButton = QPushButton(self.centralwidget)
        self.completeButton.setObjectName(u"completeButton")
        self.completeButton.setGeometry(QRect(690, 500, 291, 31))
        self.deleteButton = QPushButton(self.centralwidget)
        self.deleteButton.setObjectName(u"deleteButton")
        self.deleteButton.setGeometry(QRect(980, 500, 291, 31))
        self.taskChosenLabel = QLabel(self.centralwidget)
        self.taskChosenLabel.setObjectName(u"taskChosenLabel")
        self.taskChosenLabel.setGeometry(QRect(300, 350, 291, 41))
        self.taskChosenLabel.setFont(font1)
        self.completeLabel = QLabel(self.centralwidget)
        self.completeLabel.setObjectName(u"completeLabel")
        self.completeLabel.setGeometry(QRect(680, 540, 581, 31))
        font3 = QFont()
        font3.setPointSize(11)
        self.completeLabel.setFont(font3)
        self.incompleteLabel = QLabel(self.centralwidget)
        self.incompleteLabel.setObjectName(u"incompleteLabel")
        self.incompleteLabel.setGeometry(QRect(680, 570, 571, 31))
        self.incompleteLabel.setFont(font3)
        self.timeWorkedLabel = QLabel(self.centralwidget)
        self.timeWorkedLabel.setObjectName(u"timeWorkedLabel")
        self.timeWorkedLabel.setGeometry(QRect(680, 600, 571, 31))
        self.timeWorkedLabel.setFont(font3)
        self.timeNeededLabel = QLabel(self.centralwidget)
        self.timeNeededLabel.setObjectName(u"timeNeededLabel")
        self.timeNeededLabel.setGeometry(QRect(680, 630, 581, 31))
        self.timeNeededLabel.setFont(font3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1280, 25))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ToDoPlus", None))
        self.taskHeader.setText(QCoreApplication.translate("MainWindow", u"Add a Task", None))
        self.subjectLabel.setText(QCoreApplication.translate("MainWindow", u"Subject", None))
        self.taskLabel.setText(QCoreApplication.translate("MainWindow", u"Task Name", None))
        self.timeLabel.setText(QCoreApplication.translate("MainWindow", u"Estimated Duration (minutes)", None))
        self.addTaskButton.setText(QCoreApplication.translate("MainWindow", u"Add Task", None))
        self.productivityHeader.setText(QCoreApplication.translate("MainWindow", u"Productivity Techniques", None))
        self.chooseTaskLabel.setText(QCoreApplication.translate("MainWindow", u"Task Selector", None))
        self.chooseButton.setText(QCoreApplication.translate("MainWindow", u"Choose Task", None))
        self.productivityLabel.setText(QCoreApplication.translate("MainWindow", u"Productivity Method", None))
        self.productivityChoose.setCurrentText("")
        self.workLabel.setText(QCoreApplication.translate("MainWindow", u"Work Interval: ", None))
        self.breakLabel.setText(QCoreApplication.translate("MainWindow", u"Break Interval: ", None))
        self.cyclesLabel.setText(QCoreApplication.translate("MainWindow", u"Cycles at a Time: ", None))
        self.completeButton.setText(QCoreApplication.translate("MainWindow", u"Mark as Complete", None))
        self.deleteButton.setText(QCoreApplication.translate("MainWindow", u"Delete Task", None))
        self.taskChosenLabel.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.completeLabel.setText(QCoreApplication.translate("MainWindow", u"Number of Tasks Completed:", None))
        self.incompleteLabel.setText(QCoreApplication.translate("MainWindow", u"Number of Tasks Incomplete:", None))
        self.timeWorkedLabel.setText(QCoreApplication.translate("MainWindow", u"Total Time Worked:", None))
        self.timeNeededLabel.setText(QCoreApplication.translate("MainWindow", u"Estimated Time Needed to Finish:", None))
    # retranslateUi

