from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class TotalCommander(QMainWindow):
    def __init__(self):
        super(TotalCommander, self).__init__()

        self.setupMenus()
        self.setupToolBar()
        self.interfejs()

    def interfejs(self):

        self.grid = QGridLayout()
        self.grid.setSpacing(0)

        mainLayout = QVBoxLayout()
        mainLayout.setSpacing(0)

        
        list1 = QListWidget()

        names1 = ['[$Recycle.Bin]','[CISCO_CCNA]', '[Dev-Cpp]', '[Documents and ..]', '[fancycode-pylz..]']

        for name in names1:
            list1.addItem(name)

        list2 = QListWidget()
        names1 = ['[$Recycle.Bin]','[CISCO_CCNA]', '[Dev-Cpp]', '[Documents and ..]', '[fancycode-pylz..]']

        
        for name in names1:
            list2.addItem(name)


        self.grid.addWidget(list1,0,0,1,1)
        self.grid.addWidget(list2,0,1,1,1)

        self.hbox2 = QHBoxLayout ()
        self.hbox2.setSpacing(0)
        self.label = QLabel("C:\> ")
        self.hbox2.addWidget(self.label)

        self.hbox1 = QHBoxLayout ()
        self.hbox1.setSpacing(0)
        self.but1 = QPushButton(self)
        self.but1.setText("F3 View")
        self.but2 = QPushButton(self)
        self.but2.setText("F4 Edit")
        self.but3 = QPushButton(self)
        self.but3.setText("F5 Copy")
        self.but4 = QPushButton(self)
        self.but4.setText("F6 Move")
        self.but5 = QPushButton(self)
        self.but5.setText("F7 NewFolder")
        self.but6 = QPushButton(self)
        self.but6.setText("F8 Delete")
        self.but7 = QPushButton(self)
        self.but7.setText("Al+F4 Exit")

        self.hbox1.addWidget(self.but1)
        self.hbox1.addWidget(self.but2)
        self.hbox1.addWidget(self.but3)
        self.hbox1.addWidget(self.but4)
        self.hbox1.addWidget(self.but5)
        self.hbox1.addWidget(self.but6)
        self.hbox1.addWidget(self.but7)

        mainLayout.addLayout(self.grid)
        mainLayout.addLayout(self.hbox2)
        mainLayout.addLayout(self.hbox1)
        widget = QWidget()
        widget.setLayout(mainLayout)
        self.setCentralWidget(widget)

        self.setStyleSheet("""QWidget {
         background-color: silver;
        }

        QPushButton {
         background: silver;
        }

        
        QMenuBar {
         background-color: silver;
        }

        QMenuBar::item {
         background: silver;
        }""")


        self.setGeometry(70, 70, 500, 500)
        self.setWindowIcon(QIcon('total.png'))
        self.setWindowTitle("Total Commander 7.50a - Politechnika Lodzka - Wydzial EEIA")


    def setupMenus(self):

        filesMenu = self.menuBar().addMenu("Files")
        filesMenu.addSeparator()
        markMenu = self.menuBar().addMenu("Mark")
        markMenu.addSeparator()
        commandsMenu = self.menuBar().addMenu("Commands")
        commandsMenu.addSeparator()
        nextMenu = self.menuBar().addMenu("Next")
        nextMenu.addSeparator()
        showMenu = self.menuBar().addMenu("Show")
        showMenu.addSeparator()
        confMenu = self.menuBar().addMenu("Configuration")
        confMenu.addSeparator()
        startMenu = self.menuBar().addMenu("Start")
        startMenu.addSeparator()

        indexAction = QAction(QIcon('znak.png'),"Index", self)
        indexAction.setShortcut("F1")
        keyboardAction = QAction("Keyboard", self)
        regAction = QAction("Registration Info", self)
        vistAction = QAction("Visit Totalcmd's Web Site", self)
        aboutAction = QAction("About Total Comander...", self)
        
        helpMenu = self.menuBar().addMenu("Help")
        helpMenu.addAction(indexAction)
        helpMenu.addAction(keyboardAction)
        helpMenu.addAction(regAction)
        helpMenu.addAction(vistAction)
        helpMenu.addAction(aboutAction)

    def setupToolBar(self):
    	tb = self.addToolBar("File")

    	refresh = QAction(QIcon("refresh.png"),"refresh",self)
    	tb.addAction(refresh)

    	one = QAction(QIcon("one.png"),"one",self)
    	tb.addAction(one)

    	two = QAction(QIcon("two.png"),"two",self)
    	tb.addAction(two)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    okno = TotalCommander()
    okno.show()
    sys.exit(app.exec_())
