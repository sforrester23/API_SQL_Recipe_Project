from recipe_class import *
from recipe_db_connect import *

server = 'localhost,1433'
database = 'Recipe_Book'
username = 'SA'
password = 'Passw0rd2018'

recipe_db = Recipe_db(server, database, username, password)
# recipe_db.print_all_recipe_info()
# print(recipe_db.search_recipe_name('Chicken Fajitas'))
# recipe_db.add_recipe('Super Noodles', 'Super Noodles, Water', '1) Boil kettle. 2) Add water to super noodles and heat for 5 mins. 3) Drain and serve.', 'CA11 9QG')
# recipe_db.update_recipe('Postcode', 'TQ1 3JJ', 'Postcode', 'CA11 9QG')
# recipe_db.delete_recipe('Super Noodles')

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


all_recipe_query = recipe_db.query_all_recipes()
while True:
    record = all_recipe_query.fetchone()
    if record is None:
        break
    recipe = Recipe(record[0], record[1], record[2], record[3])
    recipe_db.append_object_to_list(recipe)

print(recipe_db.recipe_list)
recipe_4_list=[recipe_db.recipe_list[3].name, recipe_db.recipe_list[3].ingredients, recipe_db.recipe_list[3].instructions, recipe_db.recipe_list[3].postcode]
print(recipe_4_list)

recipe_4 = recipe_db.recipe_list[3]
recipe_4.write_recipe_to_file('recipe_info.txt')


# write information to list
# recipe_db.make_recipe_dictionary()
# print(recipe_db.recipe_dict)




# recipe_db.make_recipe_dictionary()
#
# print(recipe_db.recipe_dict)

