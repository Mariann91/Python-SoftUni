from project.song import Song
from typing import List


class Album:
    def __init__(self, name: str, *songs: Song) -> None:
        self.name = name
        self.published: bool = False
        self.songs: List[Song] = list(songs)

    def add_song(self, current_song: Song) -> str:

        if current_song.single:
            return f"Cannot add {current_song.name}. It's a single"

        if self.published:
            return "Cannot add songs. Album is published."

        if current_song in self.songs:
            return "Song is already in the album."

        self.songs.append(current_song)

        return f"Song {current_song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):

        for item in self.songs:

            if item.name == song_name:

                if self.published:
                    return "Cannot remove songs. Album is published."

                self.songs.remove(item)

                return f"Removed song {song_name} from album {self.name}."

        return "Song is not in the album."

    def publish(self) -> str:

        if self.published:
            return f"Album {self.name} is already published."

        self.published = True

        return f"Album {self.name} has been published."

    def details(self) -> str:
        songs_details = "\n".join([f"== {current_song.get_info()}" for current_song in self.songs])

        return f"Album {self.name}\n" +\
               f"{songs_details}\n"
      
