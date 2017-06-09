import songclass, secondary
from os import chdir, environ, getcwd
from glob import glob
from subprocess import call, DEVNULL, check_output
from codecs import decode
from os.path import exists, isdir, isfile, join, split

############################# 
#Quasi-interactive id3v2 CLI: *maybe add code for filename parsing here

#make input one line w/ delim
def metachange(files, numfiles, specific=False, target="", verb=1):
	if specific:							#for manual file input
		num = numfiles[0]
		numfiles = numfiles[1]
	else:
		num = 1

	chdir(target)							#change back to original directory when done for convenience?

	for song in files:
		#		call("clear")
		print("({}/{}) Enter the metadata for {} below (Format: [title]/[album]/[artist]/[genre]; leave blank to continue):".format(num, numfiles, song))

		data = songclass.song(songfile=song)
		temp = ""
		string = ""
		newdata = ["", "", "", ""]
		original = [data.title, data.album, data.author, data.genre]

		#Loop to change frames
		while True:
			print("Original frames: {}/{}/{}/{}".format(original[0], original[1], original[2], original[3]))

			temp = input("New frames: ")
			string = ""
			count = 0

			for char in temp:
				if char == '/':
					count += 1

			if temp == "":
				break

			elif count != 3:	 #change to exception
				print("Please use format: title/album/artist/genre.")
				continue

			else:
				count = 0
				for char in temp:
					if char == '/':
						if string == "":
							newdata[count] = original[count]
						else:
							newdata[count] = string
						count += 1
						string = ""
					else:
						string += char

				if string == "":
					if newdata[count] == "":
						newdata[count] = original[count]
					else:
						newdata[count] = newdata[count]
				else:
					newdata[count] = string

				data.changetitle(newdata[0])
				data.changealbum(newdata[1])
				data.changeauthor(newdata[2])
				data.changegenre(newdata[3])
				data.writeall()

			print("\nCurrent frames: {}/{}/{}/{}".format(newdata[0], newdata[1], newdata[2], newdata[3]))

		num += 1

		# Friendlier interface
		# title=""
		# while title == "":
		#	  title = secondary.capitalize(input("Title: "))
		#	  if title == "":
		#		  print("Title cannot be blank!")
		# artist = secondary.capitalize(input("Artist: "))
		# if artist == "":
		#	  artist = "Unknown"
		# genre = secondary.capitalize(input("Genre: "))
		# if genre == "":
		#	  genre = "Unknown"
		# album = secondary.capitalize(input("Album: "))
		# if album == "":
		#	  album = "Unknown"

