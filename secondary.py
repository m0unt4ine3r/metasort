import songclass, secondary
from os import chdir, environ, getcwd
from glob import glob
from subprocess import call, DEVNULL, check_output
from codecs import decode
from os.path import exists, isdir, isfile, join, split

######################################################################################################
#Secondary functions:

########################################
#For more reliable title capitalization:

def capitalize(s):
	return re.sub(r"[A-Za-z]+('[A-Za-z]+)?", lambda mo: mo.group(0)[0].upper() + mo.group(0)[1:].lower(), s)

################################
#Grabs tags and returns as list: *improve checking method so only needed values are checked; maybe make counter to show how many are filtered out

#make id3v2 output to hidden file for line reading and (possibly) easier parsing?
#can change to eliminate dependency on proper formating? - do with (fuzzy?) regex search
#migrate to class when built
def getdata(song, verb=1):
	data = songclass.song(song)

	if verb >= 3:														#verbosity
		print("Metadata for", split(song)[1] + ':',
			 "\n Title:", data.title,
			 "\n Author:", data.author,
			 "\n Album:", data.album,
			 "\n Genre:", data.genre)

	return data.title, data.author, data.album, data.genre

#############################################
#Checks to see if song has existing metadata (WIP):

#def datachecker(files, srcdir=source):
#	data = ""
#
#	for song in files:
#		data = getdata(join(srcdir, song))
#
#	return data

