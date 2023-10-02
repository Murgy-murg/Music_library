from lib.albums import Albums
from lib.albums_repository import AlbumRepository

#create test to return list of all album objects in seed data

def test_return_list_of_all_albums_from_seed_data(db_connection):
    db_connection.seed('seeds/music_library.sql')
    repository = AlbumRepository(db_connection)
    albums = repository.all()

    assert albums == [
Albums('Doolittle', 1989, 1),
Albums('Surfer Rosa', 1988, 1),
Albums('Waterloo', 1974, 2),
Albums('Super Trouper', 1980, 2),
Albums('Bossanova', 1990, 1),
Albums('Lover', 2019, 3),
Albums('Folklore', 2020, 3),
Albums('I Put a Spell on You', 1965, 4),
Albums('Baltimore', 1978, 4),
Albums('Here Comes the Sun', 1971, 4),
Albums('Fodder on My Wings', 1982, 4),
Albums('Ring Ring', 1973, 2),
]

