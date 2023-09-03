// script.js

document.addEventListener('DOMContentLoaded', function () {
    const submitButton = document.getElementById('submit-guess');
    const winsSelect = document.getElementById('wins-guess');
    const goalsInput = document.getElementById('goals-guess');
    const shotsInput = document.getElementById('shots-guess');
    const resultMessage = document.getElementById('result');

    submitButton.addEventListener('click', function () {
        const winsGuess = parseInt(winsSelect.value);
        const goalsGuess = parseInt(goalsInput.value);
        const shotsGuess = parseInt(shotsInput.value);

        // Send the user's guesses to the Python backend
        fetch('/guess', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: `winsGuess=${winsGuess}&goalsGuess=${goalsGuess}&shotsGuess=${shotsGuess}`,
        })
        .then(response => response.json())
        .then(data => {
            // Display the result message from the backend
            resultMessage.textContent = data.message;
            resultMessage.style.color = data.color || 'black';
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
});