from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/konton.py', methods=['POST'])
def register():
    # Get registration data from the form
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')

    # Save the registration data to konton.py
    with open('konton.py', 'a') as file:
        file.write(f'Name: {name}\n')
        file.write(f'Email: {email}\n')
        file.write(f'Password: {password}\n')
        file.write('\n')  # Add a newline separator

    # You can add additional logic for database storage or validation here

    # Redirect back to crystal_ball.html after registration
    return redirect(url_for('crystal_ball'))

@app.route('/konton.html')
def registration_page():
    return render_template('konton.html')

if __name__ == '__main__':
    app.run(debug=True)
