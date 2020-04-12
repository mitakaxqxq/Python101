from song import Song
from random import randint
import json

class Playlist:
    def __init__(self,name,repeat=False,shuffle=False):
        self.validate_arguments(name,repeat,shuffle)

        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle
        self.listOfSongs = []
        self.playedSongs = []

    def __eq__(self,other):
        return self.name == other.name and self.repeat == other.repeat and self.shuffle == other.shuffle and self.listOfSongs == other.listOfSongs

    def add_song(self,song):
        if not isinstance(song,Song):
            raise TypeError('Wrong argument - you can only add arguments of song type to the playlist')
        self.listOfSongs.append(song)

    def remove_song(self,song):
        if not isinstance(song,Song):
            raise TypeError('Wrong argument - you can only remove arguments of song type to the playlist')
        if song not in self.listOfSongs:
            raise TypeError('Wrong operation - the song you are trying to remove is not in the list')
        self.listOfSongs.remove(song)

    def add_songs(self,songs):
        if not isinstance(songs,list):
            raise TypeError('Wrong argument - the parameter of this method must be list of songs')
        for song in songs:
            if not isinstance(song,Song):
                raise TypeError('Wrong argument - a value in the list you are trying to add is not of song type')
            self.listOfSongs.append(song)

    def total_length(self):
        return len(self.listOfSongs)

    def __str__(self):
        string = ''
        for song in self.listOfSongs:
            string += str(song)
            string += '\n'
        return string

    @staticmethod
    def validate_arguments(name=None,repeat=False,shuffle=False):
        if not isinstance(name,str):
            raise TypeError('Wrong input - name of playlist must be string!')
        if not isinstance(repeat,bool):
            raise TypeError('Wrong input - type of repeat must be bool!')
        if not isinstance(shuffle,bool):
            raise TypeError('Wrong input - type of shuffle must be bool!')

    def artists(self):
        myDict = {}

        for song in self.listOfSongs:
            if song.artist in myDict.keys():
                myDict[song.artist] += 1
            else:
                myDict[song.artist] = 1

        return myDict

    def next_song(self):
        
        if self.shuffle == True:
            if self.repeat == True:
                if self.listOfSongs == []:
                    self.listOfSongs = self.playedSongs
                    self.playedSongs = []
                    index = randint(0,len(self.listOfSongs)-1)
                    self.playedSongs.append(self.listOfSongs[index])
                    self.listOfSongs.remove(self.listOfSongs[index])
                    return self.playedSongs[-1]
                else:
                    index = randint(0,len(self.listOfSongs)-1)
                    self.playedSongs.append(self.listOfSongs[index])
                    self.listOfSongs.remove(self.listOfSongs[index])
                    return self.playedSongs[-1]
            else:
                if self.listOfSongs == []:
                    raise ValueError('No more songs in the playlist')
                else:
                    index = randint(0,len(self.listOfSongs)-1)
                    self.playedSongs.append(self.listOfSongs[index])
                    self.listOfSongs.remove(self.listOfSongs[index])
                    return self.playedSongs[-1]
        else:
            if self.repeat == True:
                if self.listOfSongs == []:
                    self.listOfSongs = self.playedSongs
                    self.playedSongs = []
                    index = 0
                    self.playedSongs.append(self.listOfSongs[index])
                    self.listOfSongs.remove(self.listOfSongs[index])
                    return self.playedSongs[-1]
                else:
                    self.playedSongs.append(self.listOfSongs[0])
                    self.listOfSongs.remove(self.listOfSongs[0])
                    return self.playedSongs[-1]
            else:
                if self.listOfSongs == []:
                    raise ValueError('No more songs in the playlist')
                else:
                    self.playedSongs.append(self.listOfSongs[0])
                    self.listOfSongs.remove(self.listOfSongs[0])
                    return self.playedSongs[-1]

    def save(self):
        fileName = self.name.replace(' ','-')
        pathToFile = './playlist-data/' + fileName + '.json'
        with open(pathToFile,'w') as f:
            x = self.__dict__
            x['listOfSongs'] = [str(song) for song in self.listOfSongs]
            json.dump(x, f)
            #json.dump(self.__dict__,f,default=Song.__str__)

    def load(self,path):
        with open(path,'r') as f:
            myPlaylist = json.load(f)
            #print(myPlaylist)
            return myPlaylist
'''
playlist = Playlist("For Code",True,False)
playlist.listOfSongs = [Song("Odin","Manowar","The Sons of Odin","3:44"),Song("Little Swing","AronChupa","I'm an Albatraoz","3:50"),Song("Hole in the Roof","AronChupa","I'm an Albatraoz","3:20")]
print(playlist.next_song())
print(playlist.next_song())
print(playlist.next_song())
print(playlist.next_song())
playlist.save()
playlist.load('./playlist-data/For-Code.json')
print(playlist)
'''