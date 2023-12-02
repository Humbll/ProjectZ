document.addEventListener('DOMContentLoaded', function () {
    const submitButton = document.getElementById('submit-guess');
    const lockAllButton = document.getElementById('lock-all-button');
    const guessSelects = document.querySelectorAll('.guess-select');
    const resultMessage = document.getElementById('result');
    let guessesLocked = false;

    // Function to set a value in Local Storage
    function setLocalStorageItem(key, value) {
        localStorage.setItem(key, value);
    }

    // Function to get a value from Local Storage
    function getLocalStorageItem(key) {
        return localStorage.getItem(key);
    }

    // Load and set the last saved guesses from Local Storage
    guessSelects.forEach(guessSelect => {
        const guessType = guessSelect.id;
        const lastGuess = getLocalStorageItem(guessType);
        if (lastGuess !== null) {
            guessSelect.value = lastGuess;
        }
    });

    // Lock/Unlock all guesses
    lockAllButton.addEventListener('click', function () {
        if (!guessesLocked) {
            guessSelects.forEach(guessSelect => {
                guessSelect.disabled = true;
                // Save the current value in Local Storage
                setLocalStorageItem(guessSelect.id, guessSelect.value);
            });
            lockAllButton.textContent = "Unlock All";
            guessesLocked = true;
        } else {
            guessSelects.forEach(guessSelect => {
                guessSelect.disabled = false;
            });
            lockAllButton.textContent = "Lock All";
            guessesLocked = false;
        }
    });

    // Submit guesses
    submitButton.addEventListener('click', function () {
        if (guessesLocked) {
            resultMessage.textContent = "Guesses submitted.";
            resultMessage.style.color = "green";
        } else {
            resultMessage.textContent = "Please lock all guesses before submitting.";
            resultMessage.style.color = "red";
        }
    });
});

function removePlaceholderOption(selectElement) {
    // Get the selected option value
    const selectedValue = selectElement.value;

    // Find the placeholder option with an empty value
    const placeholderOption = selectElement.querySelector('option[value=""]');

    // If a valid option is selected (non-empty value), remove the placeholder option
    if (selectedValue !== "") {
        placeholderOption.remove();
    }
}

        // Function to toggle the dropdown content
        function toggleDropdown(button) {
          var dropdown = button.nextElementSibling;
          if (dropdown.style.display === "block") {
              dropdown.style.display = "none";
          } else {
              dropdown.style.display = "block";
          }
      }

      // Close the dropdown when clicking outside
      window.addEventListener("click", function(event) {
          var dropdowns = document.querySelectorAll(".custom-dropdown");
          for (var i = 0; i < dropdowns.length; i++) {
              var dropdown = dropdowns[i];
              if (!dropdown.contains(event.target)) {
                  dropdown.querySelector(".dropdown-content").style.display = "none";
              }
          }
      });
