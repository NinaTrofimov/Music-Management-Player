"""

Authors: Isaiah, Nina, Anthony, Tyler

Date: 12/4/2024

File: main.py

Description: Main function to show to usage of the Arraylist class. Supports methods
like add, remove, search, clear, __add__, and __eq__

"""
from Arraylist import ArrayList
def main():
    playlist1 = ArrayList(5)
    playlist2 = ArrayList(5)


    # Add some songs to playlist1
    playlist1.add("Tyler The Creator", "Igor")
    playlist1.add("Lady Gaga", "Die With A Smile")
    playlist1.add("Sabrina Carpenter", "Taste")

    # Add different songs to playlist2
    playlist2.add("Hozier", "Too Sweet")
    playlist2.add("Chappell Roan", "HOT TO GO!")
    playlist2.add("Sabrina Carpenter", "Please Please Please")

    # Print playlist1 and playlist2
    print("Playlist 1:")
    print(playlist1)    # display all songs in playlist1
    print()
    print("Playlist 2:")
    print(playlist2)    # display all songs in playlist1
    print()

    # Remove a song from playlist1
    song_to_remove = "Taste"    # specify a song to remove from playlist1
    print(f"Removing '{song_to_remove}' from Playlist 1:")
    playlist1.remove(song_to_remove)
    print("Playlist 1:")
    print(playlist1)
    print()

    # Search for song just removed from playlist 1:
    song_to_search = "Taste"    # specify a song to search
    print(f"Searching for '{song_to_search}' in Playlist 1:")
    playlist1.search(song_to_search)
    # Search for a song in playlist2
    song_two_search = "HOT TO GO!"
    print(f"Searching for '{song_two_search}' in Playlist 2:")
    playlist2.search(song_two_search)
    print()

    # Clear playlist1
    print("Clearing Playlist 1:")
    playlist1.clear()
    print(playlist1)  # Should display "The playlist is empty"
    print()

    # Add more songs after clearing playlist1
    playlist1.add("Kendrick Lamar", "Luther")
    playlist1.add("The Weeknd", "Timeless")
    print("Playlist 1 after adding more songs:")
    print(playlist1)
    print()

    # Combine playlists using __add__
    combined_playlist = playlist1 + playlist2   # Combine both playlists
    print("Combined Playlist (Using __add__):")
    print(combined_playlist)    # Display new playlist
    print()

    # Check if the playlists are equal using __eq__
    print(f"Is playlist1 equal to playlist2? {playlist1 == playlist2}")     # should result in False
    print()


if __name__ == "__main__":
    main()

