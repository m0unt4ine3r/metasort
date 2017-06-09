#Class file for songs
from subprocess import check_output, call
from codecs import decode

class song:
	def __init__(self, songfile="", title="Unknown", author="Unknown", album="Unknown", genre="Unknown", verb=1):
		if songfile != "":
			self.file = songfile
			self.title = title
			self.author = author
			self.album = album
			self.genre = genre

		if songfile != "":
			self.readframes()

	#Read in frames from file *improve checking method so only needed values are checked?
	def readframes(self):
		output = decode(check_output(["id3v2", '-R', self.file]))			#might need to change
		frame = ""
		data = []
		count = 1

		for char in output:									#compare to list-dl's imp of parser
			if char == ':':
				if frame == "TIT2" or frame == "TPE1" or frame == "TCON" or frame == "TALB":
					i = count+1
					temp = output[i]

					while output[i+1] != '\n':
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

	#Change frames
	def changetitle(self, title):
		self.title = title

	def changeauthor(self, author):
		self.author = author

	def changealbum(self, album):
		self.album = album

	def changegenre(self, genre):
		self.genre = genre

	#Write frames to file
	def writetitle(self):
		call(["id3v2", '-t', self.title, self.file])

	def writealbum(self):
		call(["id3v2", '-A', self.album, self.file])

	def writeauthor(self):
		call(["id3v2", '-a', self.author, self.file])

	def writegenre(self):
		call(["id3v2", '-g', self.genre, self.file])

	def writeall(self):
		self.writealbum()
		self.writetitle()
		self.writeauthor()
		self.writegenre()

	#Returns/prints frames:
	def gettitle(self, verb=1):
		if verb >= 3:														#verbosity
			print(split(self.file)[1] + ':',
				 "\n Title:", self.title)

		return self.title

	def getalbum(self, verb=1):
		if verb >= 3:														#verbosity
			print(split(self.file)[1] + ':',
				 "\n album:", self.author)

		return self.album

	def getauthor(self, verb=1):
		if verb >= 3:														#verbosity
			print(split(self.file)[1] + ':',
				 "\n Album:", self.album)

		return self.author

	def getgenre(self, verb=1):
		if verb >= 3:														#verbosity
			print(split(self.file)[1] + ':',
				 "\n Genre:", self.genre)

		return self.genre

