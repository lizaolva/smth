import sys, spacy
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMainWindow, QTextEdit, QDockWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt

class MyWidget(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.nlp = spacy.load("en_core_web_sm")
        self.initUI()

    def initUI(self):
        self.setWindowTitle('parsing')
        self.setGeometry(450, 540, 820, 540)

        self.raw = QTextEdit('вставьте текст', self)
        self.raw.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(self.raw)

        self.button = QPushButton('распарсить', self)
        self.button.setGeometry(390, 250, 111, 51)
        """self.button.move(70, 150)
        self.button.setFixedWidth(200)"""
        self.button.clicked.connect(self.parse)

    def parse(self):
        print(self.raw.toPlainText())
         # опытом принта я выяснила, что проблема в этой строке и недоумеваю
        print(self.raw.toPlainText())
        doc = self.nlp(self.raw.toPlainText())
        l = []
        for token in doc:
            l.append([token.text, token.pos_, token.dep_, token.head.text])
        self.table = QTableWidget()
        self.table.setRowCount(len(l))
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["token", "POS", 'SyntR', 'Head'])
        self.createTable(l) 

    def createTable(self, l):    
        for token in l:
            self.table.setItem(l.index(token) + 1, 0, QTableWidgetItem(token[0]))
            self.table.setItem(l.index(token) + 1, 1, QTableWidgetItem(token[1] if token[1] else None))
            self.table.setItem(l.index(token) + 1, 2, QTableWidgetItem(token[2] if token[2] else None))
            self.table.setItem(l.index(token) + 1, 3, QTableWidgetItem(token[3] if token[3] else None))

        #self.table.adjustSize()

        tablewidget = QDockWidget(self)
        tablewidget.setWidget(self.table)
        self.addDockWidget(Qt.BottomDockWidgetArea, tablewidget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWidget = MyWidget()
    myWidget.show()
    sys.exit(app.exec_())

# сделать список списков из всех токенов и 