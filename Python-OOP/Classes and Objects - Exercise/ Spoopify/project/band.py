from typing import List
from project.album import Album
from project.song import Song


class Band:

    def __init__(self, name: str) -> None:
        self.name = name
        self.albums: List[Album] = []

    def add_album(self, current_album: Album) -> str:

        if current_album in self.albums:
            return f"Band {self.name} already has {current_album.name} in their library."

        self.albums.append(current_album)

        return f"Band {self.name} has added their newest album {current_album.name}."

    def remove_album(self, album_name: str) -> str:

        for item in self.albums:

            if item.name == album_name:

                if item.published:
                    return "Album has been published. It cannot be removed."

                self.albums.remove(item)

                return f"Album {item.name} has been removed."

        return f"Album {album_name} is not found."

    def details(self):
        band_details = "\n".join([current_album.details() for current_album in self.albums])

        return f"Band {self.name}\n" +\
               f"{band_details}"
      
