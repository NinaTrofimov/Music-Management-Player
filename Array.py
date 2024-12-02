class ArrayList(object):
    def __init__(self, capacity, emptyValue=None):
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
        if self.isEmpty():
            return "The playlist is empty"
        return "\n".join([f"{item[1]} by {item[0]}" for item in self.items if item != self.emptyValue])
        # Song x By artist x

    def __iter__(self):
        # TODO Does an iteration overview of the array
        for i in range(self.logicalSize):
            yield self.items[i]

    def __add__(self, other):
        # TODO Returns a new array containing the contents of self and other
        new_capacity = self.capacity + other.capacity
        newArray = ArrayList(new_capacity, self.emptyValue)
        for item in self:
            newArray.add(item[0], item[1])  # (artist, song)
            # Add items from the second array
        for item in other:
            newArray.add(item[0], item[1])  # (artist, song)
        return newArray

    def __eq__(self, other):
        # TODO Returns True if self equals to other, if not it will return False
        return self.items == other  # If the order of the songs aren't the same/ will return False

    def __shrink__(self):
        # Decreases the physical size of the array if necessary.
        # create new capacity size to shrink array

        new_capacity = max(self.capacity // 2, self.logicalSize)
        # create a temp array with new capacity
        temp = ArrayList(new_capacity, self.emptyValue)
        # copy all the self.items onto the temp array with for loop
        for i in range(self.logicalSize):
            temp.items[i] = self.items[i]
        # copy temp items onto self items
        self.items = temp.items
        # update capacity
        self.capacity = len(self.items)

    def __grow__(self):
        # Increases the physical size of the array if necessary.
        new_capacity = max(2 * self.capacity, 1)  # Ensure capacity is at least 1
        # create temp array with the new capacity
        temp = ArrayList(new_capacity, self.emptyValue)
        # copy onto temp array
        for i in range(self.logicalSize):
            temp.items[i] = self.items[i]
        # recopy onto self items
        self.items = temp.items
        self.capacity = new_capacity

    def clear(self):
        # TODO Makes the array empty and rests logical size to 0
        for i in range(len(self.items)):
            self.items[i] = self.emptyValue
        self.logicalSize = 0

    def add(self, artist, song):
        # TODO Adds the song name and artist name 
        # Check to see if theres room to add the artist and song
        if self.logicalSize == self.capacity:
            self.__grow__()

        fullSong = (artist, song)
        self.items[self.logicalSize] = fullSong
        self.logicalSize += 1

    def remove(self, song):
        # TODO  Removes the song name and artist name 
        # Search for the song by name
        for i in range(self.logicalSize):
            if self.items[i][1] == song:  # Compare with song name

                # Shift items left to remove the found song
                for j in range(i, self.logicalSize - 1):
                    self.items[j] = self.items[j + 1]

                # Clear the last logical item and update logical size
                self.items[self.logicalSize - 1] = self.emptyValue
                self.logicalSize -= 1

                # Check if array should shrink
                if self.logicalSize <= self.capacity // 4:
                    self.__shrink__()

                print(f"'{song}' has been removed.")
                return True

        print(f"'{song}' not found in the playlist.")
        return False

    def sort(self):
        # TODO Sorts the playlist alphabetically by song title.
        pass

    def search(self, song):
        # TODO Check for a specific song by name.
        # goes through the items 
        for i in range(self.logicalSize):
            # grabs item at the index 1 of the tuple and compares to song name
            if self.items[i][1] == song:
                # prints if it finds it
                return print(f'{song} is in playlist at index {i}')
        return print("Song is not in playlist")


def test_code():
    playlist1 = ArrayList(5)

    print("After adding")  # add test
    playlist1.add("Artist1", "Song1")
    playlist1.add("Artist2", "Song2")
    playlist1.add("Artist3", "Song3")
    print(playlist1)
    print()
    playlist1.remove('Song2')  # remove test
    print(playlist1)
    print()
    playlist1.search('Song3')  # search test
    playlist1.search('Song2')
    print("\nClear playlist")   # clear test
    playlist1.clear()
    print(playlist1)  # Should display nothing
    print(f"Is empty: {playlist1.isEmpty()}\n")  # should return true

    print('Add 9 songs to new playlist')
    playlist2 = ArrayList(5)  # grow and shrink test
    for i in range(1, 10):
        playlist2.add(f'Artist{i}', f'Song{i}')
        print(f"Current logical size: {playlist2.logicalSize}, Capacity: {playlist2.capacity}")
    print("\nAfter adding 9 songs")
    print(playlist2)

    for i in range(1, 8):
        playlist2.remove(f'Song{i}')
        print(f"Current logical size: {playlist2.logicalSize}, Capacity: {playlist2.capacity}")

    print("After removing 7 songs")
    print(playlist2)
    playlist2.clear()

    playlist1 = ArrayList(5)
    playlist1.add("Artist1", "Song1")
    playlist1.add("Artist2", "Song2")
    playlist2 = ArrayList(5)
    playlist2.add("Artist1", "Song1")
    playlist2.add("Artist2", "Song2")

    # test equality: should be true since the playlists are identical
    print(f"playlist1 == playlist2: {playlist1 == playlist2}")
    # modify one playlist
    playlist1.add("Artist3", "Song3")
    # test equality again: should be false since the playlists are now different
    print(f"playlist1 == playlist2: {playlist1 == playlist2}")

    combined_playlist = playlist1 + playlist2   # __add__ test

    print("\nCombined playlist:")
    print(combined_playlist)

test_code()
