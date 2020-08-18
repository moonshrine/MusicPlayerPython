# program to change cover album photo in mp3 file embed

import time
from mutagen.id3 import ID3, APIC
from io import BytesIO
from PIL.ImageQt import ImageQt
from mutagen.mp3 import MP3
from PIL import Image

file_path = "D:/sonu/MusicPlayerPython/Songs/She Looks So Perfect.mp3"	
audio = ID3(file_path)


audio.add(
	APIC(
		encoding = 3,
		mime = 'image/jpeg',
		type = 3,
		data = open('D:/sonu/MusicPlayerPython/AlbumIcons/5SOS.jpg','rb').read()
		)
)
audio.save(v2_version=3)
