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

    def __shrink__(self):
        # Decreases the physical size of the array if necessary.
        if self.logicalSize <= self.__len__ // 4 and self.__len__ >= self.capacity * 2:
            temp = ArrayList(self.__len__ // 2)
            for i in range(self.logicalSize):
                temp.items[i] = self.items[i]
            self.items = temp.items

    def __grow__(self):
        #Increases the physical size of the array if necessary.
        if self.logicalSize == self.__len__:
            temp = ArrayList(self.__len__ * 2)
            for i in range(self.logicalSize):
                temp.items[i] = self.items[i]
            self.items = temp.items


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

# Testing
def main():
    playlist = ArrayList(5)
    response = 'y'
    while(response != 'N'):
        songName = input("Enter song name")
        artistName = input("Enter artist name")
        playlist.add(songName,artistName)
        response = input("Would you like to enter another song? Y/N")

main()