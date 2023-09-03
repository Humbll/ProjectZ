from flask import Flask, request, jsonify

app = Flask(__name__)

# Create a dictionary to store user guesses
user_guesses = {
    "winsGuess": None,
    "goalsGuess": None,
    "shotsGuess": None
}

@app.route('/guess', methods=['POST'])
def process_guess():
    global user_guesses  # Use the global user_guesses dictionary

    # Get user's guesses from the request
    wins_guess = int(request.form.get('winsGuess'))
    goals_guess = int(request.form.get('goalsGuess'))
    shots_guess = int(request.form.get('shotsGuess'))

    # Save the user's guesses in the global dictionary
    user_guesses["winsGuess"] = wins_guess
    user_guesses["goalsGuess"] = goals_guess
    user_guesses["shotsGuess"] = shots_guess

    # Correct the guesses (replace with your correction logic)
    corrected_wins = 4
    corrected_goals = 2
    corrected_shots = 12

    # Compare user's guesses with corrected values
    if (
        wins_guess == corrected_wins and
        goals_guess == corrected_goals and
        shots_guess == corrected_shots
    ):
        result_message = "Congratulations! Your guesses are correct."
        result_color = "green"
    else:
        result_message = "Sorry, your guesses are incorrect. Try again."
        result_color = "red"

    # Create a response with the result message and color
    response_data = {
        "message": result_message,
        "color": result_color
    }

    return jsonify(response_data)

@app.route('/get_guesses', methods=['GET'])
def get_user_guesses():
    global user_guesses  # Use the global user_guesses dictionary

    # Retrieve and return the user's guesses
    return jsonify(user_guesses)

if __name__ == '__main__':
    app.run(debug=True)
