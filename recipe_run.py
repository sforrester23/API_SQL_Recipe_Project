from recipe_class import *
from recipe_db_connect import *

# Make the class instance for the database
server = 'localhost,1433'
database = 'Recipe_Book'
username = 'SA'
password = 'Passw0rd2018'

recipe_db = Recipe_db(server, database, username, password)
# testing methods for CRUD (Creating, Reading, Updating, Deleting)
# recipe_db.print_all_recipe_info()
# print(recipe_db.search_recipe_name('Chicken Fajitas'))
# recipe_db.add_recipe('Super Noodles', 'Super Noodles, Water', '1) Boil kettle. 2) Add water to super noodles and heat for 5 mins. 3) Drain and serve.', 'CA11 9QG')
# recipe_db.update_recipe('Postcode', 'TQ1 3JJ', 'Postcode', 'CA11 9QG')
# recipe_db.delete_recipe('Super Noodles')

# Make the recipe info into a dictionary of dictionaries, testing before moving to a method in the db class
# all_recipe_query = recipe_db.query_all_recipes()
# recipe_dict = {}
# count = 1
# while True:
#     recipe = {}
#     record = all_recipe_query.fetchone()
#     if record is None:
#         break
#     recipe['Recipe Name']=record[0]
#     recipe['Ingredients']=record[1]
#     recipe['Instructions'] = record[2]
#     recipe['Postcode'] = record[3]
#     recipe_dict['Recipe #{}'.format(count)] = recipe
#     count+=1
# print(recipe_dict)

# recipe_db.append_recipe_elements()
# print(recipe_db.recipe_list)

# make the recipe information into a list
all_recipe_query = recipe_db.query_all_recipes()
while True:
    record = all_recipe_query.fetchone()
    if record is None:
        break
    recipe = Recipe(record[0], record[1], record[2], record[3])
    recipe_db.append_object_to_list(recipe)

# print the recipe list stored in the db class
print(recipe_db.recipe_list)
# get a particular element of the recipe list for testing
# recipe_4_list=[recipe_db.recipe_list[3].name, recipe_db.recipe_list[3].ingredients, recipe_db.recipe_list[3].instructions, recipe_db.recipe_list[3].postcode]
# print(recipe_4_list)


# for loop for iterating over recipe list and writing the information to a file. The write file extracts the attributes from their class objects so they can be viewed in normal terms, not class object terms
# for index in range(len(recipe_db.recipe_list)):
#     open('recipe_info.txt', 'a').write('Recipe {} \n'.format(index+1))
#     recipe_db.recipe_list[index].write_recipe_to_file('recipe_info.txt')
#     open('recipe_info.txt', 'a').write('\n')

# get all the recipe class objects to test the print
recipe_1 = recipe_db.recipe_list[0]
recipe_2 = recipe_db.recipe_list[1]
recipe_3 = recipe_db.recipe_list[2]
recipe_4 = recipe_db.recipe_list[3]
recipe_5 = recipe_db.recipe_list[4]
# recipe_1.write_recipe_to_file('recipe_info.txt')
# recipe_2.write_recipe_to_file('recipe_info.txt')
# recipe_3.write_recipe_to_file('recipe_info.txt')
# recipe_4.write_recipe_to_file('recipe_info.txt')
# recipe_5.write_recipe_to_file('recipe_info.txt')

print(recipe_1.json_for_postcode())

# testing the method that makes the recipes into a dictionary of dictionaries
# write information to
# recipe_db.make_recipe_dictionary()
# print(recipe_db.recipe_dict)

for index in range(len(recipe_db.recipe_list)):
    write(recipe_db.recipe_list[index].json_for_postcode())


