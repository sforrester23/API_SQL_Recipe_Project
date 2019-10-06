from recipe_db_connect import *
import requests
# Define a class recipe
class Recipe():
    # Give it the new attributes
    def __init__(self, name, ingredients, instructions, postcode):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
        self.postcode = postcode

    # defining the methods
    # define a method to export recipe to txt

    # define a method to take a class object of recipe and write it to a txt file
    def write_recipe_to_file(self, file):
        recipe_info = [self.name, self.ingredients, self.instructions, self.postcode]
        recipe_titles = ['Recipe Name', 'Ingredients', 'Instructions', 'Postcode']
        for index in range(len(recipe_info)):
            try:
                with open(file, 'a') as opened_file:
                    opened_file.write(recipe_titles[index] + ': ' + recipe_info[index] + '\n')

                opened_file.close()
            except FileNotFoundError:
                print('File not Found')


    # get postcode information
    def get_postcode(self):
        return self.postcode

    # define a method for getting the information on the postcode in the recipe from the API
    def json_for_postcode(self):
        resp = requests.get('http://api.postcodes.io/postcodes/' + self.postcode)
        return resp.json()['result']



