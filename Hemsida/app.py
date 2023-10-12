import requests
import pyodbc
import uuid
import hashlib


from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/register', methods=['POST'])
def register():
    # Get registration data from the form
    name = request.form.get('name')
    email = request.form.get('email')
    
    #hash passwords
    passwordtohash = request.form.get('password')
    hasher = hashlib.sha256()
    # Update the hasher with the bytes of the name
    hasher.update(passwordtohash.encode('utf-8'))
    # Get the hexadecimal representation of the hash
    password = hasher.hexdigest()

    
    context = pyodbc.connect(f'DRIVER={{ODBC Driver 18 for SQL Server}};server=localhost\\SQLExpress;database=master;Encrypt=No;Trusted_Connection=Yes',autocommit=True)
    cursor = context.cursor()
    cursor.execute('use test')
    
    id = uuid.uuid4()
    sql =  f''' 
    INSERT INTO accounts (
        id,
        name,
        password,
        email
    )
    VALUES (
        '{id}',
        '{name}',
        '{password}',
        '{email}'
    )
    '''
    
    cursor.execute(sql)
    
    # Redirect back to login.html after registration
    return redirect(url_for('register_page'))

@app.route('/register')
def register_page():
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)