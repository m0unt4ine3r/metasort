from subprocess import call, check_output
import sys
import logging
import time

#logging.basicConfig(level=logging.INFO, filename="example.log")
#log = logging.getLogger(__name__)

def update_progress(progress):
	time.sleep(0.1)
	size = 50
	total = 100
	per = int((progress*size)/total)
	sys.stdout.write("\r[{0:-<50}] {1}%".format('#'*per, progress))
	sys.stdout.flush()
	
def set_tag():
#	log.info("")
	for i in range(0, 101):
		update_progress(i)
#	try:
#		log.debug("checking for id3v2 executable")
#		check_output(['id3v2'])
#	except FileNotFoundError:
#		log.error("could not load id3v2, which is required for this module.")
#		sys.exit(2)
for i in range(100):
	time.sleep(0.01)
	print("\rThing", end="")
