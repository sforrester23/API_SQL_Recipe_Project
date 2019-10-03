# Import the necessaries
import pyodbc

# Set up the class for the database of recipes
class Recipe_db():
    def __init__(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.connect_db = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)
        self.cursor = self.connect_db.cursor()
        self.recipe_list = []
        self.recipe_dict = {}

    # Define a method for running a query, but encapsulate it so it can only be run from inside this script (by other methods)
    def __filter_query(self, query):
        return self.cursor.execute(query)

    # Define a method for getting all the data from the database
    def query_all_recipes(self):
        return self.__filter_query("SELECT * FROM Recipe_List")

    # Define a method for print all the recipe info
    def print_all_recipe_info(self):
        all_recipe_query = self.query_all_recipes()
        while True:
            record = all_recipe_query.fetchone()
            if record is None:
                break
            print(record)

    # Define a method to search for a recipe based on the name of it
    def search_recipe_name(self, Recipe_Name):
        recipe_name_query = self.__filter_query("SELECT * FROM Recipe_List WHERE Recipe_Name = '{}'".format(str(Recipe_Name)))
        return recipe_name_query.fetchone()

    # Define a method to add a recipe to the table
    def add_recipe(self, recipe_name, recipe_ingredients, recipe_instructions, recipe_postcode):
        self.__filter_query("INSERT INTO Recipe_List VALUES ('{}', '{}', '{}', '{}')".format(recipe_name, recipe_ingredients, recipe_instructions, recipe_postcode))
        self.connect_db.commit()
        print('Add Command Executed')

    # Define a method to update a value in the table
    def update_recipe(self, value_to_update, new_value, column_condition, condition_value):
        self.__filter_query("UPDATE Recipe_List SET {} = '{}' WHERE {} = '{}'".format(value_to_update, new_value, column_condition, condition_value))
        self.connect_db.commit()
        print('Update Command Executed')

    # Define a method to delete a recipe from the table
    def delete_recipe(self, recipe_name):
        self.__filter_query("DELETE FROM Recipe_List WHERE Recipe_Name = '{}'".format(recipe_name))
        self.connect_db.commit()
        print('Delete Command Executed')

    # define a method for appending object items to list
    def append_object_to_list(self, object):
        self.recipe_list.append(object)

    # define a method for making the recipe information into a list (not sure how needed this is)
    def append_all_recipe_elements(self):
        all_recipe_query = self.query_all_recipes()
        while True:
            record = all_recipe_query.fetchone()
            if record is None:
                break
            self.recipe_list.append(record)

    # define a method for making the recipe list into a dictionary
    def make_recipe_dictionary(self):
        all_recipe_query = self.query_all_recipes()
        count = 1
        while True:
            recipe = {}
            record = all_recipe_query.fetchone()
            if record is None:
                break
            recipe['Recipe Name'] = record[0]
            recipe['Ingredients'] = record[1]
            recipe['Instructions'] = record[2]
            recipe['Postcode'] = record[3]
            self.recipe_dict['Recipe #{}'.format(count)] = recipe
            count += 1





