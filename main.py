import sys, random, time, os
from datetime import date, timedelta
import numpy as np
from reportlab.pdfgen.canvas import Canvas
import PySide2
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, QTimer)
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
        self.actionNew_Day = QAction(MainWindow)
        self.actionNew_Day.setObjectName(u"actionNew_Day")
        self.actionNewDay = QAction(MainWindow)
        self.actionNewDay.setObjectName(u"actionNewDay")
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
        self.timerButton = QPushButton(self.centralwidget)
        self.timerButton.setObjectName(u"timerButton")
        self.timerButton.setGeometry(QRect(40, 580, 131, 41))
        self.timerButton.setFont(font2)
        self.statusLabel = QLabel(self.centralwidget)
        self.statusLabel.setObjectName(u"statusLabel")
        self.statusLabel.setGeometry(QRect(350, 580, 281, 41))
        font4 = QFont()
        font4.setPointSize(28)
        self.statusLabel.setFont(font4)
        self.timerLabel = QLabel(self.centralwidget)
        self.timerLabel.setObjectName(u"timerLabel")
        self.timerLabel.setGeometry(QRect(190, 580, 181, 41))
        self.timerLabel.setFont(font4)
        self.playPauseButton = QPushButton(self.centralwidget)
        self.playPauseButton.setObjectName(u"playPauseButton")
        self.playPauseButton.setGeometry(QRect(40, 630, 131, 41))
        self.playPauseButton.setFont(font2)
        self.resetButton = QPushButton(self.centralwidget)
        self.resetButton.setObjectName(u"resetButton")
        self.resetButton.setGeometry(QRect(370, 400, 131, 41))
        self.resetButton.setFont(font2)
        self.endButton = QPushButton(self.centralwidget)
        self.endButton.setObjectName(u"endButton")
        self.endButton.setGeometry(QRect(180, 630, 131, 41))
        self.endButton.setFont(font2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1280, 21))
        self.menuNew_Day = QMenu(self.menubar)
        self.menuNew_Day.setObjectName(u"menuNew_Day")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuNew_Day.menuAction())
        self.menuNew_Day.addAction(self.actionNewDay)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ToDo+", None))
        self.actionNew_Day.setText(QCoreApplication.translate("MainWindow", u"New Day", None))
        self.actionNewDay.setText(QCoreApplication.translate("MainWindow", u"New Day (Clear)", None))
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
        self.timerButton.setText(QCoreApplication.translate("MainWindow", u"Start Cycle", None))
        self.statusLabel.setText(QCoreApplication.translate("MainWindow", u"WORK", None))
        self.timerLabel.setText(QCoreApplication.translate("MainWindow", u"00:00", None))
        self.playPauseButton.setText(QCoreApplication.translate("MainWindow", u"Play/Pause", None))
        self.resetButton.setText(QCoreApplication.translate("MainWindow", u"New Cycle", None))
        self.endButton.setText(QCoreApplication.translate("MainWindow", u"End Early", None))
        self.menuNew_Day.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.popup = QMessageBox()
        self.inputPopup = QInputDialog()
        self.tasks = []
        self.timer = False
        self.study_time = 0
        self.break_time = 0
        self.second_count = 60
        self.status = "Work"
        self.timer_status = "Play"

        if not os.path.exists(os.path.join(os.path.expanduser("~"), "Documents\ToDo+")):
            os.mkdir(os.path.join(os.path.expanduser("~"), "Documents\ToDo+")) 
        
        #Setting up the Table
        self.ui.tasksTable.setColumnCount(5)
        self.ui.tasksTable.setHorizontalHeaderLabels(["Task Name", "Subject", "Estimated Duration", "Actual Time Taken", "Completed"])
        self.ui.tasksTable.resizeColumnsToContents()
        
        if not os.path.exists("tasks.npy"):
            tasks_to_save = np.array(self.tasks)
            np.save("tasks", tasks_to_save)
        else:
            self.tasks = list(np.load("tasks.npy"))
            self.loadTasks()
        
        study_methods = ["Traditional Pomodoro", "Extended Pomodoro", "Animedoro", "Desktime Pomodoro", "Ultradian Rhythms", "45-45 Variation"]
        self.study_intervals = ["25 minutes", "50 minutes", "40-60 minutes", "52 minutes", "90 minutes", "45 minutes"]
        self.break_intervals = ["5 minutes", "10 minutes", "≈ 20 minutes - one anime (or other similar length) episode", "17 minutes", "25-30 minutes", "2 minutes"]
        self.cycles = ["4, then take 15-30 minutes as a break", "2, then take 15-30 minutes as a break", "2, then take an extra 10 minutes", "2 then take 20-35 minutes as a break", "1", "2, then take a 30 minute break"]
        
        self.ui.productivityChoose.addItems(study_methods)
        
        self.updateMethods()
        
        self.ui.productivityChoose.currentIndexChanged.connect(self.updateMethods)
        
        self.ui.chooseButton.clicked.connect(self.selectTask)
        
        self.ui.addTaskButton.clicked.connect(self.addTask)
        
        self.ui.completeButton.clicked.connect(self.completeTask)
        
        self.ui.deleteButton.clicked.connect(self.deleteTask)
        
        self.ui.actionNewDay.triggered.connect(self.clear)
        
        self.ui.timerButton.clicked.connect(self.startCycle)
        
        self.ui.endButton.clicked.connect(self.endEarly)
        
        self.ui.resetButton.clicked.connect(self.newCycle)
        
        self.ui.playPauseButton.clicked.connect(self.playPause)
        
        timer = QTimer(self)
        timer.timeout.connect(self.cycleTimer)
        timer.start(1000) #change back to 1000
        
    def playPause(self):
        if self.timer_status == "Play":
            self.timer_status = "Pause"
        elif self.timer_status == "Pause":
            self.timer_status = "Play"
        
    def newCycle(self):
        if self.timer == False:
            self.updateMethods()
        else:
            self.popup.warning(self, "Error", "Cycle Already Running" + "\n Please 'End Early' before starting a new cycle") 
        
    def startCycle(self):
        self.timer = True
        self.timer_status = "Play"
        
    def endEarly(self):
        self.timer = False
        if self.minutes <= 20 and self.break_time == "20" and self.status == "Work":
            self.minutes = self.break_time
            self.second_count = 59
            self.status = "Break"
            self.ui.statusLabel.setText("BREAK")
            self.timer = True
        elif self.status == "Work":
            self.ui.statusLabel.setText("CYCLE FAIL")

    def updateClock(self):
        if self.minutes < 10 and self.second_count < 10:
            self.ui.timerLabel.setText("0" + str(self.minutes) + ":" + "0" + str(self.second_count))
        elif self.minutes < 10 and self.second_count >= 10:
            self.ui.timerLabel.setText("0" + str(self.minutes) + ":" + str(self.second_count))
        elif self.minutes >= 10 and self.second_count < 10:
            self.ui.timerLabel.setText(str(self.minutes) + ":" + "0" + str(self.second_count))
        else:
            self.ui.timerLabel.setText(str(self.minutes) + ":" + str(self.second_count))
    
    def cycleTimer(self):
        if self.timer == True and self.timer_status == "Play":
            if self.second_count == 0 and self.minutes != 0:
                self.minutes = int(self.minutes) - 1
                self.second_count = 59
                self.updateClock()
            elif self.second_count == 0 and self.minutes == 0:
                if self.status == "Work":
                    self.minutes = int(self.break_time) - 1
                    self.second_count = 59
                    self.status = "Break"
                    self.ui.statusLabel.setText("BREAK")
                    self.updateClock()
                elif self.status == "Break":
                    self.minutes = 0
                    self.second_count = 0
                    self.status = "Work"
                    self.timer = False
                    self.ui.statusLabel.setText("CYCLE OVER")
                    self.updateClock()
            else:
                self.second_count -= 1
                self.updateClock()
        
    def clear(self):
        num_tasks_completed = int(''.join(i for i in self.ui.completeLabel.text() if i.isdigit()))
        num_tasks_incompleted = int(''.join(i for i in self.ui.incompleteLabel.text() if i.isdigit()))

        time_worked = self.ui.timeWorkedLabel.text()
        time_needed_to_finish = self.ui.timeNeededLabel.text()

        yesterday = date.today() - timedelta(days = 1)
        yesterday = yesterday.strftime("%d-%m-%Y") 

        save_name = os.path.join(os.path.expanduser("~"), "Documents\ToDo+", "Work Report (" + yesterday + ").pdf")

        report = Canvas(save_name)
        report.drawString(72, 720, "ToDo+ Work Report (" + yesterday + ")")
        report.drawString(72, 690, "Total Number of Tasks: " + str(num_tasks_completed + num_tasks_incompleted))
        report.drawString(72, 670, "Number of Tasks Finished: " + str(num_tasks_completed))
        report.drawString(72, 650, "Number of Tasks Unfinished: " + str(num_tasks_incompleted))
        report.drawString(72, 625, "Task Productivity Score : " + str(round((num_tasks_completed - num_tasks_incompleted)/(num_tasks_completed + num_tasks_incompleted), 2)))
        
        report.save()

        self.tasks = []
        self.saveTasks()
        self.loadTasks()
        
    def saveTasks(self):
        tasks_to_save = np.array(self.tasks)
        np.save("tasks", tasks_to_save)
        
    def loadTasks(self):
        if len(self.tasks) == 0:
            self.ui.tasksTable.setRowCount(0)
        for i in range(0, len(self.tasks)):
            self.ui.tasksTable.setRowCount(self.ui.tasksTable.rowCount() + 1)
            self.ui.tasksTable.setItem(i, 0, QTableWidgetItem(self.tasks[i][0]))
            self.ui.tasksTable.setItem(i, 1, QTableWidgetItem(self.tasks[i][1]))
            self.ui.tasksTable.setItem(i, 2, QTableWidgetItem(self.tasks[i][2]))
            self.ui.tasksTable.setItem(i, 3, QTableWidgetItem(self.tasks[i][3]))
            if self.tasks[i][4] == "Ye":
                self.tasks[i][4] = "Yes"
            self.ui.tasksTable.setItem(i, 4, QTableWidgetItem(self.tasks[i][4]))
            
        self.updateLabels()
        
    def updateLabels(self):
        self.ui.tasksTable.resizeColumnsToContents()
        completed = 0
        incomplete = 0
        time_worked = 0
        est_time_left = 0
        for i in range(0, self.ui.tasksTable.rowCount()):
            if self.ui.tasksTable.item(i, 4).text() == "Yes":
                time_worked += int(self.ui.tasksTable.item(i, 3).text())
                completed += 1
            else:
                est_time_left += int(self.ui.tasksTable.item(i, 2).text())
                incomplete += 1
        self.ui.timeWorkedLabel.setText("Total Time Worked: " + str(time_worked) + " minutes = " + str(round(time_worked/60, 2)) + " hours")
        self.ui.timeNeededLabel.setText("Estimated Time Needed to Finish: " + str(est_time_left) + " minutes = " + str(round(est_time_left/60,2)) + " hours")
        self.ui.completeLabel.setText("Number of Tasks Completed: " + str(completed))
        self.ui.incompleteLabel.setText("Number of Tasks Incomplete: " + str(incomplete))
        
        
    def addTask(self):
        if self.ui.taskBox.text() == "" or self.ui.subjectBox.text() == "" or self.ui.timeBox.text() == "":
           self.popup.warning(self, "Error", "One or more fields are empty" + "\n Please Complete and Retry.") 
        else:
            tasks = [self.ui.taskBox.text(), self.ui.subjectBox.text(), self.ui.timeBox.text(), "", "No"]
            self.ui.tasksTable.setRowCount(self.ui.tasksTable.rowCount() + 1)
            self.ui.tasksTable.setItem(self.ui.tasksTable.rowCount() - 1, 0, QTableWidgetItem(self.ui.taskBox.text()))
            self.ui.tasksTable.setItem(self.ui.tasksTable.rowCount() - 1, 1, QTableWidgetItem(self.ui.subjectBox.text()))
            self.ui.tasksTable.setItem(self.ui.tasksTable.rowCount() - 1, 2, QTableWidgetItem(self.ui.timeBox.text()))
            self.ui.tasksTable.setItem(self.ui.tasksTable.rowCount() - 1, 3, QTableWidgetItem(""))
            self.ui.tasksTable.setItem(self.ui.tasksTable.rowCount() - 1, 4, QTableWidgetItem("No"))
            self.ui.tasksTable.resizeColumnsToContents()
            
            self.tasks.append(tasks)
            self.saveTasks()
            
            self.ui.taskBox.clear()
            self.ui.subjectBox.clear()
            self.ui.timeBox.clear()
            
            self.updateLabels()
    
    def completeTask(self):
        time_taken, formality = QInputDialog().getText(self, "Mark as Complete",
                                     "Time Taken to Complete:", QLineEdit.Normal)
        current_row = self.ui.tasksTable.currentRow()
        self.ui.tasksTable.setItem(current_row, 3, QTableWidgetItem(time_taken))
        self.ui.tasksTable.setItem(current_row, 4, QTableWidgetItem("Yes"))
        
        self.tasks[current_row][3] = time_taken
        self.tasks[current_row][4] = "Yes"
        
        self.saveTasks()
        
        self.updateLabels()
        
    def deleteTask(self):
        current_row = self.ui.tasksTable.currentRow()
        del self.tasks[current_row]
        if current_row != self.ui.tasksTable.rowCount() - 1:
            for i in range(current_row, self.ui.tasksTable.rowCount() - 1):
                self.ui.tasksTable.setItem(i, 0, QTableWidgetItem(self.ui.tasksTable.item(i+1, 0).text()))
                self.ui.tasksTable.setItem(i, 1, QTableWidgetItem(self.ui.tasksTable.item(i+1, 1).text()))
                self.ui.tasksTable.setItem(i, 2, QTableWidgetItem(self.ui.tasksTable.item(i+1, 2).text()))
                self.ui.tasksTable.setItem(i, 3, QTableWidgetItem(self.ui.tasksTable.item(i+1, 3).text()))
                self.ui.tasksTable.setItem(i, 4, QTableWidgetItem(self.ui.tasksTable.item(i+1, 4).text())) 
                
        self.ui.tasksTable.setRowCount(self.ui.tasksTable.rowCount() - 1)
        
        self.saveTasks()
                
        self.updateLabels()
        
    def updateMethods(self):
        if self.timer == True:
            self.popup.warning(self, "Error", "A work cycle is currently running." + "\n Please end the cycle before selecting a new productivity method.") 
        else:
            method = self.ui.productivityChoose.currentIndex()
            self.ui.workLabel.setText("Work Interval: " + self.study_intervals[method])
            self.ui.breakLabel.setText("Break Interval: " + self.break_intervals[method])
            self.ui.cyclesLabel.setText("Cycles at a Time: " + self.cycles[method])
            self.study_time = ''.join(i for i in self.study_intervals[method] if i.isdigit())
            if self.study_time == "4060":
                self.study_time = "60"
            self.break_time = ''.join(i for i in self.break_intervals[method] if i.isdigit())
            if self.break_time == "2530":
                self.break_time = "30"
            
            minutes = self.study_time
            self.ui.timerLabel.setText(str(minutes) + ":" + "00")
            self.minutes = int(self.study_time) - 1
            self.second_count = 60
            self.ui.statusLabel.setText("WORK")
            self.status = "Work"
        
    def selectTask(self):
        if self.ui.tasksTable.rowCount() == 0 or self.ui.tasksTable.rowCount() == 1:
            number = self.ui.tasksTable.rowCount()
        else:
            number = random.randint(1, self.ui.tasksTable.rowCount())
            while self.ui.tasksTable.item(number - 1, 4).text() == "Yes":
                number = random.randint(1, self.ui.tasksTable.rowCount())
                
        time.sleep(1)
        self.ui.taskChosenLabel.setText(str(number))

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    
    sys.exit(app.exec_())