class ArrayList(object):
    def __init__(self, artist, song, sourceCollections=None):
        self.items = list()
        self.artist = artist
        self.song = song
        self.size = 0

        self.items.append((artist, song))
        self.size += 1
        if sourceCollections:
            for item in sourceCollections:
                self.size += 1
                self.add(item)

    def isEmpty(self):
        # TODO Returns True if array is empty, False otherwise.
        return len(self.items) == 0

    def __len__(self):
        # TODO Returns the number of items in the array
        return len(self.items)

    def __str__(self):
        # TODO Returns the string representation of the array
        return "\n".join([f"{song} by {artist}" for song, artist in self.items])
        # Song x By artist x
    def __iter__(self):
        # TODO Does an iteration overview of the array
        for i in self.items:
            yield i

    def __add__(self, other):
        # TODO Returns a new array containing the contents of self and other
        pass

    def __eq__(self, other):
        # TODO Returns True if self equals to other, if not it will return False
        return self.items == other  # If the order of the songs aren't the same/ will return False

    def clear(self):
        # TODO Makes the array empty.
        self.items = []

    def add(self, artist, song):
        # TODO Adds the song name and artist name 
        # Maybe should be stored as a dictionary or tuple?
        self.items.append((artist, song))
        self.size += 1

    def remove(self, song):
        # TODO  Adds the song name and artist name 
        for i in range(len(self.items)):    # Loop through the list
            artist, track = self.items[i]    # Get access to the 2 items(artist, song) by index.
            if track == song:   # Check if the song mathes the one to remove
                del self.items[i]
                self.size -= 1
                return True # If song was found return True
        return False # If song wasn't found return false

    def sort(self):
        # TODO Sorts the playlist alphabetically by song title.
        pass

    def search(self, song):
        # TODO Check for a specific song by name.
        pass

    # def display(self):
    #     # TODO Displays the playlist in its current order.
    #     if self.isEmpty():
    #         print("The playlist is empty.")
    #     else:
    #         print("Playlist:\n")
    #         for arist, song in self.items:
    #             print(f'{song} by {arist}')


    # Main function to test code so far
def test_code():
    playlist = ArrayList('Artist1', 'Song1')

    print(playlist, "\n")

    playlist.add('Artist2', 'Song2')
    playlist.add('Artist3', 'Song3')

    print("Post add")
    print(playlist,"\n")

    playlist.remove("Song3")

    print("Post remove")
    print(playlist)
test_code()