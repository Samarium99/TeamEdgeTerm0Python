import os
from flask import Flask, render_template, request, json, jsonify, current_app as app # flask + other related libraries
import requests # requests is for apis, requesting info, request is for flask
app = Flask(__name__)

enter_path = os.path.join(app.static_folder, 'data', 'places.json') #defines the path to opening places.json

@app.route('/')
def index():
    title = "The Root"
    return render_template('index.html', title=title)

@app.route('/recipe.html')
def recipe():
    title = "Recipe Book"
    return render_template('recipe.html', title=title)

@app.route('/help.html')
def help():
    title = "User Manual"
    return render_template('help.html', title=title)

# ---- identifying parameters for navigating and completing the game + last app.route ----
inventory = [] # gift collector
recipe_quota = ['A baking set', 'A jug of milk', 'A basket of eggs', 'A basket of wild berries', 'A bundle of wheat', 'The Golden Flame'] 
# necessary gifts for completion

def check_completion():
    if set(recipe_quota).issubset(set(inventory)):      # checking which answer you get depending on if everything in quota is in inventory.
        global complete
        complete = True
    else:
        complete = False

@app.route('/api/v1/search', methods=['GET', 'POST'])
def enter_location():

    with open(enter_path, 'r') as jsondata: # defines jsondata as opening and reading the defined places.json file
        opened_lib = json.load(jsondata) # library is the action of opening the json dictionary
        
    if 'reset' in request.args['enter'].title():
        inventory.clear()
    elif 'Sunset Hallow' in request.args['enter'].title():
        check_completion()
        if complete == False: # in request.args['enter'].title():can't enter
            enter = "Try Again"
            description = "'You shall not enter,' said Gordan Ramsey. 'I do not yet smell the delectable aroma of [insert food]. Please find all of the necessary ingredients and come back'"  
            gift = "[NOTHING]"
        else:               #THE END
            for dict in opened_lib:
                if dict['location'] == 'Sunset Hallow':
                    enter = dict["location"]
                    description = dict["description"]
                    gift = dict["gift"]
    elif 'enter' in request.args:
        location = request.args['enter'].title() # the requested location is what the user writes enter =
        for dict in opened_lib: #checking every dictionary item in the list
            if location  in dict['location'].replace("'", "") :
                #**** may need to be fixed for different inputted formatting # if the requested location matches with that listed as a value.
                enter = dict['location'] # for jinja, this is the location user enters
                description = dict['description'] # for jinja, this is the description.
                gift = dict['gift'] # for jinja this is the gift
                if dict ['gift'] not in inventory:
                    inventory.append(dict['gift']) # this will be checked for when the user has all materials and enters Sunset Hollow.
                # when u go to the location, it adds an item to your inventory
    return render_template ( "portal.html", enter=enter, description=description, gift=gift, inventory=inventory)


if __name__ == '__main__':
    app.run(debug=True)

