# import flask module
from flask import Flask, render_template
 
# instance of flask application
app = Flask(__name__)

#sending top pics recipe to the frontend
RECIPE = [
    {
        'id' : 1,
        'image' : 'butterChicken.jpg',
        'title' : 'Butter Chicken',
        'cuisine' : 'Indian Mughlai',
        'calories' : '230 kcal'
    },
    {
        'id' : 2,
        'image' : 'khoSuey.jpg',
        'title' : 'Khao suey',
        'cuisine' : 'Thai',
        'calories' : '230 kcal'
    },
    {
        'id' : 3,
        'image' : 'dumplings.jpg',
        'title' : 'Dumplings',
        'cuisine' : 'Pan Asian',
        'calories' : '230 kcal'
    }
]
 
# home route that returns below text when root url is accessed
@app.route("/")
def hello_world():
    return render_template('home.html', recipe=RECIPE)
 
if __name__ == '__main__':  
   app.run()