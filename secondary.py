import songclass
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

#############################################
#Checks to see if song has existing metadata (WIP):

#def datachecker(files, srcdir=source):
#	data = ""
#
#	for song in files:
#		data = getdata(join(srcdir, song))
#
#	return data

