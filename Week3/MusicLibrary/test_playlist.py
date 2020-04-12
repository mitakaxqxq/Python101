import unittest
from song import Song
from playlist import Playlist
class TestValidationOfPlaylistArguments(unittest.TestCase):

    def test_when_playlist_name_is_not_string(self):
        
        exc = None
        
        try:
            p = Playlist(123)
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'Wrong input - name of playlist must be string!')

    def test_when_repeat_value_is_not_bool(self):
        
        exc = None

        try:
            p = Playlist("Code",123)
            print(p)
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'Wrong input - type of repeat must be bool!')


    def test_when_shuffle_value_is_not_bool(self):
        
        exc = None

        try:
            p = Playlist("Code",True,123)
            print(p)
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'Wrong input - type of shuffle must be bool!')

class TestPlaylistMethods(unittest.TestCase):

    def test_adding_element_different_of_song_type(self):

        exc = None
        p = Playlist("Code",True,True)

        try:
            p.add_song([12,3])
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertIsNotNone(str(exc),'Wrong argument - you can only add arguments of song type to the playlist')

    def test_adding_element_of_song_type(self):

        expected = Playlist("Code",True,True)
        expected.listOfSongs = [Song("Odin","Manowar","The Sons of Odin","3:44")]

        result = Playlist("Code",True,True)
        result.add_song(Song("Odin","Manowar","The Sons of Odin","3:44"))

        self.assertTrue(expected == result, "Playlists are equal")


    def test_removing_element_from_playlist_that_is_not_of_song_type(self):

        playlist = Playlist("Code",True,True)
        playlist.listOfSongs = [Song("Odin","Manowar","The Sons of Odin","3:44")]
        
        exc = None
        try:
            playlist.remove_song([1,2,3])
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'Wrong argument - you can only remove arguments of song type to the playlist')

    
    def test_removing_song_from_playlist_that_is_not_in_it(self):

        playlist = Playlist("Code",True,True)
        playlist.listOfSongs = [Song("Odin","Manowar","The Sons of Odin","3:44")]
        exc = None

        try:
            playlist.remove_song(Song("Little Swing","AronChupa","I'm an Albatraoz","3:50"))
        except Exception as err:
            exc=err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'Wrong operation - the song you are trying to remove is not in the list')

    def test_removing_song_from_playlist_that_is_in_it(self):

        expected = Playlist("Code",True,True)
        expected.listOfSongs = [Song("Odin","Manowar","The Sons of Odin","3:44")]

        result = Playlist("Code",True,True)
        result.listOfSongs = [Song("Odin","Manowar","The Sons of Odin","3:44"),Song("Little Swing","AronChupa","I'm an Albatraoz","3:50")]
        result.remove_song(Song("Little Swing","AronChupa","I'm an Albatraoz","3:50"))

        self.assertTrue(expected == result, 'Playlists are equal')

    def test_adding_value_that_is_not_of_list_type(self):

        playlist = Playlist("Code",True,True)
        exc = None

        try:
            playlist.add_songs((Song("Odin","Manowar","The Sons of Odin","3:44"),2,3))
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'Wrong argument - the parameter of this method must be list of songs')        

    def test_adding_list_of_elements_not_of_song_type(self):

        playlist = Playlist("Code",True,True)
        exc = None

        try:
            playlist.add_songs([Song("Odin","Manowar","The Sons of Odin","3:44"),2,3])
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'Wrong argument - a value in the list you are trying to add is not of song type')

    def test_adding_list_of_songs_to_playlist(self):

        expected = Playlist("Code",True,True)
        expected.listOfSongs = [Song("Odin","Manowar","The Sons of Odin","3:44"),Song("Little Swing","AronChupa","I'm an Albatraoz","3:50")]
            
        result = Playlist("Code",True,True)
        result.add_songs([Song("Odin","Manowar","The Sons of Odin","3:44"),Song("Little Swing","AronChupa","I'm an Albatraoz","3:50")])

        self.assertTrue(expected == result, 'Playlists are equal')

    def test_total_length_method(self):

        playlist = Playlist("Code",True,True)
        playlist.listOfSongs = [Song("Odin","Manowar","The Sons of Odin","3:44"),Song("Little Swing","AronChupa","I'm an Albatraoz","3:50")]

        self.assertTrue(2 == playlist.total_length(),'Total length is correct')

    def test_get_artists_and_song_count_for_each_of_them(self):

        playlist = Playlist("Code",True,True)
        playlist.listOfSongs = [Song("Odin","Manowar","The Sons of Odin","3:44"),Song("Little Swing","AronChupa","I'm an Albatraoz","3:50"),Song("Hole in the Roof","AronChupa","I'm an Albatraoz","3:20")]

        expectedDict = {"Manowar":1,"AronChupa":2}

        myDict = playlist.artists()

        self.assertTrue(myDict == expectedDict,'Dictionaries are equal')
        
    def test_saving_and_loading_object_from_a_json_file(self):

        playlist1 = Playlist("For Code",True,True)
        playlist1.listOfSongs = [Song("Odin","Manowar","The Sons of Odin","3:44"),Song("Little Swing","AronChupa","I'm an Albatraoz","3:50"),Song("Hole in the Roof","AronChupa","I'm an Albatraoz","3:20")]
        playlist1.save()
        
        #print(playlist1.__dict__)
        
        result = playlist1.load('./playlist-data/For-Code.json')
        
        print(result)
        
        self.assertTrue(playlist1.__dict__ == result, 'Dictionaries are equal')

if __name__ == '__main__':
    unittest.main()