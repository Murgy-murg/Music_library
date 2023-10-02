from lib.albums import Albums

#test album constructor

def test_that_constructs_albums_with_title_release_year_and_artist_id():
    album = Albums('Run come ya', 1981, 4)
    assert album.title == 'Run come ya'
    assert album.release_year == 1981
    assert album.artist_id == 4

#test that given instance matches what is based on our records
def test_compare_identical_albums():
    album1 = Albums('hello', 1999, 7)
    album2 = Albums('hello', 1999, 7)
    assert album1 == album2

#test that formatted nicely

def test_given_instance_is_formatted():
    album1 = Albums('hello', 1999, 7)
    assert str(album1) == "Albums(hello, 1999, 7)"