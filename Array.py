class ArrayList(object):
    def __init__(self, artist, song, sourceCollections=None):
        self.items = list()
        self.artist = artist
        self.song = song
        self.size = 0
        if sourceCollections:
            for item in sourceCollections:
                self.size += 1
                self.add(item)

    def isEmpty(self):
        # TODO Returns True if array is empty, False otherwise.
        pass

    def __len__(self):
        # TODO Returns the number of items in the array
        return len(self.items)

    def __str__(self):
        # TODO Returns the string representation of the array
        pass

    def __iter__(self):
        # TODO Does an iteration overview of the array
        for i in self.items:
            yield i

    def __add__(self, other):
        # TODO Returns a new array containing the contents of self and other
        pass

    def __eq__(self, other):
        # TODO Returns True if self equals to other, if not it will return False
        pass

    def clear(self):
        # TODO Makes the array empty.
        self.items = []

    def add(self, song, artist):
        # TODO Adds the song name and artist name 
        # Maybe should be stored as a dictionary or tuple?
        pass

    def remove(self, song):
        # TODO  Adds the song name and artist name 
        pass

    def sort(self):
        # TODO Sorts the playlist alphabetically by song title.
        pass

    def search(self, song):
        # TODO Check for a specific song by name.
        pass

    def display(self):
        # TODO Displays the playlist in its current order.
        pass