import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QFile
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        study_methods = ["Traditional Pomodoro", "Extended Pomodoro", "Animedoro"]
        self.study_intervals = ["25 minutes", "50 minutes", "40-60 minutes"]
        self.break_intervals = ["5 minutes", "10 minutes", "approx. 20 minutes - 1 anime (or other 20 minute) episode"]
        self.cycles = ["4, then take 15-30 minutes as a break", "2, then take 15-30 minutes as a break", "2, then take an extra 10 minutes"]
        
        self.ui.productivityChoose.addItems(study_methods)
        
        self.updateMethods()
        
        self.ui.productivityChoose.currentIndexChanged.connect(self.updateMethods)
            
        
    def updateMethods(self):
        method = self.ui.productivityChoose.currentIndex()
        self.ui.workLabel.setText("Work Interval: " + self.study_intervals[method])
        self.ui.breakLabel.setText("Break Interval: " + self.break_intervals[method])
        self.ui.cyclesLabel.setText("Cycles at a Time: " + self.cycles[method])

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())