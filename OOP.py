class Movie:
    def __init__(self, name, release_year, genre):
        self.name = name
        self.release_year = release_year
        self.genre = genre

    def get_name(self):
        return self.name

    def get_release_year(self):
        return self.release_year

    def get_genre(self):
        return self.genre

    def set_name(self, name):
        self.name = name

    def set_release_year(self, release_year):
        self.release_year = release_year

    def set_genre(self, genre):
        self.genre = genre


the_perks_of_being_a_wallflower = Movie("The Perks of Being a Wallflower", 2012, "Drama")
print(the_perks_of_being_a_wallflower.get_name() + " is a " + the_perks_of_being_a_wallflower.get_genre() + " that was released in " + str(the_perks_of_being_a_wallflower.get_release_year()) + ".")
