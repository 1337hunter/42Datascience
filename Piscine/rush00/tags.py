import collections

class Tags:
    """
    Analyzing data from tags.csv
    """
    def __init__(self, path_to_the_file):
        try:
            with open(path_to_the_file, 'r') as file:
                line = file.realine().strip().split(',')
                self.tags = []
                while line:
                    self.tags += [[int(line[0]), int(line[1]), line[2], int(line[3])]]
                    line = file.realine().strip().split(',')
        except OSError as exception:
            raise OSError(exception)
        self.length = len(self.tags)

    def most_words(self, n):
        """
        The method returns top-n tags with most words inside. It is a dict 
        where the keys are tags and the values are the number of words inside the tag.
        Drop the duplicates. Sort it by numbers descendingly.
        """
        if n > self.length:
            raise IndexError('Index out of tags\' range')
        sorted_list = sorted(self.tags, key=lambda x: len(x[2].split(' ')), reverse=True)
        return dict([[x[2], len(x[2].split(' '))] for x in sorted_list[:n]])

    def longest(self, n):
        """
        The method returns top-n longest tags in terms of the number of characters.
        It is a list of the tags. Drop the duplicates. Sort it by numbers descendingly.
        """
        if n > self.length:
            raise IndexError('Index out of tags\' range')
        sorted_list = sorted(self.tags, key=lambda x: len(x[2]), reverse=True)
        return [x[2] for x in sorted_list[:n]]

    def most_words_and_longest(self, n):
        """
        The method returns the intersection between top-n tags with most words inside and 
        top-n longest tags in terms of the number of characters.
        Drop the duplicates. It is a list of the tags.
        """
        return list(set(self.most_words(n).keys()) & set(self.longest(n).keys()))
        
    def most_popular(self, n):
        """
        The method returns the most popular tags. 
        It is a dict where the keys are tags and the values are the counts.
        Drop the duplicates. Sort it by counts descendingly.
        """
        return dict(collections.Counter([x[2] for x in self.tags]).most_common(n))
        
    def tags_with(self, word):
        """
        The method returns all unique tags that include the word given as the argument.
        Drop the duplicates. It is a list of the tags. Sort it by tag names alphabetically.
        """
        return sorted(list(set([x[2] for x in self.tags if word in x[2]])))
