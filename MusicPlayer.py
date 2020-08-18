
#animation for frame 


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPropertyAnimation, QRect
import pygame, time, threading

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(364, 371)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MusicPlayerFrame = QtWidgets.QFrame(self.centralwidget)
        self.MusicPlayerFrame.setGeometry(QtCore.QRect(10, 10, 311, 281))
        self.MusicPlayerFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MusicPlayerFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MusicPlayerFrame.setObjectName("MusicPlayerFrame")
        self.AlbumPhoto = QtWidgets.QGraphicsView(self.MusicPlayerFrame)
        self.AlbumPhoto.setGeometry(QtCore.QRect(40, 10, 231, 192))
        self.AlbumPhoto.setObjectName("AlbumPhoto")
        self.songSlider = QtWidgets.QSlider(self.MusicPlayerFrame)
        self.songSlider.setGeometry(QtCore.QRect(39, 210, 231, 20))
        self.songSlider.setOrientation(QtCore.Qt.Horizontal)
        self.songSlider.setObjectName("songSlider")
        self.centerButton = QtWidgets.QPushButton(self.MusicPlayerFrame)
        self.centerButton.setGeometry(QtCore.QRect(140, 240, 31, 31))
        self.centerButton.setObjectName("centerButton")
        self.LeftButton = QtWidgets.QPushButton(self.MusicPlayerFrame)
        self.LeftButton.setGeometry(QtCore.QRect(80, 240, 31, 31))
        self.LeftButton.setObjectName("LeftButton")
        self.RightButton = QtWidgets.QPushButton(self.MusicPlayerFrame)
        self.RightButton.setGeometry(QtCore.QRect(200, 240, 31, 31))
        self.RightButton.setObjectName("RightButton")
        self.songCurrentTime = QtWidgets.QLabel(self.MusicPlayerFrame)
        self.songCurrentTime.setGeometry(QtCore.QRect(10, 210, 31, 16))
        self.songCurrentTime.setObjectName("songCurrentTime")
        self.songTotalTime = QtWidgets.QLabel(self.MusicPlayerFrame)
        self.songTotalTime.setGeometry(QtCore.QRect(280, 210, 31, 16))
        self.songTotalTime.setObjectName("songTotalTime")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 364, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.centerButton.clicked.connect(self.animateFrame)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.centerButton.setText(_translate("MainWindow", "||"))
        self.LeftButton.setText(_translate("MainWindow", "<<"))
        self.RightButton.setText(_translate("MainWindow", ">>"))
        self.songCurrentTime.setText(_translate("MainWindow", "--:--"))
        self.songTotalTime.setText(_translate("MainWindow", "--:--"))

    def playSong(self):
        pygame.mixer.init(48000)
        pygame.mixer.music.load('CakeByOcean.mp3')
        pygame.mixer.music.play()

    def sleeptime(self):
        time.sleep(1)
        self.MusicPlayerFrame.hide()
        time.sleep(1)
        self.MusicPlayerFrame.show()

    def animateFrame(self):

        self.anim = QPropertyAnimation(self.MusicPlayerFrame, b"geometry")
        self.anim.setDuration(1000)     #time in miliseconds
        self.anim.setStartValue(QRect(0, 0, 311, 281))
        self.anim.setEndValue(QRect(0, 900, 500, 500))
        self.anim.start()
        threading.Thread(target = self.sleeptime).start()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
