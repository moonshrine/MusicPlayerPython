# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MPlayer.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MusicPlayer(object):
    def setupUi(self, MusicPlayer):
        MusicPlayer.setObjectName("MusicPlayer")
        MusicPlayer.resize(1206, 658)
        self.centralwidget = QtWidgets.QWidget(MusicPlayer)
        self.centralwidget.setObjectName("centralwidget")
        self.MusicPlayerFrame = QtWidgets.QFrame(self.centralwidget)
        self.MusicPlayerFrame.setGeometry(QtCore.QRect(0, 365, 391, 131))
        self.MusicPlayerFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MusicPlayerFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MusicPlayerFrame.setObjectName("MusicPlayerFrame")
        self.songSlider = QtWidgets.QSlider(self.MusicPlayerFrame)
        self.songSlider.setGeometry(QtCore.QRect(49, 10, 281, 20))
        self.songSlider.setOrientation(QtCore.Qt.Horizontal)
        self.songSlider.setObjectName("songSlider")
        self.songCurrentTime = QtWidgets.QLabel(self.MusicPlayerFrame)
        self.songCurrentTime.setGeometry(QtCore.QRect(20, 10, 31, 16))
        self.songCurrentTime.setObjectName("songCurrentTime")
        self.songTotalTime = QtWidgets.QLabel(self.MusicPlayerFrame)
        self.songTotalTime.setGeometry(QtCore.QRect(340, 10, 31, 16))
        self.songTotalTime.setObjectName("songTotalTime")
        self.groupBox = QtWidgets.QGroupBox(self.MusicPlayerFrame)
        self.groupBox.setGeometry(QtCore.QRect(30, 30, 341, 71))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 9, 341, 61))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.LeftButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.LeftButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../../Downloads/leftButton.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.LeftButton.setIcon(icon)
        self.LeftButton.setIconSize(QtCore.QSize(40, 40))
        self.LeftButton.setObjectName("LeftButton")
        self.gridLayout.addWidget(self.LeftButton, 0, 1, 1, 1)
        self.RightButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.RightButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../../../../Downloads/rightButton.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.RightButton.setIcon(icon1)
        self.RightButton.setIconSize(QtCore.QSize(40, 40))
        self.RightButton.setObjectName("RightButton")
        self.gridLayout.addWidget(self.RightButton, 0, 5, 1, 1)
        self.centerButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.centerButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../../../../../Downloads/playButton.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.centerButton.setIcon(icon2)
        self.centerButton.setIconSize(QtCore.QSize(50, 50))
        self.centerButton.setObjectName("centerButton")
        self.gridLayout.addWidget(self.centerButton, 0, 3, 1, 1)
        self.LeftButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.LeftButton_2.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../../../../../../Downloads/shuffleButton.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.LeftButton_2.setIcon(icon3)
        self.LeftButton_2.setIconSize(QtCore.QSize(40, 40))
        self.LeftButton_2.setObjectName("LeftButton_2")
        self.gridLayout.addWidget(self.LeftButton_2, 0, 0, 1, 1)
        self.RightButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.RightButton_2.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../../../../../../Downloads/repeatButton.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.RightButton_2.setIcon(icon4)
        self.RightButton_2.setIconSize(QtCore.QSize(40, 40))
        self.RightButton_2.setObjectName("RightButton_2")
        self.gridLayout.addWidget(self.RightButton_2, 0, 6, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 4, 1, 1)
        self.Speaker_icon = QtWidgets.QLabel(self.MusicPlayerFrame)
        self.Speaker_icon.setGeometry(QtCore.QRect(22, 105, 21, 20))
        self.Speaker_icon.setText("")
        self.Speaker_icon.setPixmap(QtGui.QPixmap("D:/sonu/MusicPlayerPython/AlbumIcons/SpeakerIcon.png"))
        self.Speaker_icon.setScaledContents(True)
        self.Speaker_icon.setObjectName("Speaker_icon")
        self.VolumeSlider = QtWidgets.QSlider(self.MusicPlayerFrame)
        self.VolumeSlider.setGeometry(QtCore.QRect(50, 108, 100, 15))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.VolumeSlider.sizePolicy().hasHeightForWidth())
        self.VolumeSlider.setSizePolicy(sizePolicy)
        self.VolumeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.VolumeSlider.setObjectName("VolumeSlider")
        self.LyricsButton = QtWidgets.QPushButton(self.MusicPlayerFrame)
        self.LyricsButton.setGeometry(QtCore.QRect(168, 105, 40, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.LyricsButton.setFont(font)
        self.LyricsButton.setObjectName("LyricsButton")
        self.MusicLibraryButton = QtWidgets.QPushButton(self.MusicPlayerFrame)
        self.MusicLibraryButton.setGeometry(QtCore.QRect(224, 103, 24, 24))
        self.MusicLibraryButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("D:/sonu/MusicPlayerPython/AlbumIcons/MusicLibraryIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MusicLibraryButton.setIcon(icon5)
        self.MusicLibraryButton.setObjectName("MusicLibraryButton")
        self.AlbumPhotoFrame = QtWidgets.QFrame(self.centralwidget)
        self.AlbumPhotoFrame.setGeometry(QtCore.QRect(0, 0, 391, 365))
        self.AlbumPhotoFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.AlbumPhotoFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.AlbumPhotoFrame.setObjectName("AlbumPhotoFrame")
        self.albumPhoto = QtWidgets.QLabel(self.AlbumPhotoFrame)
        self.albumPhoto.setGeometry(QtCore.QRect(36, 20, 321, 311))
        self.albumPhoto.setText("")
        self.albumPhoto.setPixmap(QtGui.QPixmap("../../../../../../Downloads/AIP6.png"))
        self.albumPhoto.setScaledContents(True)
        self.albumPhoto.setObjectName("albumPhoto")
        self.singerName = QtWidgets.QLabel(self.AlbumPhotoFrame)
        self.singerName.setGeometry(QtCore.QRect(39, 346, 241, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.singerName.setFont(font)
        self.singerName.setObjectName("singerName")
        self.songName = QtWidgets.QLabel(self.AlbumPhotoFrame)
        self.songName.setGeometry(QtCore.QRect(40, 330, 241, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.songName.setFont(font)
        self.songName.setObjectName("songName")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(400, 0, 391, 441))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_2.setGeometry(QtCore.QRect(9, 10, 371, 36))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.playlistName = QtWidgets.QLabel(self.groupBox_2)
        self.playlistName.setGeometry(QtCore.QRect(0, 0, 370, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playlistName.sizePolicy().hasHeightForWidth())
        self.playlistName.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.playlistName.setFont(font)
        self.playlistName.setAutoFillBackground(False)
        self.playlistName.setAlignment(QtCore.Qt.AlignCenter)
        self.playlistName.setObjectName("playlistName")
        self.playlistScrollArea = QtWidgets.QScrollArea(self.frame)
        self.playlistScrollArea.setGeometry(QtCore.QRect(0, 50, 391, 391))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playlistScrollArea.sizePolicy().hasHeightForWidth())
        self.playlistScrollArea.setSizePolicy(sizePolicy)
        self.playlistScrollArea.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.playlistScrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.playlistScrollArea.setLineWidth(1)
        self.playlistScrollArea.setWidgetResizable(True)
        self.playlistScrollArea.setAlignment(QtCore.Qt.AlignCenter)
        self.playlistScrollArea.setObjectName("playlistScrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 389, 389))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.playlistScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.SmallAlbumWidget = QtWidgets.QWidget(self.centralwidget)
        self.SmallAlbumWidget.setGeometry(QtCore.QRect(400, 439, 391, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SmallAlbumWidget.sizePolicy().hasHeightForWidth())
        self.SmallAlbumWidget.setSizePolicy(sizePolicy)
        self.SmallAlbumWidget.setMinimumSize(QtCore.QSize(350, 50))
        self.SmallAlbumWidget.setObjectName("SmallAlbumWidget")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.SmallAlbumWidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 10, 341, 52))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.BarAlbumIcon = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.BarAlbumIcon.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BarAlbumIcon.sizePolicy().hasHeightForWidth())
        self.BarAlbumIcon.setSizePolicy(sizePolicy)
        self.BarAlbumIcon.setMinimumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(1)
        self.BarAlbumIcon.setFont(font)
        self.BarAlbumIcon.setText("")
        self.BarAlbumIcon.setPixmap(QtGui.QPixmap("../../../../../../Downloads/AIP9.png"))
        self.BarAlbumIcon.setScaledContents(True)
        self.BarAlbumIcon.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.BarAlbumIcon.setWordWrap(False)
        self.BarAlbumIcon.setObjectName("BarAlbumIcon")
        self.horizontalLayout_3.addWidget(self.BarAlbumIcon)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.BarSongName = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BarSongName.sizePolicy().hasHeightForWidth())
        self.BarSongName.setSizePolicy(sizePolicy)
        self.BarSongName.setMinimumSize(QtCore.QSize(287, 12))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.BarSongName.setFont(font)
        self.BarSongName.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.BarSongName.setObjectName("BarSongName")
        self.verticalLayout_3.addWidget(self.BarSongName)
        self.BarArtistAlbumName = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BarArtistAlbumName.sizePolicy().hasHeightForWidth())
        self.BarArtistAlbumName.setSizePolicy(sizePolicy)
        self.BarArtistAlbumName.setMinimumSize(QtCore.QSize(287, 10))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.BarArtistAlbumName.setFont(font)
        self.BarArtistAlbumName.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.BarArtistAlbumName.setObjectName("BarArtistAlbumName")
        self.verticalLayout_3.addWidget(self.BarArtistAlbumName)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.SmallPlayButton = QtWidgets.QPushButton(self.SmallAlbumWidget)
        self.SmallPlayButton.setGeometry(QtCore.QRect(340, 10, 51, 51))
        self.SmallPlayButton.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("D:/sonu/MusicPlayerPython/AlbumIcons/smallPlayButton.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SmallPlayButton.setIcon(icon6)
        self.SmallPlayButton.setIconSize(QtCore.QSize(50, 50))
        self.SmallPlayButton.setDefault(False)
        self.SmallPlayButton.setFlat(False)
        self.SmallPlayButton.setObjectName("SmallPlayButton")
        self.SongBar = QtWidgets.QProgressBar(self.SmallAlbumWidget)
        self.SongBar.setGeometry(QtCore.QRect(0, 4, 391, 6))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SongBar.sizePolicy().hasHeightForWidth())
        self.SongBar.setSizePolicy(sizePolicy)
        self.SongBar.setMinimumSize(QtCore.QSize(285, 5))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(1)
        font.setKerning(True)
        self.SongBar.setFont(font)
        self.SongBar.setProperty("value", 45)
        self.SongBar.setTextVisible(False)
        self.SongBar.setFormat("%p%")
        self.SongBar.setObjectName("SongBar")
        self.LyricsFrame = QtWidgets.QFrame(self.centralwidget)
        self.LyricsFrame.setGeometry(QtCore.QRect(860, 60, 321, 311))
        self.LyricsFrame.setStyleSheet("background-color: rgba(157, 157, 157, 83);")
        self.LyricsFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LyricsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LyricsFrame.setObjectName("LyricsFrame")
        self.LyricsLabel = QtWidgets.QLabel(self.LyricsFrame)
        self.LyricsLabel.setGeometry(QtCore.QRect(50, 130, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.LyricsLabel.setFont(font)
        self.LyricsLabel.setStyleSheet("background-color: rgba(157, 157, 157, 0);\n"
"color: rgb(77, 77, 77);")
        self.LyricsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.LyricsLabel.setObjectName("LyricsLabel")
        self.DefaultSongWidget = QtWidgets.QWidget(self.centralwidget)
        self.DefaultSongWidget.setGeometry(QtCore.QRect(30, 520, 354, 64))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DefaultSongWidget.sizePolicy().hasHeightForWidth())
        self.DefaultSongWidget.setSizePolicy(sizePolicy)
        self.DefaultSongWidget.setMinimumSize(QtCore.QSize(350, 50))
        self.DefaultSongWidget.setStyleSheet("background-color: rgb(181, 255, 251);")
        self.DefaultSongWidget.setObjectName("DefaultSongWidget")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.DefaultSongWidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(0, 0, 354, 64))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.albumIcon_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.albumIcon_4.sizePolicy().hasHeightForWidth())
        self.albumIcon_4.setSizePolicy(sizePolicy)
        self.albumIcon_4.setMinimumSize(QtCore.QSize(50, 50))
        self.albumIcon_4.setText("")
        self.albumIcon_4.setPixmap(QtGui.QPixmap("../../../../../../Downloads/AIP9.png"))
        self.albumIcon_4.setScaledContents(True)
        self.albumIcon_4.setAlignment(QtCore.Qt.AlignCenter)
        self.albumIcon_4.setWordWrap(False)
        self.albumIcon_4.setObjectName("albumIcon_4")
        self.horizontalLayout_5.addWidget(self.albumIcon_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.songName_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.songName_5.sizePolicy().hasHeightForWidth())
        self.songName_5.setSizePolicy(sizePolicy)
        self.songName_5.setMinimumSize(QtCore.QSize(300, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.songName_5.setFont(font)
        self.songName_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.songName_5.setObjectName("songName_5")
        self.verticalLayout_5.addWidget(self.songName_5)
        self.singer = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.singer.sizePolicy().hasHeightForWidth())
        self.singer.setSizePolicy(sizePolicy)
        self.singer.setMinimumSize(QtCore.QSize(300, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.singer.setFont(font)
        self.singer.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.singer.setObjectName("singer")
        self.verticalLayout_5.addWidget(self.singer)
        self.horizontalLayout_5.addLayout(self.verticalLayout_5)
        MusicPlayer.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MusicPlayer)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1206, 21))
        self.menubar.setObjectName("menubar")
        MusicPlayer.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MusicPlayer)
        self.statusbar.setObjectName("statusbar")
        MusicPlayer.setStatusBar(self.statusbar)

        self.retranslateUi(MusicPlayer)
        QtCore.QMetaObject.connectSlotsByName(MusicPlayer)

    def retranslateUi(self, MusicPlayer):
        _translate = QtCore.QCoreApplication.translate
        MusicPlayer.setWindowTitle(_translate("MusicPlayer", "MainWindow"))
        self.songCurrentTime.setText(_translate("MusicPlayer", "--:--"))
        self.songTotalTime.setText(_translate("MusicPlayer", "--:--"))
        self.LyricsButton.setText(_translate("MusicPlayer", "Lyrics"))
        self.singerName.setText(_translate("MusicPlayer", "Niall Horan"))
        self.songName.setText(_translate("MusicPlayer", "No Judgement"))
        self.playlistName.setText(_translate("MusicPlayer", "Playlist Name"))
        self.BarSongName.setText(_translate("MusicPlayer", "Nice To Meet Ya"))
        self.BarArtistAlbumName.setText(_translate("MusicPlayer", "TextLabel"))
        self.LyricsLabel.setText(_translate("MusicPlayer", "TextLabel"))
        self.songName_5.setText(_translate("MusicPlayer", "Nice To Meet Ya"))
        self.singer.setText(_translate("MusicPlayer", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MusicPlayer = QtWidgets.QMainWindow()
    ui = Ui_MusicPlayer()
    ui.setupUi(MusicPlayer)
    MusicPlayer.show()
    sys.exit(app.exec_())
