# app.py

from flask import Flask, request, jsonify

app = Flask(__name__)

# Replace this with the actual number of wins for Team A
actual_wins = 10

@app.route('/')
def index():
    return "Welcome to the HLTV-Inspired Website"

@app.route('/guess', methods=['POST'])
def guess_wins():
    try:
        user_guess = int(request.form.get('guess'))
    except ValueError:
        return jsonify({'message': 'Please enter a valid number.', 'color': 'red'}), 400

    if user_guess == actual_wins:
        return jsonify({'message': 'Congratulations! You guessed correctly.', 'color': 'green'}), 200
    else:
        return jsonify({'message': f'Sorry, the actual number of wins is {actual_wins}. Try again.', 'color': 'red'}), 200

if __name__ == '__main__':
    app.run(debug=True)