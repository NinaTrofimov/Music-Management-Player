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
        newArray = ArrayList(self.items)
        for item in other:
            newArray.add(item)
            self.logicalSize += 1
        

    def __eq__(self, other):
        # TODO Returns True if self equals to other, if not it will return False
        return self.items == other  # If the order of the songs aren't the same/ will return False

    def __shrink__(self):
        # Decreases the physical size of the array if necessary.
        #create new capacity size to shrink array
        new_capacity = max(self.capacity, len(self.items) // 2)
        #create a temp array with new capacity
        temp = ArrayList(new_capacity, self.emptyValue)
        #copy all the self.items onto the temp array with for loop
        for i in range(self.logicalSize):
            temp.items[i] = self.items[i]
        #copy temp items onto self items
        self.items = temp.items
        # update capacity
        self.capacity = len(self.items)

    def __grow__(self):
        # Increases the physical size of the array if necessary.
        new_capacity = max(2 * self.capacity, 1)  # Ensure capacity is at least 1
        # create temp array with the new capacity
        temp = ArrayList(new_capacity, self.emptyValue)
        #copy onto temp array
        for i in range(self.logicalSize):  
            temp.items[i] = self.items[i]
        #recopy onto self items
        self.items = temp.items
        self.capacity = new_capacity


    def clear(self):
        # TODO Makes the array empty and rests logical size to 0
        for i in range(len(self.items)):
            self.items[i] = self.emptyValue
        self.logicalSize = 0

    def add(self, artist, song):
        # TODO Adds the song name and artist name 
        # Maybe should be stored as a dictionary or tuple?

        #Check to see if theres room to add the artist and song
        if self.logicalSize == self.__len__():
            self.__grow__()

        fullSong = [(artist),(song)]
        self.items[self.logicalSize] = (fullSong)
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
                if self.logicalSize <= len(self.items) // 4 and len(self.items) > self.capacity * 2:
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
            #grabs item at the index 1 of the tuple and compares to song name
            if self.items[i][1] == song:
                #prints if it finds it
                return print(f'{song} is in playlist at index {i}')
        return print("Song is not in playlist")


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
     playlist = ArrayList(5)

     print("After adding")
     playlist.add("Artist1", "Song1")
     playlist.add("Artist2", "Song2")
     playlist.add("Artist3", "Song3")

     print(playlist)

     

     print('after removing')
     playlist.remove('Song2')
     print(playlist)

     playlist.search('Song3')
     
test_code()