import sys, random, time, os
import numpy as np
from PySide2.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QInputDialog, QLineEdit
from PySide2.QtCore import QTimer
from ui_mainwindow import Ui_MainWindow

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
        
        study_methods = ["Traditional Pomodoro", "Extended Pomodoro", "Animedoro"]
        self.study_intervals = ["25 minutes", "50 minutes", "40-60 minutes"]
        self.break_intervals = ["5 minutes", "10 minutes", "approx. 20 minutes - one anime (or other with a similar duration) episode"]
        self.cycles = ["4, then take 15-30 minutes as a break", "2, then take 15-30 minutes as a break", "2, then take an extra 10 minutes"]
        
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
        
        timer = QTimer(self)
        timer.timeout.connect(self.cycleTimer)
        timer.start(1000) #change back to 1000
        
    def newCycle(self):
        if self.timer == False:
            self.updateMethods()
        else:
            self.popup.warning(self, "Error", "Cycle Already Running" + "\n Please 'End Early' before starting a new cycle") 
        
    def startCycle(self):
        self.timer = True
        
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
        
    def cycleTimer(self):
        if self.timer:
            if self.second_count == 0 and self.minutes != 0:
                self.minutes -= 1
                self.second_count = 59
                self.second_count -= 1
                self.ui.timerLabel.setText(str(self.minutes) + ":" + str(self.second_count))
            elif self.second_count == 0 and self.minutes == 0:
                if self.status == "Work":
                    self.minutes = int(self.break_time) - 1
                    self.second_count = 59
                    self.status = "Break"
                    self.ui.statusLabel.setText("BREAK")
                    self.ui.timerLabel.setText(str(self.minutes) + ":" + str(self.second_count))
                elif self.status == "Break":
                    self.minutes = 0
                    self.second_count = 0
                    self.status = "Work"
                    self.timer = False
                    self.ui.statusLabel.setText("CYCLE OVER")
                    self.ui.timerLabel.setText(str(self.minutes) + ":" + str(self.second_count))
            else:
                self.second_count -= 1
                self.ui.timerLabel.setText(str(self.minutes) + ":" + str(self.second_count))
        
    def clear(self):
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
        if self.ui.tasksTable.item(current_row, 4).text() == "Yes":
            self.completed -= 1
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
        method = self.ui.productivityChoose.currentIndex()
        self.ui.workLabel.setText("Work Interval: " + self.study_intervals[method])
        self.ui.breakLabel.setText("Break Interval: " + self.break_intervals[method])
        self.ui.cyclesLabel.setText("Cycles at a Time: " + self.cycles[method])
        self.study_time = ''.join(i for i in self.study_intervals[method] if i.isdigit())
        if self.study_time == "4060":
            self.study_time = "60"
        self.break_time = ''.join(i for i in self.break_intervals[method] if i.isdigit())
        
        minutes = self.study_time
        self.ui.timerLabel.setText(str(minutes) + ":" + "00")
        self.minutes = int(self.study_time) - 1
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