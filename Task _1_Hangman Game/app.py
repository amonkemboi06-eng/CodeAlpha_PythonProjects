from flask import Flask, render_template, request,redirect
from Hangman import HangmanGame

app = Flask(__name__)

game = HangmanGame()

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":
        letter = request.form["letter"]
        game.guess_letter(letter)

    if game.is_won() or game.is_lost():
      return render_template(
        "index.html",
        word=game.get_word(),
        guesses_left=game.guesses_left(),
        guessed=game.guessed_letters,
        won=game.is_won(),
        lost=game.is_lost(),
        answer=game.word
    )

    return render_template(
        "index.html",
        word=game.get_word(),
        guesses_left=game.guesses_left(),
        guessed=game.guessed_letters,
        won=game.is_won(),
        lost=game.is_lost(),
        answer=""
    )

@app.route("/next")
def next_game():
    global game
    game = HangmanGame()    # Create a new game
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)