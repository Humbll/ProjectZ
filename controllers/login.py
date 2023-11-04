import hashlib

# Simulated database of user data (replace with your actual user database)
user_database = {
    'username123': {
        'hashed_password': '7a2e0452e10d86c6e12b42bf3f4dd58676f0db8d212c3a52d3b72c754a5f1f59',  # Hashed password
        # Other user data
    }
}

def login(username, entered_password):
    if username in user_database:
        stored_hashed_password = user_database[username]['hashed_password']
        
        # Hash the entered password using the same hash algorithm
        hasher = hashlib.sha256()
        hasher.update(entered_password.encode('utf-8'))
        entered_hashed_password = hasher.hexdigest()
        
        # Compare the entered hashed password with the stored one
        if entered_hashed_password == stored_hashed_password:
            return True  # Passwords match, login successful
        else:
            return False  # Passwords don't match
    else:
        return False  # User not found

# Example usage
username = 'username123'
password = 'user_password123'  # Replace with the user's entered password
if login(username, password):
    print("Login successful!")
else:
    print("Login failed.")
