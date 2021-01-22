import sys, random, time
from PySide2.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QInputDialog, QLineEdit
from PySide2.QtCore import QFile, QRandomGenerator
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.popup = QMessageBox()
        self.inputPopup = QInputDialog()
        self.completed = 0
        self.num_tasks = 0
        
        study_methods = ["Traditional Pomodoro", "Extended Pomodoro", "Animedoro"]
        self.study_intervals = ["25 minutes", "50 minutes", "40-60 minutes"]
        self.break_intervals = ["5 minutes", "10 minutes", "approx. 20 minutes - 1 anime (or other 20 minute) episode"]
        self.cycles = ["4, then take 15-30 minutes as a break", "2, then take 15-30 minutes as a break", "2, then take an extra 10 minutes"]
        
        self.ui.productivityChoose.addItems(study_methods)
        
        self.updateMethods()
        
        self.ui.productivityChoose.currentIndexChanged.connect(self.updateMethods)
        
        self.ui.chooseButton.clicked.connect(self.selectTask)
        
        self.ui.addTaskButton.clicked.connect(self.addTask)
        
        self.ui.completeButton.clicked.connect(self.completeTask)
        
        self.ui.deleteButton.clicked.connect(self.deleteTask)
        
        self.ui.completeLabel.setText("Number of Tasks Completed: " + str(self.completed))
        self.ui.incompleteLabel.setText("Number of Tasks Completed: " + str(self.num_tasks - self.completed))
        
        #Setting up the Table
        self.ui.tasksTable.setColumnCount(5)
        self.ui.tasksTable.setHorizontalHeaderLabels(["Task Name", "Subject", "Estimated Duration", "Actual Time Taken", "Completed"])
        self.ui.tasksTable.resizeColumnsToContents()
        
    def updateLabels(self):
        self.ui.completeLabel.setText("Number of Tasks Completed: " + str(self.completed))
        self.ui.incompleteLabel.setText("Number of Tasks Incomplete: " + str(self.num_tasks - self.completed))
        time_worked = 0
        est_time_left = 0
        for i in range(0, self.ui.tasksTable.rowCount()):
            if self.ui.tasksTable.item(i, 4).text() == "Yes":
                time_worked += int(self.ui.tasksTable.item(i, 3).text())
            else:
                est_time_left += int(self.ui.tasksTable.item(i, 2).text())
        self.ui.timeWorkedLabel.setText("Total Time Worked: " + str(time_worked) + " minutes = " + str(round(time_worked/60, 2)) + " hours")
        self.ui.timeNeededLabel.setText("Estimated Time Needed to Finish: " + str(est_time_left) + " minutes = " + str(round(est_time_left/60,2)) + " hours")
        
        
    def addTask(self):
        if self.ui.taskBox.text() == "" or self.ui.subjectBox.text() == "" or self.ui.timeBox.text() == "":
           self.popup.warning(self, "Error", "One or more fields are empty" + "\n Please Complete and Retry.") 
        else:
            self.ui.tasksTable.setRowCount(self.ui.tasksTable.rowCount() + 1)
            self.ui.tasksTable.setItem(self.ui.tasksTable.rowCount() - 1, 0, QTableWidgetItem(self.ui.taskBox.text()))
            self.ui.tasksTable.setItem(self.ui.tasksTable.rowCount() - 1, 1, QTableWidgetItem(self.ui.subjectBox.text()))
            self.ui.tasksTable.setItem(self.ui.tasksTable.rowCount() - 1, 2, QTableWidgetItem(self.ui.timeBox.text()))
            self.ui.tasksTable.setItem(self.ui.tasksTable.rowCount() - 1, 3, QTableWidgetItem(""))
            self.ui.tasksTable.setItem(self.ui.tasksTable.rowCount() - 1, 4, QTableWidgetItem("No"))
            self.ui.tasksTable.resizeColumnsToContents()
            
            self.ui.taskBox.clear()
            self.ui.subjectBox.clear()
            self.ui.timeBox.clear()
            
            self.num_tasks += 1
            self.updateLabels()
    
    def completeTask(self):
        time_taken, formality = QInputDialog().getText(self, "Mark as Complete",
                                     "Time Taken to Complete:", QLineEdit.Normal)
        current_row = self.ui.tasksTable.currentRow()
        self.ui.tasksTable.setItem(current_row, 3, QTableWidgetItem(time_taken))
        self.ui.tasksTable.setItem(current_row, 4, QTableWidgetItem("Yes"))
        
        self.completed += 1
        self.updateLabels()
        
    def deleteTask(self):
        current_row = self.ui.tasksTable.currentRow()
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
        
        self.num_tasks -= 1
        
        self.updateLabels()
        
    def updateMethods(self):
        method = self.ui.productivityChoose.currentIndex()
        self.ui.workLabel.setText("Work Interval: " + self.study_intervals[method])
        self.ui.breakLabel.setText("Break Interval: " + self.break_intervals[method])
        self.ui.cyclesLabel.setText("Cycles at a Time: " + self.cycles[method])
        
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