from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/konton.py', methods=['POST'])
def register():
    # Get registration data from the form (similar to your previous code)
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')

    # Save the registration data (similar to your previous code)

    # Redirect to the index.html page after successful registration
    return redirect('index.html')

if __name__ == '__main__':
    app.run(debug=True)