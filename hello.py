from tkinter import *
from PIL import Image, ImageTk
import pygame, time
import random
import threading
from mutagen.mp3 import MP3

class Song:
    def __init__(self, artistName, songName, albumName, albumPhoto):
        self.artistName = artistName
        self.songName = songName
        self.albumName = albumName
        self.albumPhoto = albumPhoto



class MusicPlayer:

    def __init__(self, master, song_list):      # constructor
        
        self.songList = song_list
        self.currentSongIndex = 0

        pygame.mixer.init(48000)  # Bit rate of song - find it using audacity

        playerFrame = Frame(master)
        playerFrame.pack()
        # load Image
        render = ImageTk.PhotoImage(file="E:/Users/sonu/Downloads/AIP4.png")# use '/' insted of '\' 
        #create Label
        albumPhoto = Label(playerFrame, image = render, height = 400, width = 500)
        albumPhoto.image = render
        albumPhoto.grid(row = 0, column = 0, columnspan = 5)

        self.songCurrentTime = Label(playerFrame, text = '--:--', justify = 'center', width = 5)
        self.songCurrentTime.grid(row = 1, column = 0)

        self.songSlider = Scale(playerFrame, from_ = 0, to = 40, sliderlength = 5,   
                                showvalue = 0, length = 409, orient = HORIZONTAL)
        self.songSlider.grid(row = 1, column = 1, columnspan = 3, sticky = W+E)
        self.songSlider.bind("<Enter>", self.sliderInFocus)
        
        self.songTotalTime = Label(playerFrame, text = '--:--', justify = 'center', width = 5)
        self.songTotalTime.grid(row = 1, column = 4)

        self.shuffleButton = Button(playerFrame, text = 'x')
        self.shuffleButton.grid(row = 2, column = 0)

        leftImg = ImageTk.PhotoImage(file="E:/Users/sonu/Downloads/leftButton.png")
        self.leftButton = Button(playerFrame, image = leftImg, height = 50, width = 50, command = self.leftButtonPressed)
        self.leftButton.image = leftImg
        self.leftButton.grid(row = 2, column = 1)

        self.centerButtonCnt = 0
        self.playImg = ImageTk.PhotoImage(file="E:/Users/sonu/Downloads/playButton.png")
        self.pauseImg = ImageTk.PhotoImage(file="E:/Users/sonu/Downloads/pauseButton.png")
        self.centerButton = Button(playerFrame, image = self.playImg, height = 50, width = 50, command = self.centerButtonPressed)
        self.centerButton.image = self.playImg
        self.centerButton.grid(row = 2, column = 2)
        
        rightImg = ImageTk.PhotoImage(file="E:/Users/sonu/Downloads/rightButton.png")
        self.rightButton = Button(playerFrame, image = rightImg, height = 50, width = 50, command = self.rightButtonPressed)
        self.rightButton.image = rightImg
        self.rightButton.grid(row = 2, column = 3)

        self.repeatButton = Button(playerFrame, text = '1=')
        self.repeatButton.grid(row = 2, column = 4)

        self.playSong(random.choice(self.songList))
        threading.Thread(target = self.updateSliderPos).start()
        

    def centerButtonPressed(self):

    	self.centerButtonCnt += 1
    	if self.centerButtonCnt % 2 == 0:
    		self.centerButton.config(image = self.playImg)
    		self.unpauseMusic()
    	else:
    		self.centerButton.config(image = self.pauseImg)
    		self.pauseMusic()

    def pauseMusic(self):
    	pygame.mixer.music.pause()

    def unpauseMusic(self):
    	pygame.mixer.music.unpause()


    def sliderInFocus(self, event):

        #print('Slider Clicked', currentValue)
        print('Sldier In Focus')
        self.sliderClicked = True

    def updateSliderPos(self):

        print('Hello from inside of update slider pos')
        try:
            while pygame.mixer.music.get_busy():
                totalSeconds = pygame.mixer.music.get_pos()//1000

                currentMins = totalSeconds//60
                currentSecs = int(totalSeconds%60)

                self.songCurrentTime.config(text = str(currentMins).zfill(2) + ':' + str(currentSecs).zfill(2))
                self.songSlider.set(int(totalSeconds))
            self.rightButtonPressed()
            threading.Thread(target = self.updateSliderPos).start()
        except:
            print('Error while updating time')


    def rightButtonPressed(self):

    	#print(pygame.mixer.music.get_pos()//1000)
    	if self.currentSongIndex < len(self.songList) -1:
    		self.playSong(self.songList[self.currentSongIndex + 1])


    def leftButtonPressed(self):

    	if self.currentSongIndex > 0 :
    		self.playSong(self.songList[self.currentSongIndex - 1])


    def playSong(self, song_name):

    	self.currentSongIndex = self.songList.index(song_name)	#set song index
    	print('Current Song Index: ', self.currentSongIndex)

    	pygame.mixer.music.load(song_name)	#song name with path 
    	
    	print(song_name)
    	songMp3 = MP3(song_name)		# to find length first load the song using mixer
    	songLength = songMp3.info.length

    	print('Song Total seconds : ', songLength)

    	self.songTotalMins = int(songLength/60)
    	self.songTotalSecs = int(songLength%60)
    	print('Song length - ', self.songTotalMins,':', self.songTotalSecs)

    	self.songTotalTime.config(text = str(self.songTotalMins).zfill(2) + ':' + str(self.songTotalSecs).zfill(2))
    	#currentPos = pygame.mixer.music.get_pos()
    	self.songSlider.config(to = int(songLength))
    		
    	pygame.mixer.music.play()

    	


def mP():
    #global screen
    musicPlayerFrame = Frame(screen)
    musicPlayerFrame.pack()
    # load Image
    render = ImageTk.PhotoImage(file="E:/Users/sonu/Downloads/AIP4.png")        # use '/' insted of '\' 
    #create Label
    albumPhoto = Label(musicPlayerFrame, image = render, height = 400, width = 500)
    albumPhoto.image = render
    albumPhoto.grid(row= 0, column = 0)
    

screen = Tk()
screen.title('Music Player')

song_list = ['Hide.mp3', 'UpTownFunk.mp3', 'CakeByOcean.mp3', 'NiceToMeetYa.mp3', 'NoJudgement.mp3', 'Habit.mp3', 'HeartbreakWhether.mp3']

Mp = MusicPlayer(screen, song_list)


def sleeptime():
	time.sleep(30)
	pygame.mixer.music.stop()


#pygame.init()
#song_name = random.choice(song_list)

#get song length using mutagen.mp3 module
#song = MP3(song_name)
#slength = song.info.length
#print('song length - ' + str(int(slength/60)), ':', str(int(slength%60)))
#-----

#pygame.mixer.init(48000)  # Bit rate of song - find it using audacity

#print(song_name)

#pygame.mixer.music.load(song_name)
#pygame.mixer.music.play()

def windowDestroyed(event):

	pygame.mixer.music.stop()

#threading.Thread(target = sleeptime).start()		#Seperate thread to play song and sleep
screen.bind("<Destroy>", windowDestroyed)

screen.mainloop()
