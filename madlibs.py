"""A madlib game that compliments its users."""

from random import choice, sample

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = sample(AWESOMENESS, 3)
    #pass a list of three compliements 

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)

@app.route('/game')
def show_madlib_form():
    """Gets user's response to 'Would you like to play a game?'"""

#if user says no return a rendered template  goodbye.html
    play_game = request.args.get("game")

    if play_game == "yes":
        return render_template("game.html")

    else:
        return render_template("goodbye.html")

@app.route('/madlib')
def show_madlib():
    """Provides user input into a Madlibs story'"""

    name = request.args.get("person")
    color = request.args.get("color")
    noun = request.args.get("noun")
    adjective = request.args.get("adjective")
    city = request.args.get("city")
    pet = request.args.get("pet")
    pet_name = request.args.get("pet_name")
    destination = request.args.get("destination")
    sport = request.args.get("sport")

    templates = ["madlib.html", "madlibs2.html", "madlibs3.html"]

    template = choice(templates)

    return render_template(template, person=name, color=color, noun=noun, 
        adjective=adjective, city=city, pet=pet, pet_name=pet_name, 
        destination=destination, sport=sport)



if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
