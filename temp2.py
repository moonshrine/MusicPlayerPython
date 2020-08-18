from PyQt5 import QtCore, QtGui, QtWidgets
import os, csv, pygame, threading, time, sys
from mutagen.mp3 import MP3, EasyMP3
from mutagen.id3 import ID3
from io import BytesIO
from PIL import Image
from PIL.ImageQt import ImageQt
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent


class songWidgetClass(QtWidgets.QWidget):
    songClicked = QtCore.pyqtSignal()

    def mousePressEvent(self, event):
        Ui_MusicPlayer.current_song_index = self.index
        self.songClicked.emit()
        QtWidgets.QWidget.mousePressEvent(self, event)
        #change color of widget when selected
        #setStyleSheet("background-color: rgb(181, 255, 251);")
        #print(self.singer_name)
        #Ui_MusicPlayer.songClickedPlay(self)
        #print(Ui_MusicPlayer.currentSongIndex)

class smallMPlayerClass(QtWidgets.QWidget):
    playerClicked = QtCore.pyqtSignal()

    def mousePressEvent(self, event):
        self.playerClicked.emit()
        QtWidgets.QWidget.mousePressEvent(self,event)
        print("Small Music Player Clicked ")

class Ui_MusicPlayer(object):
    icon_path = "D:/sonu/MusicPlayerPython/AlbumIcons"
    song_path = "D:/sonu/MusicPlayerPython/Songs"
    current_song_index = 0

    def setupUi(self, MusicPlayer):

        self.play_button_active = True
        self.songSliderPressed = False  #set True when slider is in foucs/ pressed
        self.mainPlayerEnabled = False

        #initialize pygame mixer
        #pygame.mixer.init(48000, -16, 2, 2048)  # Bit rate of song - find it using audacity

        MusicPlayer.setObjectName("MusicPlayer")
        MusicPlayer.resize(820, 531)

        self.centralwidget = QtWidgets.QWidget(MusicPlayer)
        self.centralwidget.setObjectName("centralwidget")
        self.MusicPlayerFrame = QtWidgets.QFrame(self.centralwidget)
        self.MusicPlayerFrame.setGeometry(QtCore.QRect(0, 365, 391, 131))
        self.MusicPlayerFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MusicPlayerFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MusicPlayerFrame.setObjectName("MusicPlayerFrame")
        self.songSlider = QtWidgets.QSlider(self.MusicPlayerFrame)
        self.songSlider.setGeometry(QtCore.QRect(53, 10, 281, 20))
        self.songSlider.setOrientation(QtCore.Qt.Horizontal)
        self.songSlider.setObjectName("songSlider")

        self.songSlider.sliderMoved.connect(self.setSeekingPosition)    #if slider manually moved / seek moved

        self.songCurrentTime = QtWidgets.QLabel(self.MusicPlayerFrame)
        self.songCurrentTime.setGeometry(QtCore.QRect(20, 10, 31, 16))
        self.songCurrentTime.setObjectName("songCurrentTime")
        self.songTotalTime = QtWidgets.QLabel(self.MusicPlayerFrame)
        self.songTotalTime.setGeometry(QtCore.QRect(340, 10, 31, 16))
        self.songTotalTime.setObjectName("songTotalTime")
        self.groupBox = QtWidgets.QGroupBox(self.MusicPlayerFrame)
        self.groupBox.setGeometry(QtCore.QRect(20, 30, 341, 71))
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
        icon.addPixmap(QtGui.QPixmap(Ui_MusicPlayer.icon_path +"/leftButton.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.LeftButton.setIcon(icon)
        self.LeftButton.setIconSize(QtCore.QSize(40, 40))
        self.LeftButton.setObjectName("LeftButton")

        self.LeftButton.clicked.connect(self.leftButtonPressed) #bind to method on button press

        self.gridLayout.addWidget(self.LeftButton, 0, 1, 1, 1)
        self.RightButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.RightButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(Ui_MusicPlayer.icon_path +"/rightButton.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.RightButton.setIcon(icon1)
        self.RightButton.setIconSize(QtCore.QSize(40, 40))
        self.RightButton.setObjectName("RightButton")

        self.RightButton.clicked.connect(self.rightButtonPressed)   # bind to method on button press

        self.gridLayout.addWidget(self.RightButton, 0, 5, 1, 1)
        self.centerButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.centerButton.setText("")

        #save play and pasue button icons for future use
        self.play_icon = QtGui.QIcon()
        self.play_icon.addPixmap(QtGui.QPixmap(Ui_MusicPlayer.icon_path + "/playButton.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pause_icon = QtGui.QIcon()
        self.pause_icon.addPixmap(QtGui.QPixmap(Ui_MusicPlayer.icon_path + "/pauseButton.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.centerButton.setIcon(self.play_icon)
        self.centerButton.setIconSize(QtCore.QSize(50, 50))
        self.centerButton.setObjectName("centerButton")
        self.centerButton.clicked.connect(self.centerButtonPressed) #Bind method to on press button

        self.gridLayout.addWidget(self.centerButton, 0, 3, 1, 1)
        self.shuffleButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.shuffleButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(Ui_MusicPlayer.icon_path +"/shuffleButton.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.shuffleButton.setIcon(icon3)
        self.shuffleButton.setIconSize(QtCore.QSize(40, 40))
        self.shuffleButton.setObjectName("shuffleButton")


        self.gridLayout.addWidget(self.shuffleButton, 0, 0, 1, 1)
        self.repeatButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.repeatButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(Ui_MusicPlayer.icon_path +"/repeatButton.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.repeatButton.setIcon(icon4)
        self.repeatButton.setIconSize(QtCore.QSize(40, 40))
        self.repeatButton.setObjectName("repeatButton")

        self.gridLayout.addWidget(self.repeatButton, 0, 6, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 4, 1, 1)
        
        Speaker_icon = QtWidgets.QLabel(self.MusicPlayerFrame)
        Speaker_icon.setGeometry(QtCore.QRect(22, 105, 21, 20))
        Speaker_icon.setText("")
        Speaker_icon.setPixmap(QtGui.QPixmap("D:/sonu/MusicPlayerPython/AlbumIcons/SpeakerIcon.png"))
        Speaker_icon.setScaledContents(True)
        Speaker_icon.setObjectName("Speaker_icon")
        self.VolumeSlider = QtWidgets.QSlider(self.MusicPlayerFrame)
        self.VolumeSlider.setGeometry(QtCore.QRect(50, 108, 100, 15))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.VolumeSlider.sizePolicy().hasHeightForWidth())
        self.VolumeSlider.setSizePolicy(sizePolicy)
        self.VolumeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.VolumeSlider.setObjectName("VolumeSlider")

        self.VolumeSlider.sliderMoved.connect(self.changeVolume)  # connect to change volume method to update 
        self.VolumeSlider.setValue(99)  # set default volume of song and postion of slider
        #self.changeVolume(100)

        self.LyricsButton = QtWidgets.QPushButton(self.MusicPlayerFrame)
        self.LyricsButton.setGeometry(QtCore.QRect(168, 105, 40, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.LyricsButton.setFont(font)
        self.LyricsButton.setObjectName("LyricsButton")
        self.LyricsButton.setText('Lyrics')
        self.MusicLibraryButton = QtWidgets.QPushButton(self.MusicPlayerFrame)
        self.MusicLibraryButton.setGeometry(QtCore.QRect(224, 103, 24, 24))
        self.MusicLibraryButton.setText("")
        self.MusicLibraryButton.clicked.connect(self.controlFrames)
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

        self.albumPhoto.setPixmap(QtGui.QPixmap( Ui_MusicPlayer.icon_path+"/DefaultCover.jpg"))
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
        self.frame.setGeometry(QtCore.QRect(0, 0, 391, 441))
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
        self.playlistScrollArea.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.playlistScrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.playlistScrollArea.setLineWidth(1)
        self.playlistScrollArea.setWidgetResizable(True)
        self.playlistScrollArea.setObjectName("playlistScrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 379, 329))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")

        #small song bar window
        self.SmallAlbumWidget = smallMPlayerClass(self.centralwidget)

        #On clicked event for small widget
        self.SmallAlbumWidget.playerClicked.connect(self.controlFrames)

        self.SmallAlbumWidget.setGeometry(QtCore.QRect(0, 439, 391, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SmallAlbumWidget.sizePolicy().hasHeightForWidth())
        self.SmallAlbumWidget.setSizePolicy(sizePolicy)
        self.SmallAlbumWidget.setMinimumSize(QtCore.QSize(350, 50))
        self.SmallAlbumWidget.setObjectName("SmallAlbumWidget")
        horizontalLayoutWidget_2 = QtWidgets.QWidget(self.SmallAlbumWidget)
        horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 10, 341, 52))
        horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        horizontalLayout_3 = QtWidgets.QHBoxLayout(horizontalLayoutWidget_2)
        horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        horizontalLayout_3.setSpacing(0)
        horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.BarAlbumIcon = QtWidgets.QLabel(horizontalLayoutWidget_2)
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
        self.BarAlbumIcon.setPixmap(QtGui.QPixmap(Ui_MusicPlayer.icon_path + "/NineTrackMind.jpg"))
        self.BarAlbumIcon.setScaledContents(True)
        self.BarAlbumIcon.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.BarAlbumIcon.setWordWrap(False)
        self.BarAlbumIcon.setObjectName("BarAlbumIcon")
        horizontalLayout_3.addWidget(self.BarAlbumIcon)
        verticalLayout_3 = QtWidgets.QVBoxLayout()
        verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        verticalLayout_3.setSpacing(0)
        verticalLayout_3.setObjectName("verticalLayout_3")
        self.BarSongName = QtWidgets.QLabel(horizontalLayoutWidget_2)
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
        verticalLayout_3.addWidget(self.BarSongName)
        self.BarArtistAlbumName = QtWidgets.QLabel(horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BarArtistAlbumName.sizePolicy().hasHeightForWidth())
        self.BarArtistAlbumName.setSizePolicy(sizePolicy)
        self.BarArtistAlbumName.setMinimumSize(QtCore.QSize(287, 10))
        self.BarArtistAlbumName.setText('Flicker')
        self.BarSongName.setText('Slow Hands')
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.BarArtistAlbumName.setFont(font)
        self.BarArtistAlbumName.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.BarArtistAlbumName.setObjectName("BarArtistAlbumName")
        verticalLayout_3.addWidget(self.BarArtistAlbumName)
        horizontalLayout_3.addLayout(verticalLayout_3)
        self.SmallPlayButton = QtWidgets.QPushButton(self.SmallAlbumWidget)
        self.SmallPlayButton.setGeometry(QtCore.QRect(340, 10, 51, 51))
        self.SmallPlayButton.setText("")
        
        #smaller icons for play and pasue button
        self.smallPlayIcon = QtGui.QIcon()
        self.smallPlayIcon.addPixmap(QtGui.QPixmap(Ui_MusicPlayer.icon_path+"/smallPlayButton.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.smallPauseIcon = QtGui.QIcon()
        self.smallPauseIcon.addPixmap(QtGui.QPixmap(Ui_MusicPlayer.icon_path+"/smallPauseButton.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.SmallPlayButton.setIcon(self.smallPlayIcon)
        self.SmallPlayButton.setIconSize(QtCore.QSize(50, 50))
        self.SmallPlayButton.setDefault(False)
        self.SmallPlayButton.setFlat(False)
        self.SmallPlayButton.setObjectName("SmallPlayButton")

        #connect to slot on click of small play/pause button
        self.SmallPlayButton.clicked.connect(self.centerButtonPressed)

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
        self.SongBar.setProperty("value", 45)   # set or update value of song bar
        self.SongBar.setTextVisible(False)
        self.SongBar.setFormat("%p%")
        self.SongBar.setObjectName("SongBar")

        #*********------------
        
        #Add Lyrics frame or window
        self.LyricsFrame = QtWidgets.QFrame(self.centralwidget)
        self.LyricsFrame.setGeometry(QtCore.QRect(440, 60, 321, 311))
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
        self.LyricsLabel.setText('Meant To Be , me')

        #********--------------


        self.playlistScrollArea.setWidget(self.scrollAreaWidgetContents)
        MusicPlayer.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MusicPlayer)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 820, 21))
        self.menubar.setObjectName("menubar")
        MusicPlayer.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MusicPlayer)
        self.statusbar.setObjectName("statusbar")
        MusicPlayer.setStatusBar(self.statusbar)

        self.retranslateUi(MusicPlayer)
        QtCore.QMetaObject.connectSlotsByName(MusicPlayer)

        self.song_list = []

        #Reading Song from folder/ Directory and adding them to playlist
        self.traverseSongFromFolder("D:/sonu/MusicPlayerPython/Songs")

        #create media player
        self.mediaPlayer = QMediaPlayer()

        #media player signals
        self.mediaPlayer.stateChanged.connect(self.mediaStateChanged)
        self.mediaPlayer.positionChanged.connect(self.mediaPositionChanged)
        self.mediaPlayer.durationChanged.connect(self.mediaDurationChanged)

        self.MusicPlayerFrame.hide()
        self.AlbumPhotoFrame.hide()

        #open explorer widnow to select music
        #fileChoosen = QtWidgets.QFileDialog.getOpenFileUrl(None,'Open Music File', os.path.expanduser('~'),'Audio (*.mp3 *.ogg *.wav)','*.mp3 *.ogg *.wav')


    def retranslateUi(self, MusicPlayer):
        _translate = QtCore.QCoreApplication.translate
        MusicPlayer.setWindowTitle(_translate("MusicPlayer", "MainWindow"))
        self.songCurrentTime.setText(_translate("MusicPlayer", "--:--"))
        #self.songTotalTime.setText(_translate("MusicPlayer", "--:--"))
        #self.singerName.setText(_translate("MusicPlayer", "Niall Horan"))
        #self.songName.setText(_translate("MusicPlayer", "No Judgement"))
        self.playlistName.setText(_translate("MusicPlayer", "Playlist Name"))
        #self.songName_2.setText(_translate("MusicPlayer", "Nice To Meet Ya"))
        #self.label_2.setText(_translate("MusicPlayer", "TextLabel"))


    def song_widget(self, index, ipsong_name, ipsinger_name, ipalbum_icon):

        widget = songWidgetClass(self.scrollAreaWidgetContents)

        widget.songClicked.connect(self.songClickedPlay)  #On mouse press event call
        widget.song_name = ipsong_name
        widget.singer_name = ipsinger_name
        widget.album_icon = ipalbum_icon
        widget.index = index


        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(widget.sizePolicy().hasHeightForWidth())
        widget.setSizePolicy(sizePolicy)
        widget.setMinimumSize(QtCore.QSize(354, 50))
        widget.setObjectName("widget")
        horizontalLayoutWidget = QtWidgets.QWidget(widget)
        horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 360, 50))
        horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        horizontalLayout_2 = QtWidgets.QHBoxLayout(horizontalLayoutWidget)
        horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        horizontalLayout_2.setSpacing(0)
        horizontalLayout_2.setObjectName("horizontalLayout_2")
        album_icon = QtWidgets.QLabel(horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(album_icon.sizePolicy().hasHeightForWidth())
        album_icon.setSizePolicy(sizePolicy)
        album_icon.setMinimumSize(QtCore.QSize(50, 50))
        album_icon.setText("")
        album_icon.setPixmap(QtGui.QPixmap.fromImage(ipalbum_icon))
        album_icon.setScaledContents(True)
        album_icon.setAlignment(QtCore.Qt.AlignCenter)
        album_icon.setWordWrap(False)
        album_icon.setObjectName("albumIcon")
        horizontalLayout_2.addWidget(album_icon)
        verticalLayout_2 = QtWidgets.QVBoxLayout()
        verticalLayout_2.setSpacing(0)
        verticalLayout_2.setObjectName("verticalLayout_2")
        song_name = QtWidgets.QLabel(horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(song_name.sizePolicy().hasHeightForWidth())
        song_name.setSizePolicy(sizePolicy)
        song_name.setMinimumSize(QtCore.QSize(310, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        song_name.setFont(font)
        song_name.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        song_name.setObjectName("song_name")
        verticalLayout_2.addWidget(song_name)
        singer_name = QtWidgets.QLabel(horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(singer_name.sizePolicy().hasHeightForWidth())
        singer_name.setSizePolicy(sizePolicy)
        singer_name.setMinimumSize(QtCore.QSize(300, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        singer_name.setFont(font)
        singer_name.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        singer_name.setObjectName("singer_name")
        verticalLayout_2.addWidget(singer_name)
        horizontalLayout_2.addLayout(verticalLayout_2)
        self.verticalLayout.addWidget(widget)

        #Set texts 
        singer_name.setText(ipsinger_name)
        song_name.setText(ipsong_name)

    def songClickedPlay(self):
        print(Ui_MusicPlayer.current_song_index)
        self.playSong()

    def controlFrames(self):
        if self.mainPlayerEnabled:
            self.MusicPlayerFrame.hide()
            self.AlbumPhotoFrame.hide()
            
            self.SmallAlbumWidget.show()
            self.frame.show()
        else:
            self.MusicPlayerFrame.show()
            self.AlbumPhotoFrame.show()

            self.SmallAlbumWidget.hide()
            self.frame.hide()
        self.mainPlayerEnabled = not self.mainPlayerEnabled

    def traverseSongFromFolder(self, folder_path):  
        #Traverse songs from folder
        #if they are mp3 files then add them to list
        # extract artist name, album cover and all other tags from mp3 file  
        #then add them to scroll area
        cnt = 0
        for file in os.listdir(folder_path):
            if file.endswith('.mp3'):
                #file, waste = file.split('.')
                self.song_list.append(file)
                song_name, artist_name, album_icon = self.extractTagsFromSong(file)
                #print(song_name, artist_name)
                self.song_widget(len(self.song_list)-1, song_name, artist_name, album_icon)
                cnt += 1
        print(cnt,' songs added to the list')


    def extractTagsFromSong(self, song_name):   #send song name only, file path is in song_path variable
        # send song_name parameter with .mp3 extension
        # extract cover image using ID3 APIC tag then
        #convert that binary data to bytes and open as image
        #then convert that using ImageQt for use in PyQt5
        #also extract tags from mp3 file
        try:
            audio = ID3(Ui_MusicPlayer.song_path + '/'+ song_name)
            x = audio.get('APIC:').data
            im = Image.open(BytesIO(x))
            #print('image size:',im.size)
            im2 = ImageQt(im)
            #self.albumPhoto.setPixmap(QtGui.QPixmap.fromImage(im2))
        except:
            print('Error while extarcting image/ No Cover image')
            im2 = Image.open(Ui_MusicPlayer.icon_path + '/DefaultCover.jpg')

        tags = EasyMP3(Ui_MusicPlayer.song_path + '/'+ song_name)
        song_name, waste = song_name.split('.')
        if 'albumartist' in tags:
            artist_name = tags['albumartist']
        else:
            artist_name = 'Unknown'

        return song_name, artist_name[0], im2  # return song name without extension, artist name and cover photo


    def centerButtonPressed(self):

        if not self.play_button_active:
            self.centerButton.setIcon(self.play_icon)
            self.SmallPlayButton.setIcon(self.smallPlayIcon)
            self.playHandler()
            self.play_button_active = not self.play_button_active
        else:
            self.centerButton.setIcon(self.pause_icon)
            self.SmallPlayButton.setIcon(self.smallPauseIcon)
            self.pauseHandler()
            self.play_button_active = not self.play_button_active


    def rightButtonPressed(self):
        if Ui_MusicPlayer.current_song_index <len(self.song_list)-1:
            Ui_MusicPlayer.current_song_index += 1
            self.playSong()


    def leftButtonPressed(self):
        if Ui_MusicPlayer.current_song_index > 0:
            Ui_MusicPlayer.current_song_index -= 1
            self.playSong()

    def mediaPositionChanged(self, value):
        self.songSlider.setValue(value)

        currentSeconds = value     # in miliseconds
        currentSeconds /= 1000
        currentMins = int(currentSeconds//60)
        currentSeconds = int(currentSeconds%60)
        self.songCurrentTime.setText(str(currentMins).zfill(2) +':'+ str(currentSeconds).zfill(2))

        barPercentage = 0
        if value!= 0:
            barPercentage = value/self.mediaPlayer.duration()
            barPercentage *= 100
        self.SongBar.setValue(barPercentage)

    def mediaDurationChanged(self, duration):
        self.songSlider.setRange(0, duration)

        totalSeconds = duration     # in miliseconds
        totalSeconds /= 1000
        totalMins = int(totalSeconds//60)
        totalSeconds = int(totalSeconds%60)
        print('Duration',totalMins , ':', totalSeconds)
        self.songTotalTime.setText(str(totalMins).zfill(2) +':'+ str(totalSeconds).zfill(2))

    def mediaStateChanged(self):
        print('Media state changed')

    def setSeekingPosition(self, position):
        self.mediaPlayer.setPosition(position)

    def changeVolume(self, vol):
        self.mediaPlayer.setVolume(vol)
        #print('Volume changed to',vol)


    def playHandler(self):
        if self.mediaPlayer.state() == QMediaPlayer.StoppedState:
            print('stopped state')
            if self.mediaPlayer.mediaStatus() == QMediaPlayer.NoMedia:
                print('player has no media to play')
                self.playSong()
                pass
            elif self.mediaPlayer.mediaStatus() == QMediaPlayer.LoadedMedia:
                self.mediaPlayer.play()
            elif self.mediaPlayer.mediaStatus() == QMediaPlayer.BufferedMedia:
                self.mediaPlayer.play()
        elif self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            pass
        elif self.mediaPlayer.state() == QMediaPlayer.PausedState:
            self.mediaPlayer.play()

    def pauseHandler(self):
        self.mediaPlayer.pause()

    def playSong(self):
        #print(Ui_MusicPlayer.current_song_index)
        self.centerButton.setIcon(self.play_icon)
        self.SmallPlayButton.setIcon(self.smallPlayIcon)
        self.play_button_active = True

        self.mediaPlayer.stop()

        song_filename = self.song_list[Ui_MusicPlayer.current_song_index]
        song_name, singer_name, album_icon = self.extractTagsFromSong(song_filename)    #song_name without extension

        song_filename = Ui_MusicPlayer.song_path +'/'+ song_filename
        

        #AlbumPhotoFrame updates
        self.albumPhoto.setPixmap(QtGui.QPixmap.fromImage(album_icon))
        self.BarAlbumIcon.setPixmap(QtGui.QPixmap.fromImage(album_icon))

        #update total song time in window
        self.songName.setText(song_name)
        self.BarSongName.setText(song_name)

        #change artist/singer and album name
        self.singerName.setText(singer_name)
        self.BarArtistAlbumName.setText(singer_name)

        self.mediaPlayer.setMedia(QMediaContent(QtCore.QUrl.fromLocalFile(song_filename)))
        self.mediaPlayer.play()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    #app.aboutToQuit.connect(Ui_MusicPlayer.quitMusic )  # stop music on different thread
    
    MusicPlayer = QtWidgets.QMainWindow()
    ui = Ui_MusicPlayer()
    ui.setupUi(MusicPlayer)
    MusicPlayer.show()
    sys.exit(app.exec_())

