from bs4 import BeautifulSoup
from urllib.request import urlopen
from song import Song
import logging

logging.basicConfig(filename='log.txt', level=logging.DEBUG)

def getListOfArtist(url):
    ''' given artist page url. return a list of html a element to artists'''
    logging.debug("getting artists for " + url)
    f = urlopen(url)
    s = BeautifulSoup(f, "lxml")
    temp = s.find("div", {"id" : "b"})
    temp = temp.find_all("p")[0]
    return temp.find_all("a")

def getListofSongs(url):
    ''' given artist url, return a list of html a element to the songs '''
    logging.debug("getting songs for " + url)
    f = urlopen(url)
    s = BeautifulSoup(f, 'lxml')
    tmp = s.find("div", {"id" : "b"})
    if tmp is None:
        return []
    tmp = tmp.find_all("p")[1]
    tmp = tmp.find_all("a")
    if len(tmp) == 0:
        logging.warning(url + " has no songs")
    return [ tmp[i] for i in range(len(tmp)) if i % 2 == 1 ]

def getSongFromURL(url):
    ''' return a Song object for given song url '''
    logging.debug("get a Song object from " + url)
    f = urlopen(url)
    s = BeautifulSoup(f, 'lxml')
    tmp = s.find("div", {"id" : "b"})
    artistInfo = tmp.find_all("p")[0].find_all("a")
    artist = artistInfo[0].text
    album = None
    if len(artistInfo) > 1:
        album = artistInfo[1].text
    else:
        logging.warning(url + " has no album")
    lyricsInfo = tmp.find("p", {"style" : "padding:30px 0;"})
    if lyricsInfo == None:
        logging.fatal("find lyrics error for " + url)
        return None
    lyrics = []
    for s in lyricsInfo.stripped_strings:
        lyrics.append(s)
    return Song(artist, album, lyrics)
