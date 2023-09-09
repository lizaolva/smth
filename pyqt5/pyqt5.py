import sys, spacy
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMainWindow, QTextEdit
from PyQt5.QtCore import Qt

class MyWidget(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('parsing')
        self.setGeometry(300, 250, 350, 200)

        self.raw = QTextEdit('вставьте текст', self)
        self.setCentralWidget(self.raw)
        self.raw.setFixedWidth(200)
        self.raw.move(100, 250)

        self.button = QPushButton('распарсить', self)
        self.button.move(70, 150)
        self.button.setFixedWidth(200)
        self.button.clicked.connect(self.parse)

    def parse(self):
        print(self.raw.toPlainText())
        nlp = spacy.load("en_core_web_sm") # опытом принта я выяснила, что проблема в этой строке и недоумеваю
        print(self.raw.toPlainText())
        doc = nlp(self.raw.toPlainText())
        l = []
        for token in doc:
            l.append(f'{token.i:2}. {token.text:15} POS: {token.pos_:6} SyntR: {token.dep_:9} Head: {token.head.text}')
        self.text = QLabel(l, self)
        self.text.adjustSize()
        self.setDockWidget(self.text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWidget = MyWidget()
    myWidget.show()
    sys.exit(app.exec_())
