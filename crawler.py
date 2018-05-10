import os
import sys
from parser import *
import pickle
from create_file import *
from remove_stopwords import *
base_url = "http://www.slolyrics.com/" # USED TO BE http://www.lyrics123.net/


# change this to specify the page. all options are above
artist_initial = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"]

all_data = []

for initial in artist_initial:
    data_with_initial = []
    artist_list_url = os.path.join(base_url, "izvajalci", initial) # izvajalci = artist
    artists = getListOfArtist(artist_list_url)
    totalArtists = len(artists)
    print("crawling artists starting with " + initial)
    for i in range(totalArtists):
        # keep track of which artist we're currently crawling
        print("parsing songs for " + (str)(artists[i].attrs['href']))
        sys.stdout.flush()

        # doing actual crawling
        artist = artists[i]
        artist_url = os.path.join(base_url, artist.attrs['href'])
        # print(artist_url)
        songs = getListofSongs(artist_url)
        for song_suffix in songs:
            song_url = os.path.join(base_url, song_suffix.attrs['href'])
            print("parsing " + song_url)
            song = getSongFromURL(song_url)
            if song is not None:
                all_data.append(song)
                data_with_initial.append(song)

    # dump into [initial]_song.txt file
    dumpSongDataIntoFile(initial + "_songs.dat", data_with_initial)

# save all song data
dumpSongDataIntoFile("songs/songs.dat", all_data)

# remove stop words, clean data, and write to data file
removeStopWords("songs/songs.dat", "songs/songs_data.dat")
