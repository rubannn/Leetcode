from sortedcontainers import SortedList
import collections


class FoodRatings(object):
    def __init__(self, foods, cuisines, ratings):
        self.ratings = {}
        self.cuisines = {}
        self.rating_by_cuisine = collections.defaultdict(lambda: SortedList())
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.ratings[food] = rating
            self.cuisines[food] = cuisine
            self.rating_by_cuisine[self.cuisines[food]].add((-rating, food))

    def changeRating(self, food, newRating):
        oldRating = -self.ratings[food]
        self.ratings[food] = newRating
        self.rating_by_cuisine[self.cuisines[food]].remove((oldRating, food))
        self.rating_by_cuisine[self.cuisines[food]].add((-newRating, food))

    def highestRated(self, cuisine):
        return self.rating_by_cuisine[cuisine][0][1]
