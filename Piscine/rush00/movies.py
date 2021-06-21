class Movies:
    """
    Analyzing data from movies.csv
    """
    def __init__(self, path_to_the_file):
        try:
            with open(path_to_the_file, 'r') as file:
                line = file.realine().strip().split(',')
                self.movies = []
                while line:
                    self.movies += [[int(line[0]), int(line[1]), float(line[2]), int(line[3])]]
                    line = file.realine().strip().split(',')
        except OSError as exception:
            raise OSError(exception)
        self.length = len(self.movies)

    def dist_by_release(self):
        """
        The method returns a dict or an OrderedDict where the keys are years and the values are counts. 
        You need to extract years from the titles. Sort it by counts descendingly.
        """
        return release_years
    
    def dist_by_genres(self):
        """
        The method returns a dict where the keys are genres and the values are counts.
     Sort it by counts descendingly.
        """
        return genres
        
    def most_genres(self, n):
        """
        The method returns a dict with top-n movies where the keys are movie titles and 
        the values are the number of genres of the movie. Sort it by numbers descendingly.
        """
        return movies
