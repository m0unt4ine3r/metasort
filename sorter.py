#######################
#Metadata based sorter: *needs more for man input case

def metasort(files, numfiles, specific=False, srcdir=source, destdir=dest, verb=1):
	chdir(destdir)

	if specific:													#when using specific
		num = numfiles[0]
		numfiles = numfiles[1]
	else:
		num = 1

#	call("clear")
	for song in files:
		data = getdata(join(srcdir, song), verb=verb)
		path = join(data[1], data[3])
		title = data[0] + ".mp3"

		if verb >= 2:														#verbosity
			print("Copying {} as {} to {} ({}/{})...".format(song, title, path, num, numfiles))

		call(["mkdir", '-p', path], stderr=DEVNULL)
		call(["cp", '-i', join(source, song), join(path, title)])
		num += 1

	if verb >= 1:															#verbosity
		print("Done sorting {} file(s).".format(numfiles))
	fin = input("Delete originals now? [y/N]: ")
	if fin == "y":
		for song in files:
			call(["rm", join(split(srcdir)[1], song)])					
