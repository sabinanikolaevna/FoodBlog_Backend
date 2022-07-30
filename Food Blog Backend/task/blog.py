
import sqlite3



food_blog = sqlite3.connect('food_blog.db')
c = food_blog.cursor()
c.execute('''CREATE TABLE meals (
meal_id int AUTO_INCREMENT PRIMARY KEY,
meal_name text not null UNIQUE)''')
c.execute('''CREATE TABLE ingredients (
ingredient_id int AUTO_INCREMENT PRIMARY KEY,
ingredient_name text not null UNIQUE)''')
c.execute('''CREATE TABLE measures (
measure_id int AUTO_INCREMENT PRIMARY KEY,
measure_name text UNIQUE)''')
data = {"meals": ("breakfast", "brunch", "lunch", "supper"),
        "ingredients": ("milk", "cacao", "strawberry", "blueberry", "blackberry", "sugar"),
        "measures": ("ml", "g", "l", "cup", "tbsp", "tsp", "dsp", "")}



for i in data['meals']:
        c.execute(f'''INSERT INTO meals (meal_name) 
        VALUES ("{i}")''')
for i in data['ingredients']:
        c.execute(f'''INSERT INTO ingredients (ingredient_name)
        VALUES ("{i}")''')
for i in data['measures']:
        c.execute(f'''INSERT INTO measures (measure_name) 
        VALUES ("{i}")''')

food_blog.commit()
food_blog.close()



food_blog = sqlite3.connect('food_blog.db')
c = food_blog.cursor()
c.execute('''CREATE TABLE recipes (
recipe_id int AUTO_INCREMENT PRIMARY KEY,
recipe_name text not null,
recipe_description text)''')
food_blog.commit()
food_blog.close()


food_blog = sqlite3.connect('food_blog.db')
c = food_blog.cursor()

c.execute('''CREATE TABLE serve (
serve_id int AUTO_INCREMENT PRIMARY KEY,
recipe_id int not null,
meal_id int not null,
FOREIGN KEY(recipe_id) REFERENCES recipes(recipe_id),
FOREIGN KEY(meal_id) REFERENCES meals(meal_id))''')





food_blog.commit()
food_blog.close()



food_blog = sqlite3.connect('food_blog.db')
c = food_blog.cursor()

c.execute('''CREATE TABLE quantity (
quantity_id int AUTO_INCREMENT PRIMARY KEY,
measure_id int not null,
ingredient_id int not null,
quantity int not null,
recipe_id int not null,
FOREIGN KEY(measure_id) REFERENCES measures(measure_id),
FOREIGN KEY(ingredient_id) REFERENCES ingredients(ingredient_id),
FOREIGN KEY(recipe_id) REFERENCES recipes(recipe_id))''')
food_blog.commit()
food_blog.close()


food_blog = sqlite3.connect('food_blog.db')
c = food_blog.cursor()
print('Pass the empty recipe name to exit.')
while True:
        name = input('Recipe name:')
        if name != '':
                description = input('Recipe description:')
                c.execute(f'''INSERT INTO recipes (recipe_name, recipe_description)
                VALUES ("{name}", "{description}")''')
                serving = input('1) breakfast  2) brunch  3) lunch  4) supper \nEnter proposed meals separated by a space:')
                if '1' in serving:
                        c.execute(f'''INSERT INTO serve (recipe_id, meal_id) 
                        VALUES ("{name}", "breakfast")''')
                if '2' in serving:
                        c.execute(f'''INSERT INTO serve (recipe_id, meal_id) 
                        VALUES ("{name}", "brunch")''')
                if '3' in serving:
                        c.execute(f'''INSERT INTO serve (recipe_id, meal_id) 
                        VALUES ("{name}", "lunch")''')
                if '4' in serving:
                        c.execute(f'''INSERT INTO serve (recipe_id, meal_id) 
                        VALUES ("{name}", "supper")''')
                while True:
                        string = list(input('Input quantity of ingredient <press enter to stop>:').split())
                        if len(string) == 2:
                                quantity = string[0]
                                ingredient = string[1]
                                if ingredient not in data['ingredients']:
                                    print('The ingredient is not conclusive!')
                                c.execute(f'''INSERT INTO quantity (quantity, measure_id, ingredient_id, recipe_id) 
                                VALUES ("{quantity}", "", "{ingredient}", "{name}")''')
                        elif len(string) == 3:
                                quantity = string[0]
                                measure = string[1]
                                ingredient = string[2]
                                if measure not in data['measures']:
                                        print('The measure is not conclusive!')
                                if ingredient not in data['ingredients']:
                                        print('The ingredient is not conclusive!')
                                c.execute(f'''INSERT INTO quantity (quantity, measure_id, ingredient_id, recipe_id) 
                                                VALUES ("{quantity}", "{measure}", "{ingredient}", "{name}")''')

                        if len(string) == 0:
                                break
        else:
                break

food_blog.commit()
food_blog.close()
