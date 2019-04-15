"""Restaurant rating lister."""
def rate_restaurant(filename):
    """Returns restaurants and their ratings"""

    restaurant_file = open(filename)
    restaurant_rating = {}
    for line in restaurant_file:
        line = line.strip()
        words = line.split(':')
        restaurant_rating[words[0]] = words[1]
    name = input("Please enter a restaurant name: \n ")
    rate = input("Please rate the restaurant: \n")
    restaurant_rating[name] = rate
    for restaurant, rating in sorted(restaurant_rating.items()):
        print(f"{restaurant} is rated at {rating}")

    restaurant_file.close()
rate_restaurant("scores.txt")   


# put your code here
