from recipe_db_connect import *
# Define a class recipe
class Recipe():
    # Give it the new attributes
    def __init__(self, name, ingredients, instructions, postcode):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
        self.postcode = postcode

    # defining the methods

    # new()
        # create a recipe obj

    # save()
        # save a recipe objc to the DB (make persistant)

    # read() - on the DB class methods
        # read one object

    # all() - on the DB class methods
        # get all the instances from the DB
        # get each record
        # create individual instances of recipe
        # store in a list
        # return the list

    # destroy()
        # destroy one object

    # get postcode information