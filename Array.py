class ArrayList(object):
    def __init__(self, capacity, emptyValue = None):
        self.items = list()
        self.capacity = capacity
        self.logicalSize = 0
        self.emptyValue = emptyValue
        for count in range(capacity):
            self.items.append(emptyValue)


    def isEmpty(self):
        # TODO Returns True if array is empty, False otherwise.
        return self.logicalSize == 0

    def __len__(self):
        # TODO Returns the number of items in the array
        return self.logicalSize

    def __str__(self):
        # TODO Returns the string representation of the array
        # item[1] and item[0] are artist and song respectively.
        # Item != self.emptyValue makes sure that you're skipping the slots that say "None"
        return "\n".join([f"{item[1]} by {item[0]}" for item in self.items if item != self.emptyValue])
        # Song x By artist x
    def __iter__(self):
        # TODO Does an iteration overview of the array
        for i in range(self.logicalSize):
            yield self.items[i]

    def __add__(self, other):
        # TODO Returns a new array containing the contents of self and other
        pass

    def __eq__(self, other):
        # TODO Returns True if self equals to other, if not it will return False
        return self.items == other  # If the order of the songs aren't the same/ will return False

    def __shrink__(self):
        # Decreases the physical size of the array if necessary.
        if self.logicalSize <= len(self) // 4 and len(self) >= self.capacity * 2:
            temp = ArrayList(len(self) // 2)
            for i in range(self.logicalSize):
                temp.items[i] = self.items[i]
            self.items = temp.items

    def __grow__(self):
        # Increases the physical size of the array if necessary.
        if self.logicalSize == self.__len__:
            temp = ArrayList(len(self) * 2)
            for i in range(self.logicalSize):
                temp.items[i] = self.items[i]
            self.items = temp.items


    def clear(self):
        # TODO Makes the array empty and rests logical size to 0
        for i in range(len(self.items)):
            self.items[i] = self.emptyValue
        self.logicalSize = 0

    def add(self, artist, song):
        # TODO Adds the song name and artist name 
        # Maybe should be stored as a dictionary or tuple?
        for i in range(len(self.items)):
            if self.items[i] == self.emptyValue:    # Find the fist empty slot
                self.items[i] = (artist, song)      # Place values
                self.logicalSize += 1
                return
    def remove(self, song):
        # TODO  Adds the song name and artist name 
        for i in range(len(self.items)):    # Loop through the list
            artist, track = self.items[i]    # Get access to the 2 items(artist, song) by index.
            if track == song:   # Check if the song mathes the one to remove
                self.items[i] = self.emptyValue
                self.logicalSize -= 1
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

def main():
    playlist = ArrayList(5)
    response = 'y'
    while(response != 'N'):
        songName = input("Enter song name: ")
        artistName = input("Enter artist name: ")
        playlist.add(artistName, songName)
        response = input("Would you like to enter another song? Y/N")
        response = response.upper()

        print(playlist)
main()


# def test_code():
#     playlist = ArrayList(5)
#
#     print("After adding")
#     playlist.add("Artist1", "Song1")
#     playlist.add("Artist2", "Song2")
#     playlist.add("Artist3", "Song3")
#
#     print(playlist)
#
#     print('after removing')
#     playlist.remove('Song2')
#     print(playlist)
# test_code()