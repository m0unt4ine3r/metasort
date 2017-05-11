############################# 
#Quasi-interactive id3v2 CLI: *maybe add code for filename parsing here

#make input one line w/ delim
def metachange(files, numfiles, specific=False, target=source, verb=1):
	if specific:													#for manual file input
		num = numfiles[0]
		numfiles = numfiles[1]
	else:
		num = 1

	chdir(target)                                                                                                   #change back to original directory when done for convenience?

	for song in files:
#		call("clear")
          print("Enter the metadata for {} below ({}/{}) (Format: title/album/artist/genre; leave blank to continue):".format(song, num, numfiles))

          #make while loop here for input safety net
          newdata = input("New frames: ")

          data = getdata(song)
          print("Current frames: {}/{}/{}/{}".format(data[1], data[1], data[2], data[3]))

          newdata = input("New frames: ")
          string = ""
          count = 0

          for char in newdata:
               if char == '/':
                    data[count] = string
                    count += 1
                    string = ""
               else:
                    string += char

		#needs revision for cases where tags exist; also make tag wipe optional
		# call(["id3v2", '-D', song])
		call(["id3v2", '-t', title, '-a', artist, '-g', genre, '-A', album, song])
		num += 1

		# Friendlier interface
		# title=""
		# while title == "":
		#	  title = capitalize(input("Title: "))
		#	  if title == "":
		#		  print("Title cannot be blank!")
		# artist = capitalize(input("Artist: "))
		# if artist == "":
		#	  artist = "Unknown"
		# genre = capitalize(input("Genre: "))
		# if genre == "":
		#	  genre = "Unknown"
		# album = capitalize(input("Album: "))
		# if album == "":
		#	  album = "Unknown"
		
