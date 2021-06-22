import collections
import datetime
from collections import Counter
from collections import OrderedDict

class Ratings:
    """
    Analyzing data from ratings.csv
    """
    def __init__(self, path_to_the_file):
        try:
            with open(path_to_the_file, 'r') as file:
                line = file.realine().strip().split(',')
                self.ratings = []
                while line:
                    self.ratings += [[int(line[0]), int(line[1]), float(line[2]), int(line[3])]]
                    line = file.realine().strip().split(',')
        except OSError as exception:
            raise OSError(exception)
        self.length = len(self.ratings)
    class Movies:    
        def dist_by_year(self):
            """
            The method returns a dict where the keys are years and the values are counts. 
            Sort it by years ascendingly. You need to extract years from timestamps.
            """
            return OrderedDict(sorted(dict(Counter([datetime.datetime.fromtimestamp(x[3]) for x in self.ratings])).items()))
        
        def dist_by_rating(self):
            """
            The method returns a dict where the keys are ratings and the values are counts.
            Sort it by ratings ascendingly.
            """
            return OrderedDict(sorted(dict(Counter([x[2] for x in self.ratings])).items()))
        
        def top_by_num_of_ratings(self, n): ############################################################################
            """
            The method returns top-n movies by the number of ratings. 
            It is a dict where the keys are movie titles and the values are numbers.
            Sort it by numbers descendingly.
            """
            if n > self.length:
                raise IndexError('Index out of ratings\' range')
            top_id = sorted(self.raitings, key=lambda x: x[2], reverse=True)[:n]
            #return top_movies
        
        #def top_by_ratings(self, n, metric=average): ####################################################################
            # """
            # The method returns top-n movies by the average or median of the ratings.
            # It is a dict where the keys are movie titles and the values are metric values.
            # Sort it by metric descendingly.
            # The values should be rounded to 2 decimals.
            # """
            #return top_movies
        
        def top_controversial(self, n):
            """
            The method returns top-n movies by the variance of the ratings.
            It is a dict where the keys are movie titles and the values are the variances.
          Sort it by variance descendingly.
            The values should be rounded to 2 decimals.
            """
            return top_movies

    class Users:
        """
        In this class, three methods should work. 
        The 1st returns the distribution of users by the number of ratings made by them.
        The 2nd returns the distribution of users by average or median ratings made by them.
        The 3rd returns top-n users with the biggest variance of their ratings.
     Inherit from the class Movies. Several methods are similar to the methods from it.
        """
