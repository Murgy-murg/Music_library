from lib.albums import Albums

class AlbumRepository:
    def __init__(self, connection):
        self._connection = connection

    #get all albums from database
    def all(self):
        rows = self._connection.execute('SELECT * from albums')
        albums = []
        for row in rows:
            item = Albums(row["title"], row["release_year"], row["artist_id"])
            albums.append(item)
        return albums

