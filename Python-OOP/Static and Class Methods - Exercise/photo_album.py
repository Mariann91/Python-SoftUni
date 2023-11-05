from math import ceil


class PhotoAlbum:
    MAX_PHOTOS = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):

        instance_pages = ceil(photos_count / cls.MAX_PHOTOS)

        return cls(instance_pages)

    def add_photo(self, label: str):

        for page in range(self.pages):

            if len(self.photos[page]) < PhotoAlbum.MAX_PHOTOS:
                self.photos[page].append(label)
              
                return f"{label} photo added successfully on page {page + 1} slot {self.photos[page].index(label) + 1}"

        return "No more free slots"

    def display(self):
        result = ["-" * 11]

        for page in self.photos:
            result.append(("[] " * len(page)).rstrip())
            result.append("-" * 11)

        return "\n".join(result)
      
