class Song:
    def __init__(self,title,artist,album,length):
        self.validate_arguments(title,artist,album,length)
        
        self.title = title
        self.artist = artist
        self.album = album
        self.__length = length

    @staticmethod
    def validate_arguments(title=None,artist=None,album=None,length=None):       
        if not (isinstance(title,str) and isinstance(artist,str) and isinstance(album,str) and isinstance(length,str)):
            raise TypeError('All values must be strings!')

        if title == "" or artist == "" or album == "" or length == "":
            raise TypeError('None of the values can be the empty string!')

        listOfValues = length.split(":")

        if len(listOfValues) < 2:
            raise TypeError('Incorrect length of song - it can not be a single digit!')

        if '' in listOfValues:
            raise TypeError('Incorrect input - you have entered a wrong length!')

        for element in list(length):
            if element not in ['0','1','2','3','4','5','6','7','8','9',':']:
                raise TypeError('Incorrect input - you have entered an unrecognizable symbol in the length!')

        if len(listOfValues) == 3:
            if len(listOfValues[1]) == 1:
                raise TypeError('Incorrect input - you have entered an hour but minutes less than ten as a single digit!')

        if len(listOfValues) > 3:
            raise TypeError('Incorrect input - you have entered more numbers than just hours, minutes and seconds!')

        if len(listOfValues) == 3:
            if int(listOfValues[1]) > 60:
                raise TypeError('Incorrect input - minutes value is bigger than maximum possible')
            if int(listOfValues[2]) > 60:
                raise TypeError('Incorrect input - seconds value is bigger than maximum possible')
        else:
            if int(listOfValues[0]) > 60:
                raise TypeError('Incorrect input - minutes value is bigger than maximum possible')
            if int(listOfValues[1]) > 60:
                raise TypeError('Incorrect input - seconds value is bigger than maximum possible')

    def __str__(self):
        return f'{self.artist} - {self.title} from {self.album} - {self.__length}'

    def __eq__(self,other):
        return self.artist == other.artist and self.title == other.title and self.album == other.album and self.__length == other.__length
    
    def __hash__(self):
        return hash((self.artist,self.title,self.album,self.__length))

    def __repr__(self):
        return f'{self}'

    def length(self,seconds=False,minutes=False,hours=False):
        
        listOfValues = self.__length.split(":")

        if len(listOfValues) == 3:
            if seconds == True:
                return int(listOfValues[0])*1440+int(listOfValues[1])*60+int(listOfValues[2])
            elif minutes == True:
                return int(listOfValues[0])*60+int(listOfValues[1])
            elif hours == True:
                return int(listOfValues[0])
        else:
            if seconds == True:
                return int(listOfValues[0])*60+int(listOfValues[1])
            elif minutes == True:
                return int(listOfValues[0])
            elif hours == True:
                return 0

        return self.__repr__()


