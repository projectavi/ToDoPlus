import sys, random, time
from PySide2.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox
from PySide2.QtCore import QFile, QRandomGenerator
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.popup = QMessageBox()
        
        study_methods = ["Traditional Pomodoro", "Extended Pomodoro", "Animedoro"]
        self.study_intervals = ["25 minutes", "50 minutes", "40-60 minutes"]
        self.break_intervals = ["5 minutes", "10 minutes", "approx. 20 minutes - 1 anime (or other 20 minute) episode"]
        self.cycles = ["4, then take 15-30 minutes as a break", "2, then take 15-30 minutes as a break", "2, then take an extra 10 minutes"]
        
        self.ui.productivityChoose.addItems(study_methods)
        
        self.updateMethods()
        
        self.ui.productivityChoose.currentIndexChanged.connect(self.updateMethods)
        
        self.ui.chooseButton.clicked.connect(self.selectTask)
        
        self.ui.addTaskButton.clicked.connect(self.addTasks)
        
        #Setting up the Table
        self.ui.tasksTable.setColumnCount(5)
        self.ui.tasksTable.setHorizontalHeaderLabels(["Task Name", "Subject", "Estimated Duration", "Actual Time Taken", "Completed"])
        
    def addTasks(self):
        if self.ui.taskBox.text() == "" or self.ui.subjectBox.text() == "" or self.ui.timeBox.text() == "":
           self.popup.warning(self, "Error", "One or more fields are empty" + "\n Please Complete and Retry.") 
        else:
            self.ui.tasksTable.setRowCount(self.ui.tasksTable.rowCount() + 1)
            task_item = QTableWidgetItem(self.ui.taskBox.text())
            subject_item = QTableWidgetItem(self.ui.subjectBox.text())
            eta_item = QTableWidgetItem(self.ui.timeBox.text())
            print(task_item)
            self.ui.tasksTable.setItem(self.ui.tasksTable.rowCount() - 1, 0, task_item)
            self.ui.tasksTable.setItem(self.ui.tasksTable.rowCount() - 1, 1, subject_item)
            self.ui.tasksTable.setItem(self.ui.tasksTable.rowCount() - 1, 2, eta_item)

        
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
        time.sleep(3)
        self.ui.taskChosenLabel.setText(str(number))

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    
    sys.exit(app.exec_())