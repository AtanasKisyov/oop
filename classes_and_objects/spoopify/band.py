class Band:

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name):
        album = ""
        for s in self.albums:
            if s.name == album_name:
                album = s
        if album == "":
            return f"Album {album_name} is not found."
        if album.published:
            return "Album has been published. It cannot be removed."
        self.albums.remove(album)
        return f"Album {album.name} has been removed."

    def details(self):
        string_to_return = ""
        for s in self.albums:
            string_to_return += f"{s.details()}"
        return f"Band {self.name}\n{string_to_return}"
