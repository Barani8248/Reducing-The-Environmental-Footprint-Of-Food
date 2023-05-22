from flask import Flask, render_template

app = Flask(_name_)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')

if _name_ == '_main_':
    app.run()
import ibm_db

# Obtain your DB2 credentials and connection details
conn = ibm_db.connect("<dsn_string>", "", "")

@app.route('/register', methods=['POST'])
def register():
    # Retrieve user registration data from the request
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')

    # Execute an SQL query to insert the user data into the database
    query = f"INSERT INTO users (username, email, password) VALUES ('{username}', '{email}', '{password}')"
    stmt = ibm_db.exec_immediate(conn, query)

    # Perform any necessary error handling or response logic

# Remember to close the database connection when the application stops
@app.teardown_appcontext
def teardown_db(exception):
    if conn is not None:
        ibm_db.close(conn)

if _name_ == '_main_':
    app.run()
 @app.route('/login', methods=['POST'])
def login():
    # Retrieve user login data from the request
    username = request.form.get('username')
    password = request.form.get('password')

    # Execute an SQL query to retrieve the user data from the database
    query = f"SELECT * FROM users WHERE username = '{username}'"
           stmt = ibm_db.exec_immediate(conn, query)

       # Fetch the result of the query
       result = ibm_db.fetch_assoc(stmt)

       # Check if the username exists in the database and compare passwords
       if result is not None and result['password'] == password:
           # Authentication successful
           # Perform any necessary logic for a successful login
           return "Login successful"
       else:
           # Authentication failed
           # Perform any necessary logic for a failed login
           return "Login failed"