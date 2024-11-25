class ArrayList(object):
    def __init__(self,artist,song,sourceCollections = None):
        self.items = list()
        self.artist = artist
        self.song = song
        self.size = 0
        if sourceCollections:
            for item in sourceCollections:
                self.size += 1
                self.add(item)
    
    def isEmpty(self):
        #TODO Returns True if array is empty, False if it’s empty. 
        pass
    
    def __len__(self):
        #TODO Returns the number of items in the array
        pass

    def __str__(self):
        #TODO Returns the string representation of the array
        pass

    def __iter__(self):
        #TODO Does an iteration overview of the array
        pass

    def __add__(self,other):
        #TODO Returns a new array containing the contents of self and other
        pass

    def __eq__(self,other):
        #TODO Returns True if self equals to other, if not it will return False
        pass

    def clear(self):
        #TODO Makes the array empty.
        pass

    def add(self,song,artist):
        #TODO Adds the song name and artist name 
        pass

    def remove(self,song):
        #TODO  Adds the song name and artist name 
        pass

    def sort(self):
        #TODO Sorts the playlist alphabetically by song title.
        pass
    