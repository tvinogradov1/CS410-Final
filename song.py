class Song(object):
    def __init__(self, artist, album, lyrics):
        self.artist = artist
        self.album = album
        self.lyrics = lyrics

    def getArtist(self):
        return self.artist

    def getAlbum(self):
        return self.album

    def getLyrics(self):
        return self.lyrics
