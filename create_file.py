# > : artist
# $ : album
# # : lyric

def dumpSongDataIntoFile(fname, data):
    f1 = open(fname, "w")
    for i in range(len(data)):
        if data[i].artist is not None:
            f1.write("> " + data[i].artist)
            f1.write("\n")
        if data[i].album is not None:
            f1.write("$ " + data[i].album)
            f1.write("\n")
        if data[i].lyrics is not None:
            for line in range(len(data[i].lyrics)):
                f1.write("# " + data[i].lyrics[line])
                f1.write("\n")
    f1.close()
