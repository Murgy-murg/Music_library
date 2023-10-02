class Albums:
    # Initialise our attributes
    # Each Column in the table should have one of these attributes
    def __init__(self, title, release_year, artist_id):
        #Set attribute
        self.title = title
        self.release_year = release_year
        self.artist_id = artist_id


    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    #tests whether the instances it expects are the same ones based on our records

    def __repr__(self):
        #return f"Album"
        return f"Albums({self.title}, {self.release_year}, {self.artist_id})"