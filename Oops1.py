class sample:
    pass


a=sample()


from collections import defaultdict
class FoodRatings:
    def __init__(self, foods, cuisines, ratings):
        self.map1 = defaultdict(set)  # cuisine -> (rating, food)
        self.map2 = defaultdict(list)  # food -> (cuisine, rating)
        for x, y, z in zip(foods, cuisines, ratings):
            self.map1[y].add((-z, x))
            self.map2[x].append((y, z))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, rating = self.map2[food][0]
        self.map1[cuisine].remove((-rating, food))
        self.map1[cuisine].add((-newRating, food))
        self.map2[food][0] = (cuisine, newRating)

    def highestRated(self, cuisine: str) -> str:
        return self.map1[cuisine][0][1]
    
#food=FoodRatings(["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7])
