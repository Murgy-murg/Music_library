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
    #get one album from database dependent on id

    def find(self, id):
        rows = self._connection.execute(f'SELECT * FROM albums WHERE id = %s', [id])
        row = rows[0]
        item = Albums(row['title'], row['release_year'], row['artist_id'])
        return item
    def create(self, new_record):
        self._connection.execute(f'INSERT INTO albums (title, release_year, artist_id) VALUES (%s, %s, %s)', [new_record.title, new_record.release_year, new_record.artist_id])
        return None
    def delete(self, id):
        self._connection.execute(f'DELETE FROM albums WHERE id = %s', [id])
        return None
