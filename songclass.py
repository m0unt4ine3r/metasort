#Class file for songs
from subprocess import check_output
from codecs import decode

class song:
	def __init__(self, songfile, title="Unknown", author="Unknown", album="Unknown", genre="Unknown"):
		self.title = title
		self.author = author
		self.album = album
		self.genre = genre
		self.getdata(songfile)

	#Setters
	def settitle(self, title):
		self.title = title

	def setauthor(self, author):
		self.author = author

	def setalbum(self, album):
		self.album = album

	def setgenre(self, genre):
		self.genre = genre

	#Read in data from file
	def getdata(self, songfile):
		output = decode(check_output(["id3v2", '-R', songfile]))			#might need to change
		frame = ""
		data = []
		count = 1

		for char in output:									#compare to list-dl's imp of parser
			if char == ':':
				if frame == "TIT2" or frame == "TPE1" or frame == "TCON" or frame == "TALB":
					i = count+1
					temp = output[i]

					while output[i+1] != '\n':		 #off by 1?
						i += 1
						temp += output[i]

					if frame == "TIT2":
						self.title = temp

					elif frame == "TPE1":
						self.author = temp

					elif frame == "TCON":
						self.genre = temp

					elif frame == "TALB":
						self.album = temp

			elif char == '\n':
				frame = ""

			else:
				frame += char

			count += 1
