import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtPrintSupport
import speech_recognition as sr
import sys
from PyQt5 import QtQuick
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5 import QtWidgets
import os
from tqdm import tqdm
from multiprocessing.dummy import Pool


class Main(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.initUI()

    def initUI(self):

        #  Toolbar

        #  Upper Toolbar
        aboutAction = QAction(QIcon("icons/about.png"), "About", self)
        aboutAction.setStatusTip("About")
        aboutAction.triggered.connect(self.About)

        usergdAction =QAction(QIcon("icons/usergd.png"), "User Guide",self)
        usergdAction.setStatusTip("User Guide")
        usergdAction.triggered.connect(self.Guide)

        updateAction = QAction(QIcon("icons/update.png"),"Check for updates", self)
        updateAction.setStatusTip("Check for updates")
        updateAction.triggered.connect(self.Update)

        feedbackAction = QAction(QIcon("icons/feedback.png"), "Feedback", self)
        feedbackAction.setStatusTip("Feedback")
        feedbackAction.triggered.connect(self.Feedback)

        recordAction = QAction(QIcon("icons/record.png"), "Record", self)
        recordAction.setShortcut("Ctrl+D")
        recordAction.setStatusTip("Start a new recording")
        recordAction.triggered.connect(self.Record)

        newAction = QAction(QIcon("icons/new.png"), "New", self)
        newAction.setShortcut("Ctrl+N")
        newAction.setStatusTip("Create a new document from scratch.")
        newAction.triggered.connect(self.New)

        openAction = QAction(QIcon("icons/open.png"), "Open file", self)
        openAction.setStatusTip("Open existing document")
        openAction.setShortcut("Ctrl+O")
        openAction.triggered.connect(self.Open)

        saveAction = QAction(QIcon("icons/save.png"), "Save", self)
        saveAction.setStatusTip("Save document")
        saveAction.setShortcut("Ctrl+S")
        saveAction.triggered.connect(self.Save)

        save_asAction = QAction(QIcon("icons/save_as.png"), "Save As", self)
        save_asAction.setStatusTip("Save document")
        save_asAction.setShortcut("Shift+Ctrl+S")
        save_asAction.triggered.connect(self.Save_As)

        closeAction = QAction(QIcon("icons/close.png"), "Exit", self)
        closeAction.setStatusTip("Exit Speech writer")
        closeAction.setShortcut("Ctrl+Q")
        closeAction.triggered.connect(self.Close)

        allAction = QAction(QIcon("icons/all.png"), "Select All", self)
        allAction.setStatusTip("Select all text in clipboard")
        allAction.setShortcut("Ctrl+A")
        allAction.triggered.connect(self.All)

        cutAction = QAction(QIcon("icons/cut.png"), "Cut to clipboard", self)
        cutAction.setStatusTip("Delete and copy text to clipboard")
        cutAction.setShortcut("Ctrl+X")
        cutAction.triggered.connect(self.Cut)

        copyAction = QAction(QIcon("icons/copy.png"), "Copy to clipboard", self)
        copyAction.setStatusTip("Copy text to clipboard")
        copyAction.setShortcut("Ctrl+C")
        copyAction.triggered.connect(self.Copy)

        pasteAction = QAction(QIcon("icons/paste.png"), "Paste from clipboard", self)
        pasteAction.setStatusTip("Paste text from clipboard")
        pasteAction.setShortcut("Ctrl+V")
        pasteAction.triggered.connect(self.Paste)

        undoAction = QAction(QIcon("icons/undo.png"), "Undo last action", self)
        undoAction.setStatusTip("Undo last action")
        undoAction.setShortcut("Ctrl+Z")
        undoAction.triggered.connect(self.Undo)

        redoAction = QAction(QIcon("icons/redo.png"), "Redo last undone thing", self)
        redoAction.setStatusTip("Redo last undone thing")
        redoAction.setShortcut("Ctrl+Y")
        redoAction.triggered.connect(self.Redo)

        printAction = QAction(QIcon("icons/print.png"), "Print document", self)
        printAction.setStatusTip("Print document")
        printAction.setShortcut("Ctrl+P")
        printAction.triggered.connect(self.Print)

        self.toolbar = self.addToolBar("Options")
        self.toolbar.addAction(recordAction)

        self.toolbar.addSeparator()

        self.toolbar.addAction(newAction)
        self.toolbar.addAction(openAction)
        self.toolbar.addAction(saveAction)
        self.toolbar.addAction(save_asAction)
        self.toolbar.addSeparator()

        self.toolbar.addAction(printAction)

        self.toolbar.addSeparator()

        self.toolbar.addAction(allAction)
        self.toolbar.addAction(cutAction)
        self.toolbar.addAction(copyAction)
        self.toolbar.addAction(pasteAction)
        self.toolbar.addAction(undoAction)
        self.toolbar.addAction(redoAction)

        self.toolbar.addSeparator()

        self.toolbar.addAction(aboutAction)
        self.toolbar.addAction(usergdAction)
        self.toolbar.addAction(updateAction)
        self.toolbar.addAction(feedbackAction)
        self.toolbar.addSeparator()

        self.addToolBarBreak()

        # Lower Toolbar

        self.fontFamily = QFontComboBox(self)
        self.fontFamily.currentFontChanged.connect(self.FontFamily)

        fontSize = QComboBox(self)
        fontSize.setEditable(True)
        fontSize.setMinimumContentsLength(3)
        fontSize.activated.connect(self.FontSize)
        flist = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 20, 22, 24, 26, 28, 32, 36, 40, 44, 48,
                 54, 60, 66, 72, 80, 88, 96]

        for i in flist:
            fontSize.addItem(str(i))

        fontColor = QAction("Change font color", self)
        fontColor.triggered.connect(self.FontColor)

        boldAction = QAction(QIcon("icons/bold.png"), "Bold", self)
        boldAction.setShortcut("Ctrl+B")
        boldAction.triggered.connect(self.Bold)

        italicAction = QAction(QIcon("icons/italic.png"), "Italic", self)
        italicAction.setShortcut("Ctrl+I")
        italicAction.triggered.connect(self.Italic)

        underlAction = QAction(QIcon("icons/undl.png"), "Underline", self)
        underlAction.setShortcut("Ctrl+U")
        underlAction.triggered.connect(self.Underl)

        #   Alignment

        rightAlign = QAction(QIcon("icons/right.png"), "Align Right", self)
        rightAlign.setShortcut("Ctrl+R")
        rightAlign.triggered.connect(self.rightAlign)

        centerAlign = QAction(QIcon("icons/center.png"), "Align Center", self)
        centerAlign.setShortcut("Ctrl+E")
        centerAlign.triggered.connect(self.centerAlign)

        justifyAlign = QAction(QIcon("icons/justify.png"), "Align Justify", self)
        justifyAlign.setShortcut("Ctrl+J")
        justifyAlign.triggered.connect(self.justifyAlign)

        leftAlign = QAction(QIcon("icons/left.png"), "Align Left", self)
        leftAlign.setShortcut("Ctrl+L")
        leftAlign.triggered.connect(self.leftAlign)

        insertBullets = QAction(QIcon("icons/checklist.png"), "Insert Bullet List", self)
        insertBullets.triggered.connect(self.insertBullet)

        insertNumber = QAction(QIcon("icons/num.png"), "insert Number List", self)
        insertNumber.triggered.connect(self.insertNumber)

        space1 = QLabel("  ", self)
        space2 = QLabel(" ", self)
        space3 = QLabel(" ", self)

        self.formatbar = self.addToolBar("Format")
        self.formatbar.addWidget(self.fontFamily)
        self.formatbar.addWidget(space1)
        self.formatbar.addWidget(fontSize)
        self.formatbar.addWidget(space2)

        self.formatbar.addSeparator()

        self.formatbar.addAction(fontColor)

        self.formatbar.addSeparator()

        self.formatbar.addAction(boldAction)
        self.formatbar.addAction(italicAction)
        self.formatbar.addAction(underlAction)

        self.formatbar.addSeparator()

        self.formatbar.addAction(rightAlign)
        self.formatbar.addAction(leftAlign)
        self.formatbar.addAction(centerAlign)
        self.formatbar.addAction(justifyAlign)

        self.formatbar.addSeparator()

        self.formatbar.addAction(insertNumber)
        self.formatbar.addAction(insertBullets)

        self.formatbar.addSeparator()

        self.formatbar.addSeparator()

                 # Text Edit

        self.text = QTextEdit(self)
        self.text.setTabStopWidth(12)
        self.setCentralWidget(self.text)

                      # Statusbar

        self.status = self.statusBar()

        self.text.cursorPositionChanged.connect(self.CursorPosition)

                           # Window settings
        self.setGeometry(100, 100, 1200, 900)
        self.setWindowTitle("STT EDITOR")
        self.setWindowIcon(QIcon("icons/logo2.png"))
        self.show()

                                    # Menubar

        menubar = self.menuBar()
        file = menubar.addMenu("File")
        edit = menubar.addMenu("Edit")
        formart = menubar.addMenu("Format")
        help = menubar.addMenu("Help")

        file.addAction(recordAction)
        file.addAction(newAction)
        file.addAction(openAction)
        file.addAction(saveAction)
        file.addAction(save_asAction)
        file.addAction(printAction)
        file.addAction(closeAction)

        edit.addAction(undoAction)
        edit.addAction(redoAction)
        edit.addAction(allAction)
        edit.addAction(cutAction)
        edit.addAction(copyAction)
        edit.addAction(pasteAction)

        help.addAction(aboutAction)
        help.addAction(usergdAction)
        help.addAction(updateAction)
        help.addAction(feedbackAction)

        formart.addAction(boldAction)
        formart.addAction(italicAction)
        formart.addAction(underlAction)
        formart.addAction(rightAlign)
        formart.addAction(leftAlign)
        formart.addAction(centerAlign)
        formart.addAction(justifyAlign)
        formart.addAction(insertBullets)
        formart.addAction(insertNumber)

                  # Toolbar slots

    def New(self):
        self.text.clear()

    def Record(self):
        pool = Pool(8)  # Number of concurrent threads

        with open('/home/shimuli/PycharmProjects/example/api-key.json') as f:
            GOOGLE_CLOUD_SPEECH_CREDENTIALS = f.read()

        r = sr.Recognizer()
        files = sorted(os.listdir('/home/shimuli/Desktop/parts/keep/'))

        def transcribe(data):
            idx, file = data
            name = '/home/shimuli/Desktop/parts/keep/' + file
            print(name + " started")
            # Load audio file
            with sr.AudioFile(name) as source:
                audio = r.record(source)
            # Transcribe audio file
            text = r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS)
            print(name + " done")
            return {
                "idx": idx,
                "text": text
            }

        all_text = pool.map(transcribe, enumerate(files))
        pool.close()
        pool.join()

        transcript = ""
        for t in sorted(all_text, key=lambda x: x['idx']):
            total_seconds = t['idx'] * 30
            # Cool shortcut from:
            # https://stackoverflow.com/questions/775049/python-time-seconds-to-hms
            # to get hours, minutes and seconds
            m, s = divmod(total_seconds, 60)
            h, m = divmod(m, 60)

            # Format time as h:m:s - 30 seconds of text
            transcript = transcript + "{:0>2d}:{:0>2d}:{:0>2d} {}\n".format(h, m, s, t['text'])

        print(transcript)

        with open("transcript.txt", "w") as f:
            self.text.setText(transcript)
        #self.text.clear()

        #with sr.AudioFile(sound2) as source:
            #sound2 = r.listen(source)
       # try:
            #text = r.recognize_google(sound2)
            #self.text.setText(text)
        #except Exception as e:
                #print("Network error")

    def Open(self):
        filename = QFileDialog.getOpenFileName(self, 'Open File')
        f = open(filename, 'r')
        filedata = f.read()
        self.text.setText(filedata)
        f.close()

    def Save_As(self):
        filename = QFileDialog.getSaveFileName(self, 'Save File', '/', '.txt')[0]
        f = open(filename, 'w')
        filedata = self.text.toPlainText()
        f.write(filedata)
        f.close()

    def Save(self):
        # Only open dialog if there is no filename yet
        #if not self.filename:
            #self.filename = QFileDialog.getSaveFileName(self, 'Save File')

        # Append extension if not there yet
        #if not self.filename.endswith(".writer"):
            #self.filename += ".writer"

        # We just store the contents of the text file along with the
        # format in html, which Qt does in a very nice way for us
        #with open(self.filename, "wt") as file:
            #file.write(self.text.toHtml())

        filename = self.text.toPlainText()
        with open('Recovered.doc', 'w') as f:
            f.write(filename)

    def PageView(self):
        preview = QtPrintSupport.QPrintPreviewDialog()
        preview.paintRequested.connect(self.PaintPageView)
        preview.exec_()

    def Print(self):
        dialog = QtPrintSupport.QPrintDialog()
        if dialog.exec_() == QDialog.Accepted:
            self.text.document().print_(dialog.printer())

    def PDF(self):
        printer = QtPrintSupport.QPrinter()
        printer.setOutputFormat(printer.NativeFormat)

        dialog = QtPrintSupport.QPrintDialog(printer)
        dialog.setOption(dialog.PrintToFile)
        if dialog.exec_() == QDialog.Accepted:
            self.text.document().print_(dialog.printer())

    def Close(self):
        sys.exit()

    def Undo(self):
        self.text.undo()

    def Redo(self):
        self.text.redo()

    def Cut(self):
        self.text.cut()

    def Copy(self):
        self.text.copy()

    def All(self):
        self.text.selectAll()

    def Paste(self):
        self.text.paste()

    def CursorPosition(self):
        line = self.text.textCursor().blockNumber()
        col = self.text.textCursor().columnNumber()
        linecol = ("Line: " + str(line) + " | " + "Column: " + str(col))
        self.status.showMessage(linecol)

    def FontFamily(self, font):
        font = QFont(self.fontFamily.currentFont())
        self.text.setCurrentFont(font)

    def FontSize(self, fsize):
        size = (int(fsize))
        self.text.setFontPointSize(size)

    def FontColor(self):
        c = QColorDialog.getColor()

        self.text.setTextColor(c)

    def Bold(self):
        w = self.text.fontWeight()
        if w == 50:
            self.text.setFontWeight(QFont.Bold)
        elif w == 75:
            self.text.setFontWeight(QFont.Normal)

    def Italic(self):
        i = self.text.fontItalic()

        if i == False:
            self.text.setFontItalic(True)
        elif i == True:
            self.text.setFontItalic(False)

    def Underl(self):
        ul = self.text.fontUnderline()

        if ul == False:
            self.text.setFontUnderline(True)
        elif ul == True:
            self.text.setFontUnderline(False)

    def rightAlign(self):
       self.text.setAlignment(Qt.AlignRight)

    def leftAlign(self):
        self.text.setAlignment(Qt.AlignLeft)

    def centerAlign(self):
        self.text.setAlignment(Qt.AlignCenter)

    def justifyAlign(self):
        self.text.setAlignment(Qt.AlignJustify)

    def insertBullet(self):
        self.text.insertHtml("<ul><li> .</li></ul>")

    def insertNumber(self):
        self.text.insertHtml("<ol><li>. </li></ol>")

    def About(self):
        msg = QMessageBox()

        msg.setIcon(QMessageBox.Information)
        #msg.setStyleSheet("QLabel{min-width:500 px; font-size: 14px;}")
        #msg.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        #msg.resize(100, 200)

        msg.setText("About")
        msg.setInformativeText("A modern, simple-to-use,open source product"
                               " suite for word processing, speech to text processing and normal editor operation.")
        msg.setWindowTitle("")
        msg.setDetailedText("Version: STT EDITOR(1.0.0)\n"
                            "Update: First version(1.0.0)\n"
                            "System Support: Linux and Windows\n"
                            "User Directory: /home/shimuli/PycharmPr\n"
                            "Copyright © 2018\n")
        msg.setStandardButtons(QMessageBox.Ok)

        retval = msg.exec_()

    def Guide(self):
        url = QtCore.QUrl("https://stt-editor.firebaseapp.com/")

        QDesktopServices.openUrl(url)

    def Update(self):
       reponse = QMessageBox.information(self, "Check for updates",
                                      "You are using the latest version STT EDITOR (1.0.0)",
                                      QMessageBox.Cancel)

    def Feedback(self):
        url = QtCore.QUrl("mailto:csmadegwa@student.mmust.ac.ke")

        QDesktopServices.openUrl(url)


def main():
    app = QApplication(sys.argv)
    main = Main()
    main.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()