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
function updateCountdown() {
  const countdownElement = document.getElementById('countdown');
  // End date
  const endDate = new Date('2023-12-01T00:00:00Z');

  const now = new Date();
  const timeDifference = endDate - now;

  const days = Math.floor(timeDifference / (1000 * 60 * 60 * 24));
  const hours = Math.floor((timeDifference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  const minutes = Math.floor((timeDifference % (1000 * 60 * 60)) / (1000 * 60));
  const seconds = Math.floor((timeDifference % (1000 * 60)) / 1000);

  countdownElement.textContent = `Tid innan val låses in: ${days}d ${hours}h ${minutes}m ${seconds}s`;
}

// Update the countdown every second
setInterval(updateCountdown, 1000);
