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
recipe_db.delete_recipe('Super Noodles')
recipe_db.print_all_recipe_info()
